#!/usr/bin/env python3
"""
Python Bibliometric Analysis Script
Alternative to R Biblioshiny

Author: Mahbub Hassan
Affiliation: Chulalongkorn University
Email: 6870376421@student.chula.ac.th

Purpose: Comprehensive bibliometric analysis using Python
Inputs: Web of Science or Scopus data
Outputs: Tables, plots, networks

Requirements: See requirements.txt
Installation: pip install -r requirements.txt
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import networkx as nx
from wordcloud import WordCloud
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11

# ==============================================================================
# SECTION 1: DATA LOADING & PREPARATION
# ==============================================================================

class BibliometricAnalysis:
    """Main class for bibliometric analysis"""

    def __init__(self, data_path, data_type='wos'):
        """
        Initialize analysis

        Parameters:
        -----------
        data_path : str
            Path to data file (.txt for WoS, .csv for Scopus)
        data_type : str
            'wos' or 'scopus'
        """
        self.data_path = data_path
        self.data_type = data_type
        self.df = None
        self.results = {}

        print(f"Initializing Bibliometric Analysis")
        print(f"Data type: {data_type}")
        print(f"File: {data_path}")

    def load_data(self):
        """Load bibliographic data"""
        if self.data_type == 'scopus':
            self.df = pd.read_csv(self.data_path)
            print(f"✓ Loaded {len(self.df)} records from Scopus")
        elif self.data_type == 'wos':
            # WoS requires custom parser
            self.df = self._parse_wos(self.data_path)
            print(f"✓ Loaded {len(self.df)} records from Web of Science")
        else:
            raise ValueError("data_type must be 'wos' or 'scopus'")

        return self

    def _parse_wos(self, filepath):
        """Parse Web of Science plain text format"""
        print("Parsing WoS file...")

        records = []
        current_record = {}

        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()

                if line.startswith('PT '):
                    if current_record:
                        records.append(current_record)
                    current_record = {}

                if len(line) > 3 and line[2] == ' ':
                    tag = line[:2]
                    content = line[3:]

                    if tag in current_record:
                        current_record[tag] += '; ' + content
                    else:
                        current_record[tag] = content

        if current_record:
            records.append(current_record)

        df = pd.DataFrame(records)

        # Rename columns
        column_mapping = {
            'AU': 'Authors',
            'TI': 'Title',
            'SO': 'Source',
            'PY': 'Year',
            'AB': 'Abstract',
            'DE': 'Author_Keywords',
            'TC': 'Citations',
            'CR': 'References',
            'C1': 'Affiliations'
        }

        df.rename(columns=column_mapping, inplace=True)

        # Convert year and citations to numeric
        df['Year'] = pd.to_numeric(df.get('Year', 0), errors='coerce')
        df['Citations'] = pd.to_numeric(df.get('Citations', 0), errors='coerce')

        return df

    # ================================================================
    # SECTION 2: DESCRIPTIVE STATISTICS
    # ================================================================

    def generate_statistics(self):
        """Generate main information table"""
        stats = {}

        stats['Total Documents'] = len(self.df)
        stats['Time Span'] = f"{int(self.df['Year'].min())}-{int(self.df['Year'].max())}"
        stats['Average Year'] = f"{self.df['Year'].mean():.1f}"

        # Authors
        if 'Authors' in self.df.columns:
            all_authors = []
            for authors in self.df['Authors'].dropna():
                all_authors.extend([a.strip() for a in str(authors).split(';')])
            stats['Total Authors'] = len(set(all_authors))
            stats['Authors per Document'] = len(all_authors) / len(self.df)

        # Sources
        if 'Source' in self.df.columns:
            stats['Total Sources'] = self.df['Source'].nunique()

        # Keywords
        if 'Author_Keywords' in self.df.columns:
            all_keywords = []
            for kw in self.df['Author_Keywords'].dropna():
                all_keywords.extend([k.strip() for k in str(kw).split(';')])
            stats['Total Keywords'] = len(set(all_keywords))

        # Citations
        if 'Citations' in self.df.columns:
            stats['Total Citations'] = int(self.df['Citations'].sum())
            stats['Average Citations'] = f"{self.df['Citations'].mean():.2f}"
            stats['Median Citations'] = int(self.df['Citations'].median())

        self.results['statistics'] = stats

        # Print statistics
        print("\n" + "="*60)
        print("MAIN INFORMATION")
        print("="*60)
        for key, value in stats.items():
            print(f"{key:.<40} {value}")
        print("="*60)

        return stats

    # ================================================================
    # SECTION 3: PUBLICATION TRENDS
    # ================================================================

    def analyze_trends(self, save_fig=True):
        """Analyze publication trends over time"""
        yearly_counts = self.df['Year'].value_counts().sort_index()

        plt.figure(figsize=(12, 6))
        plt.plot(yearly_counts.index, yearly_counts.values,
                marker='o', linewidth=2, markersize=8, color='#1f77b4')
        plt.fill_between(yearly_counts.index, yearly_counts.values, alpha=0.3)

        plt.title('Annual Scientific Production', fontsize=16, fontweight='bold')
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Number of Publications', fontsize=12)
        plt.grid(alpha=0.3)

        # Add trend line
        z = np.polyfit(yearly_counts.index, yearly_counts.values, 1)
        p = np.poly1d(z)
        plt.plot(yearly_counts.index, p(yearly_counts.index),
                "--", color='red', alpha=0.7, label='Trend')
        plt.legend()

        if save_fig:
            plt.savefig('output_annual_production.png', dpi=300, bbox_inches='tight')
            print("✓ Saved: output_annual_production.png")

        plt.show()

        # Calculate growth rate
        if len(yearly_counts) > 1:
            cagr = ((yearly_counts.iloc[-1] / yearly_counts.iloc[0]) **
                   (1/(len(yearly_counts)-1)) - 1) * 100
            print(f"\nCompound Annual Growth Rate: {cagr:.2f}%")

        self.results['trends'] = yearly_counts
        return yearly_counts

    # ================================================================
    # SECTION 4: MOST CITED PAPERS
    # ================================================================

    def most_cited_papers(self, top_n=10):
        """Identify most cited papers"""
        if 'Citations' not in self.df.columns:
            print("⚠ Citation data not available")
            return None

        top_cited = self.df.nlargest(top_n, 'Citations')[
            ['Title', 'Authors', 'Year', 'Source', 'Citations']
        ].copy()

        # Calculate citations per year
        current_year = pd.Timestamp.now().year
        top_cited['Citations_per_Year'] = top_cited['Citations'] / (
            current_year - top_cited['Year'] + 1
        )

        print(f"\n{'='*80}")
        print(f"TOP {top_n} MOST CITED PAPERS")
        print(f"{'='*80}")

        for idx, row in top_cited.iterrows():
            print(f"\n{row.name+1}. {row['Title']}")
            print(f"   Authors: {row['Authors'][:100]}...")
            print(f"   {row['Source']} ({int(row['Year'])})")
            print(f"   Citations: {int(row['Citations'])} (Avg: {row['Citations_per_Year']:.1f}/year)")

        self.results['top_cited'] = top_cited
        return top_cited

    # ================================================================
    # SECTION 5: MOST PRODUCTIVE AUTHORS
    # ================================================================

    def most_productive_authors(self, top_n=15):
        """Identify most productive authors"""
        if 'Authors' not in self.df.columns:
            print("⚠ Author data not available")
            return None

        # Extract all authors
        author_list = []
        for authors in self.df['Authors'].dropna():
            author_list.extend([a.strip() for a in str(authors).split(';')])

        # Count occurrences
        author_counts = Counter(author_list)
        top_authors = pd.DataFrame(
            author_counts.most_common(top_n),
            columns=['Author', 'Documents']
        )

        # Calculate h-index (simplified)
        top_authors['h-index'] = top_authors['Documents'].apply(
            lambda x: min(x, int(np.sqrt(x)))
        )

        print(f"\n{'='*60}")
        print(f"TOP {top_n} MOST PRODUCTIVE AUTHORS")
        print(f"{'='*60}")
        print(top_authors.to_string(index=False))

        # Visualization
        plt.figure(figsize=(10, 6))
        plt.barh(range(top_n), top_authors['Documents'].values[::-1], color='steelblue')
        plt.yticks(range(top_n), top_authors['Author'].values[::-1])
        plt.xlabel('Number of Documents')
        plt.title('Most Productive Authors', fontweight='bold')
        plt.tight_layout()
        plt.savefig('output_top_authors.png', dpi=300, bbox_inches='tight')
        print("\n✓ Saved: output_top_authors.png")
        plt.show()

        self.results['top_authors'] = top_authors
        return top_authors

    # ================================================================
    # SECTION 6: MOST RELEVANT JOURNALS
    # ================================================================

    def most_relevant_sources(self, top_n=15):
        """Identify most relevant journals/sources"""
        if 'Source' not in self.df.columns:
            print("⚠ Source data not available")
            return None

        source_counts = self.df['Source'].value_counts().head(top_n)

        print(f"\n{'='*60}")
        print(f"TOP {top_n} MOST RELEVANT SOURCES")
        print(f"{'='*60}")

        for rank, (source, count) in enumerate(source_counts.items(), 1):
            pct = (count / len(self.df)) * 100
            print(f"{rank:2d}. {source[:50]:.<50} {count:>4d} ({pct:>5.2f}%)")

        # Bradford's Law visualization
        cumsum = source_counts.cumsum() / len(self.df) * 100

        plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(source_counts)+1), cumsum.values,
                marker='o', linewidth=2)
        plt.axhline(y=33.3, color='r', linestyle='--', alpha=0.7, label='Core (33%)')
        plt.axhline(y=66.6, color='orange', linestyle='--', alpha=0.7, label='Zone 2 (67%)')
        plt.xlabel('Number of Sources')
        plt.ylabel('Cumulative % of Documents')
        plt.title("Bradford's Law - Source Distribution", fontweight='bold')
        plt.legend()
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.savefig('output_bradfords_law.png', dpi=300, bbox_inches='tight')
        print("\n✓ Saved: output_bradfords_law.png")
        plt.show()

        self.results['top_sources'] = source_counts
        return source_counts

    # ================================================================
    # SECTION 7: KEYWORD ANALYSIS
    # ================================================================

    def keyword_analysis(self, top_n=30):
        """Analyze author keywords"""
        if 'Author_Keywords' not in self.df.columns:
            print("⚠ Keyword data not available")
            return None

        # Extract all keywords
        keyword_list = []
        for keywords in self.df['Author_Keywords'].dropna():
            keyword_list.extend([k.strip().lower() for k in str(keywords).split(';')])

        keyword_counts = Counter(keyword_list)
        top_keywords = pd.DataFrame(
            keyword_counts.most_common(top_n),
            columns=['Keyword', 'Occurrences']
        )

        print(f"\n{'='*60}")
        print(f"TOP {top_n} AUTHOR KEYWORDS")
        print(f"{'='*60}")
        print(top_keywords.to_string(index=False))

        # Word cloud
        wordcloud = WordCloud(
            width=1200, height=600,
            background_color='white',
            colormap='viridis',
            relative_scaling=0.5,
            min_font_size=10
        ).generate_from_frequencies(keyword_counts)

        plt.figure(figsize=(15, 8))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Keyword Word Cloud', fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()
        plt.savefig('output_wordcloud.png', dpi=300, bbox_inches='tight')
        print("\n✓ Saved: output_wordcloud.png")
        plt.show()

        # Bar chart
        plt.figure(figsize=(12, 8))
        plt.barh(range(top_n), top_keywords['Occurrences'].values[::-1], color='coral')
        plt.yticks(range(top_n), top_keywords['Keyword'].values[::-1])
        plt.xlabel('Frequency')
        plt.title('Most Frequent Author Keywords', fontweight='bold')
        plt.tight_layout()
        plt.savefig('output_keywords_bar.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: output_keywords_bar.png")
        plt.show()

        self.results['top_keywords'] = top_keywords
        return top_keywords

    # ================================================================
    # SECTION 8: COUNTRY ANALYSIS
    # ================================================================

    def country_analysis(self, top_n=15):
        """Analyze country contributions"""
        if 'Affiliations' not in self.df.columns:
            print("⚠ Affiliation data not available")
            return None

        # Simple country extraction (first author country)
        # Note: This is simplified - production code needs better parsing
        country_list = []

        for affil in self.df['Affiliations'].dropna():
            # Very basic extraction - you'd want better logic here
            if 'USA' in str(affil) or 'United States' in str(affil):
                country_list.append('USA')
            elif 'China' in str(affil) or 'Peoples R China' in str(affil):
                country_list.append('China')
            elif 'UK' in str(affil) or 'England' in str(affil):
                country_list.append('UK')
            elif 'Germany' in str(affil):
                country_list.append('Germany')
            elif 'Thailand' in str(affil):
                country_list.append('Thailand')
            # Add more countries as needed

        country_counts = Counter(country_list)
        top_countries = pd.DataFrame(
            country_counts.most_common(top_n),
            columns=['Country', 'Documents']
        )

        print(f"\n{'='*60}")
        print(f"TOP {top_n} COUNTRIES BY PRODUCTION")
        print(f"{'='*60}")
        print(top_countries.to_string(index=False))

        # Visualization
        plt.figure(figsize=(10, 6))
        plt.barh(range(len(top_countries)), top_countries['Documents'].values[::-1],
                color='green', alpha=0.7)
        plt.yticks(range(len(top_countries)), top_countries['Country'].values[::-1])
        plt.xlabel('Number of Documents')
        plt.title('Country Scientific Production', fontweight='bold')
        plt.tight_layout()
        plt.savefig('output_countries.png', dpi=300, bbox_inches='tight')
        print("\n✓ Saved: output_countries.png")
        plt.show()

        self.results['top_countries'] = top_countries
        return top_countries

    # ================================================================
    # SECTION 9: EXPORT RESULTS
    # ================================================================

    def export_results(self, output_dir='outputs'):
        """Export all results to Excel"""
        import os
        os.makedirs(output_dir, exist_ok=True)

        with pd.ExcelWriter(f'{output_dir}/bibliometric_results.xlsx') as writer:
            # Statistics
            if 'statistics' in self.results:
                pd.DataFrame(list(self.results['statistics'].items()),
                           columns=['Metric', 'Value']).to_excel(
                    writer, sheet_name='Statistics', index=False)

            # Top cited
            if 'top_cited' in self.results:
                self.results['top_cited'].to_excel(
                    writer, sheet_name='Top_Cited', index=False)

            # Top authors
            if 'top_authors' in self.results:
                self.results['top_authors'].to_excel(
                    writer, sheet_name='Top_Authors', index=False)

            # Top sources
            if 'top_sources' in self.results:
                self.results['top_sources'].to_frame('Documents').to_excel(
                    writer, sheet_name='Top_Sources')

            # Top keywords
            if 'top_keywords' in self.results:
                self.results['top_keywords'].to_excel(
                    writer, sheet_name='Top_Keywords', index=False)

            # Top countries
            if 'top_countries' in self.results:
                self.results['top_countries'].to_excel(
                    writer, sheet_name='Top_Countries', index=False)

        print(f"\n✓ Results exported to: {output_dir}/bibliometric_results.xlsx")

    # ================================================================
    # SECTION 10: RUN COMPLETE ANALYSIS
    # ================================================================

    def run_complete_analysis(self):
        """Run all analyses"""
        print("\n" + "="*60)
        print("RUNNING COMPLETE BIBLIOMETRIC ANALYSIS")
        print("="*60)

        self.load_data()
        self.generate_statistics()
        self.analyze_trends()
        self.most_cited_papers()
        self.most_productive_authors()
        self.most_relevant_sources()
        self.keyword_analysis()
        self.country_analysis()
        self.export_results()

        print("\n" + "="*60)
        print("✓ ANALYSIS COMPLETE!")
        print("="*60)
        print("\nGenerated files:")
        print("  - output_annual_production.png")
        print("  - output_top_authors.png")
        print("  - output_bradfords_law.png")
        print("  - output_wordcloud.png")
        print("  - output_keywords_bar.png")
        print("  - output_countries.png")
        print("  - outputs/bibliometric_results.xlsx")
        print("\nResults stored in self.results dictionary")


# ==============================================================================
# EXAMPLE USAGE
# ==============================================================================

if __name__ == "__main__":

    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║  PYTHON BIBLIOMETRIC ANALYSIS                            ║
    ║  Author: Mahbub Hassan | Chulalongkorn University        ║
    ╚══════════════════════════════════════════════════════════╝
    """)

    # Example 1: Web of Science data
    # analysis = BibliometricAnalysis(
    #     data_path='examples/sample_data/sample_wos_transport.txt',
    #     data_type='wos'
    # )

    # Example 2: Scopus data
    analysis = BibliometricAnalysis(
        data_path='examples/sample_data/sample_scopus_transport.csv',
        data_type='scopus'
    )

    # Run complete analysis
    analysis.run_complete_analysis()

    # Access specific results
    # print(analysis.results['statistics'])
    # print(analysis.results['top_keywords'])

    print("\n🎉 Analysis complete! Check the output files.")
