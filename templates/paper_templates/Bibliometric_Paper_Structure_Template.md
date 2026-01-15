# Bibliometric Paper Structure Template
## Complete Manuscript Template for Q1 Journals

**Author:** Mahbub Hassan | Chulalongkorn University
**For:** Transportation Research, Cities, Journal of Cleaner Production, etc.
**Word Count Target:** 6000-8000 words

---

## 📋 Title Suggestions

**Format:** [Topic] + [Method] + [Scope]

**Examples:**
1. "Electric Vehicle Adoption in Smart Cities: A Bibliometric Analysis of Research Trends and Future Directions (2015-2024)"
2. "Mapping the Knowledge Structure of Sustainable Transportation: A Scientometric Review"
3. "Global Research on Autonomous Vehicles: Bibliometric Patterns, Collaboration Networks, and Emerging Themes"

**Title Checklist:**
- ✅ Includes main topic
- ✅ Mentions "bibliometric" or "scientometric"
- ✅ Specifies time period
- ✅ <20 words
- ✅ Specific and informative

---

## 📄 Abstract (250-300 words)

### Template Structure:

**[Background - 2-3 sentences]**
> "[Topic] has gained significant attention in recent years. However, a comprehensive understanding of the research landscape, knowledge structure, and emerging trends remains limited. This study addresses this gap through systematic bibliometric analysis."

**[Objectives - 1-2 sentences]**
> "This research aims to: (1) map the intellectual structure of [topic] research, (2) identify key themes and evolution patterns, (3) analyze collaboration networks, and (4) reveal emerging research frontiers."

**[Methods - 2-3 sentences]**
> "We retrieved [X] publications from the Web of Science Core Collection spanning [Year]-[Year]. Bibliometric analysis was conducted using R Biblioshiny and VOSviewer, examining publication trends, citation patterns, keyword co-occurrence, co-citation relationships, and collaboration networks."

**[Results - 3-4 sentences]**
> "Results reveal: (1) exponential growth in publications (CAGR: X%), (2) [Country/Institution] as leading contributors, (3) five major research clusters including [theme 1], [theme 2], and [theme 3], and (4) recent shift from [old focus] to [new focus]. The most influential works focus on [key findings]. Collaboration analysis shows strong international partnerships, particularly between [countries/regions]."

**[Conclusions - 1-2 sentences]**
> "This study provides a comprehensive map of [topic] research, identifying research gaps and future directions. Findings benefit researchers, policymakers, and practitioners in understanding the evolution and trajectory of this critical field."

**Keywords:** 5-7 keywords (bibliometric analysis; [topic]; research trends; knowledge mapping; scientometrics; [specific terms])

---

## 1. Introduction (1200-1500 words)

### 1.1 Background and Context (300-400 words)

**Structure:**
```
¶1 - Importance of the topic
¶2 - Growth and significance
¶3 - Current challenges/gaps
¶4 - Need for systematic review
```

**Example Opening:**
> "The global transition toward sustainable transportation has positioned electric vehicles (EVs) as a critical solution to reduce greenhouse gas emissions and dependence on fossil fuels (IEA, 2023). Over the past decade, EV research has experienced remarkable growth, with publications increasing from approximately 500 papers in 2015 to over 5,000 in 2024 (preliminary count). This explosive growth reflects rising academic and industry interest driven by technological advances, supportive policies, and increasing environmental awareness."

### 1.2 Problem Statement (200-250 words)

**Key Elements:**
- Despite growth, knowledge is fragmented
- Lack of systematic overview
- Unclear research evolution
- Unknown collaboration patterns
- Need to identify gaps

**Example:**
> "Despite this proliferation of research, the field lacks a comprehensive, systematic analysis of its knowledge structure and evolution. Existing reviews focus on specific aspects [cite], but none have systematically mapped the entire research landscape, identified key knowledge clusters, traced thematic evolution, or analyzed global collaboration patterns. This gap hinders researchers from understanding the field's development trajectory and identifying promising future directions."

### 1.3 Research Questions (100-150 words)

**Format:**
1. **RQ1:** What are the publication and citation trends in [topic] research?
2. **RQ2:** Who are the most influential authors, institutions, and countries?
3. **RQ3:** What are the major research themes and their evolution over time?
4. **RQ4:** What is the intellectual structure of the field (co-citation patterns)?
5. **RQ5:** How do collaboration networks function across authors, institutions, and countries?
6. **RQ6:** What are the emerging research frontiers and future directions?

### 1.4 Research Objectives (100-150 words)

**List format:**
This study aims to:
1. Analyze publication trends and identify growth patterns
2. Identify most influential contributors (authors, journals, institutions, countries)
3. Map the knowledge structure through co-citation analysis
4. Reveal thematic evolution and research hotspots
5. Examine collaboration networks and international partnerships
6. Identify research gaps and propose future research directions

### 1.5 Significance and Contributions (200-250 words)

**What makes your study unique?**
- First comprehensive bibliometric analysis of [topic]
- Largest dataset analyzed (X publications)
- Latest data (up to 2024)
- Multiple complementary methods
- Actionable insights for stakeholders

**Example:**
> "This research makes several significant contributions. First, it provides the first comprehensive bibliometric analysis of [topic], analyzing over [X] publications—the most extensive dataset to date. Second, it employs multiple complementary methods (performance analysis, science mapping, network analysis) to provide a holistic view. Third, it reveals temporal evolution, showing how research focus has shifted over time. Fourth, it identifies specific research gaps and proposes concrete future directions. Finally, findings benefit multiple stakeholders: researchers gain guidance for future studies, funding agencies understand research priorities, and practitioners access evidence-based insights."

### 1.6 Paper Structure (100 words)

> "The remainder of this paper is organized as follows. Section 2 describes the bibliometric methodology and data collection process. Section 3 presents results organized by research questions. Section 4 discusses key findings, implications, and limitations. Section 5 concludes with research gaps and future directions."

---

## 2. Methodology (1500-2000 words)

### 2.1 Research Design (200-250 words)

**Include:**
- Type of review (systematic bibliometric)
- Framework used (if any)
- Overall approach
- Flowchart reference

**Example:**
> "This study employs systematic bibliometric analysis to map the knowledge landscape of [topic] research. Bibliometric methods quantitatively analyze large volumes of scientific literature to reveal patterns, trends, and structures (Donthu et al., 2021). We follow a structured framework combining performance analysis (productivity, citations) and science mapping (co-citation, co-occurrence, collaboration networks) (Cobo et al., 2011). Figure 1 presents the research framework and workflow."

**[Insert PRISMA-style flowchart here]**

### 2.2 Data Source and Collection (400-500 words)

#### 2.2.1 Database Selection

**Justify choice:**
> "We selected the Web of Science (WoS) Core Collection as the primary data source for several reasons: (1) high-quality, peer-reviewed content with rigorous selection criteria, (2) comprehensive citation indexing enabling co-citation analysis, (3) complete bibliographic metadata (authors, affiliations, references), (4) broad coverage of multidisciplinary research, and (5) wide acceptance in bibliometric studies (Pranckutė, 2021). While Scopus offers broader coverage, WoS ensures higher data quality and consistency for scientometric analysis."

#### 2.2.2 Search Strategy

**Document your exact query:**

```
Database: Web of Science Core Collection
Search Date: [Date]
Time Span: 2015-01-01 to 2024-12-31

Search Query:
TS=("electric vehicle*" OR "battery electric vehicle*" OR "BEV" OR "EV")
AND
TS=("adoption" OR "acceptance" OR "uptake" OR "diffusion" OR "consumer*")

Filters Applied:
- Document Types: Article, Review
- Languages: English
- Indexes: SCI-EXPANDED, SSCI, A&HCI

Results: X,XXX publications
```

**Search query development:**
- Pilot searches conducted
- Keywords refined iteratively
- Boolean operators optimized
- Verified with known key papers

#### 2.2.3 Inclusion/Exclusion Criteria

**Inclusion Criteria:**
1. Published in peer-reviewed journals
2. Written in English
3. Full-length articles or reviews
4. Published between 2015-2024
5. Relevant to [topic]

**Exclusion Criteria:**
1. Conference papers, book chapters
2. Editorials, letters, corrections
3. Non-English publications
4. Duplicate records
5. Off-topic content (manual screening)

#### 2.2.4 Data Retrieval

**Process:**
1. Execute search query
2. Export results (max 500 per batch for WoS)
3. Select: Full Record and Cited References
4. Format: Plain Text (.txt)
5. Merge multiple files if needed
6. Total records retrieved: [X,XXX]

### 2.3 Data Screening and Cleaning (300-350 words)

**Multi-stage process:**

**Stage 1: Automatic Screening**
- Remove duplicates: [X] removed
- Filter by document type: [X] removed
- Language filter: [X] removed
- Remaining: [X,XXX]

**Stage 2: Manual Screening**
- Two researchers independently reviewed titles/abstracts
- Cohen's Kappa inter-rater reliability: 0.XX
- Disagreements resolved through discussion
- Off-topic papers removed: [X]

**Final Dataset:** [X,XXX] publications

**Data Cleaning:**
- Author name standardization
- Institution name harmonization
- Journal name consistency
- Country assignment based on first author address
- Manual correction of obvious errors

**Example Table:**
| Stage | Records | Removed | Remaining |
|-------|---------|---------|-----------|
| Initial retrieval | X,XXX | - | X,XXX |
| Duplicate removal | X,XXX | XXX | X,XXX |
| Document type filter | X,XXX | XXX | X,XXX |
| Language filter | X,XXX | XX | X,XXX |
| Manual screening | X,XXX | XXX | **X,XXX** |

### 2.4 Analytical Tools and Methods (400-500 words)

#### 2.4.1 Software

**R with bibliometrix package (v4.1.4):**
- Performance analysis
- Descriptive statistics
- Trend analysis
- Thematic evolution
- Biblioshiny web interface for visualization

**VOSviewer (v1.6.20):**
- Network visualization
- Co-citation analysis
- Bibliographic coupling
- Co-authorship networks
- Keyword co-occurrence networks

#### 2.4.2 Analytical Techniques

**1. Performance Analysis**
- Publication trends (annual production)
- Citation analysis (most cited papers, authors, journals)
- H-index calculations
- Impact metrics (TC, TC/Year, CPP)

**2. Science Mapping**

**a) Co-citation Analysis**
- Identifies intellectual structure
- Shows which works are cited together
- Reveals foundational literature
- Threshold: Minimum X citations

**b) Bibliographic Coupling**
- Reveals current research fronts
- Papers citing similar references
- Shows contemporary themes
- Threshold: Minimum X citations

**c) Keyword Co-occurrence**
- Maps research topics
- Identifies thematic clusters
- Shows topic relationships
- Threshold: Minimum X occurrences

**d) Co-authorship Analysis**
- Author collaboration networks
- Institutional partnerships
- Country collaboration patterns
- Minimum X documents threshold

**3. Thematic Evolution**
- Tracks themes across time periods
- Sankey diagrams for theme flow
- Strategic diagrams (niche/motor/basic/emerging)

### 2.5 Quality Assurance (150-200 words)

**Reliability measures:**
1. **Reproducibility:** Documented search strategy
2. **Transparency:** All parameters reported
3. **Consistency:** Standardized procedures
4. **Validation:** Cross-checked with domain experts
5. **Triangulation:** Multiple methods used

**Limitations acknowledged:**
- WoS coverage limitations
- English-language bias
- Publication lag (2024 incomplete)
- Citation window effects

---

## 3. Results (2500-3000 words)

### 3.1 Descriptive Statistics (400-500 words)

**Table 1: Main Information About Data**

| Description | Results |
|------------|---------|
| Timespan | 2015-2024 |
| Documents | X,XXX |
| Sources (Journals, Books, etc.) | XXX |
| Keywords Plus (ID) | X,XXX |
| Author's Keywords (DE) | X,XXX |
| Authors | X,XXX |
| Author Appearances | XX,XXX |
| Authors of single-authored documents | XXX |
| Authors of multi-authored documents | X,XXX |
| Single-authored documents | XXX |
| Documents per Author | X.XX |
| Authors per Document | X.XX |
| Co-Authors per Documents | X.XX |
| Collaboration Index | X.XX |
| International co-authorships % | XX% |
| Document types | Article (XX%), Review (XX%) |
| Average citations per document | XX.X |
| Average citations per year per doc | X.XX |
| References | XXX,XXX |

**Key observations:**
- Total of X,XXX publications
- Average X.X authors per paper (high collaboration)
- XX% international co-authorship (strong global collaboration)
- Average XX citations per document

### 3.2 Publication and Citation Trends (300-400 words)

**Figure 1: Annual Scientific Production**
[Insert line graph: Years vs. Number of Publications]

**Analysis:**
- Clear upward trend: XX papers (2015) → XXX papers (2024)
- Compound Annual Growth Rate (CAGR): XX%
- Exponential/linear growth pattern
- Inflection points: 20XX (explain why)
- Slight decrease in 2024 (incomplete year)

**Figure 2: Average Citations per Year**
[Insert graph showing citation patterns]

**Observations:**
- Older papers (2015-2018) have higher total citations (citation window effect)
- Recent papers (2022-2024) show increasing citations per year
- Indicates growing field impact

### 3.3 Most Influential Contributors (600-700 words)

#### 3.3.1 Most Productive Authors

**Table 2: Top 15 Most Productive Authors**

| Rank | Author | h-index | g-index | m-index | Articles | TC | TC/Year |
|------|--------|---------|---------|---------|----------|----|---------|
| 1 | SMITH J | XX | XX | X.XX | XX | XXX | XX.X |
| 2 | LI X | XX | XX | X.XX | XX | XXX | XX.X |
| ... | ... | ... | ... | ... | ... | ... | ... |

**Key findings:**
- Smith J. most productive (XX articles)
- Li X. highest citations (XXX total)
- Core group of XX authors with 10+ papers
- Top 15 authors represent XX% of total publications

#### 3.3.2 Most Cited Papers

**Table 3: Top 10 Most Globally Cited Documents**

| Paper | TC | TC/Year | Journal | Year |
|-------|----|---------| --------|------|
| Author1 et al., 20XX, J Name | XXX | XX.X | Journal Name | 20XX |
| ... | ... | ... | ... | ... |

**Analysis:**
- Seminal paper: [Title] (XXX citations)
- Most papers from 2015-2018 (longer citation window)
- Review articles dominate top 10
- Thematic focus: [identify common themes]

#### 3.3.3 Most Relevant Sources

**Table 4: Most Relevant Journals (Bradford's Law)**

**Core Journals (Zone 1):**
| Journal | Articles | IF (2023) | TC |
|---------|----------|-----------|-----|
| Journal of Cleaner Production | XXX | X.XX | X,XXX |
| Energy Policy | XXX | X.XX | X,XXX |
| ... | ... | ... | ... |

**Analysis:**
- XX journals publish XX% of articles (Bradford's core)
- Multidisciplinary spread: energy, environment, transport, policy
- High-impact journals dominate

#### 3.3.4 Most Productive Countries

**Table 5: Top 15 Countries by Production**

| Country | Articles | SCP | MCP | MCP_Ratio | TC | TC/Article |
|---------|----------|-----|-----|-----------|----|-----------|
| USA | XXX | XXX | XXX | XX% | X,XXX | XX.X |
| China | XXX | XXX | XXX | XX% | X,XXX | XX.X |
| ... | ... | ... | ... | ... | ... | ... |

**Legend:**
- SCP = Single Country Publications
- MCP = Multiple Country Publications
- MCP_Ratio = International collaboration rate

**Key insights:**
- USA leads in production (XXX articles)
- China highest growth rate
- European countries strong collaboration (high MCP%)
- Asian countries increasing presence

**Figure 3: Country Collaboration Map**
[Insert world map or collaboration network]

### 3.4 Intellectual Structure - Co-Citation Analysis (500-600 words)

**Figure 4: Co-Citation Network of Cited References**
[Insert VOSviewer network visualization]

**Minimum citations threshold:** XX
**Total items:** XXX cited references
**Clusters identified:** X

**Cluster Analysis:**

**Cluster 1 (Red): [Theme Name] (n=XX papers)**
- Key papers: [Author, Year]; [Author, Year]
- Focus: [Brief description]
- Example: Technology development, battery advances

**Cluster 2 (Green): [Theme Name] (n=XX papers)**
- Key papers: [Author, Year]; [Author, Year]
- Focus: [Brief description]
- Example: Consumer behavior, adoption factors

**Cluster 3 (Blue): [Theme Name] (n=XX papers)**
- Key papers: [Author, Year]; [Author, Year]
- Focus: [Brief description]
- Example: Policy and incentives

**Cluster 4 (Yellow): [Theme Name] (n=XX papers)**
- Key papers: [Author, Year]; [Author, Year]
- Focus: [Brief description]
- Example: Infrastructure and charging

**[Additional clusters if applicable]**

**Interpretation:**
> "The co-citation network reveals the intellectual foundation of [topic] research. Cluster 1 represents the technological core, anchored by seminal works on [X]. Cluster 2 shows the behavioral science perspective, with strong connections to TAM and innovation diffusion theory. Clusters 3 and 4 represent policy and infrastructure dimensions. The close connection between Clusters 1 and 4 suggests technology-infrastructure interdependence. Cluster 2's relatively isolated position indicates distinct theoretical foundations."

### 3.5 Knowledge Structure - Keyword Analysis (500-600 words)

**Figure 5: Keyword Co-occurrence Network**
[Insert VOSviewer keyword network]

**Parameters:**
- Keywords: Author keywords
- Minimum occurrences: X
- Total keywords: XXX
- Clusters: X

**Cluster Description:**

**Cluster 1 (Red) - [Theme Name]:**
- Core keywords: keyword1, keyword2, keyword3
- Focus: [Description]
- Link strength: [Strong connections to...]

**Cluster 2 (Green) - [Theme Name]:**
- Core keywords: keyword1, keyword2, keyword3
- Focus: [Description]
- Emerging keywords: [new terms]

**[Continue for all clusters]**

**Temporal Evolution:**

**Figure 6: Keyword Overlay Visualization (Time-based)**
[Insert overlay visualization with color gradient]

**Blue keywords (2015-2018) - Foundational topics:**
- Early focus: [list keywords]
- Example: "range anxiety", "battery cost"

**Yellow/Red keywords (2022-2024) - Emerging topics:**
- Recent focus: [list keywords]
- Example: "vehicle-to-grid", "smart charging", "machine learning"

**Shift interpretation:**
> "The temporal analysis reveals a clear evolution from fundamental technology concerns (blue) to advanced applications and system integration (yellow/red). This shift indicates field maturation and broadening scope."

### 3.6 Thematic Evolution (300-400 words)

**Figure 7: Thematic Evolution (Sankey Diagram)**
[Insert Sankey diagram showing theme flow across time periods]

**Time periods:**
- Period 1: 2015-2017 (XX papers)
- Period 2: 2018-2020 (XXX papers)
- Period 3: 2021-2024 (X,XXX papers)

**Major themes and evolution:**

**Persistent themes** (stable across periods):
1. [Theme 1]: Battery technology
2. [Theme 2]: Consumer adoption

**Emerging themes** (new in recent period):
1. [Theme 1]: AI/ML applications
2. [Theme 2]: V2G integration

**Declining themes** (less prominent):
1. [Theme 1]: Early infrastructure concerns

**Interpretation:**
> "Thematic evolution shows field maturation. Core technical themes persist but expand in scope. New themes emerging around system integration, smart technologies, and sustainability indicate interdisciplinary expansion."

### 3.7 Collaboration Networks (400-500 words)

#### 3.7.1 Author Collaboration

**Figure 8: Co-authorship Network (Authors)**
[Insert network with key author clusters]

**Findings:**
- XX collaboration clusters identified
- Largest cluster: [Lead author] group (XX authors)
- Most connected author: [Author name] (XX collaborations)
- Average collaborators per author: X.X

#### 3.7.2 Institutional Collaboration

**Figure 9: Institutional Collaboration Network**

**Top collaborative institutions:**
1. MIT ↔ Stanford (XX joint publications)
2. Tsinghua ↔ UC Berkeley (XX joint publications)
3. [etc.]

**Interpretation:**
> "Strong ties between leading US and Chinese institutions drive global collaboration. European institutions form distinct but interconnected cluster."

#### 3.7.3 Country Collaboration

**Figure 10: Country Collaboration Network**

**Major partnerships:**
- USA-China: XXX collaborations
- USA-UK: XXX collaborations
- Germany-Netherlands: XXX collaborations

**Regional patterns:**
- North America-Europe corridor
- Asia-Pacific collaboration hub
- Limited Global South participation

---

## 4. Discussion (1500-1800 words)

### 4.1 Key Findings Summary (300-400 words)

**RQ1: Publication trends**
> "The field shows exponential growth (CAGR XX%), indicating increasing academic and practical interest. Growth accelerated post-2020, likely due to [policy changes, technology breakthroughs, climate urgency]."

**RQ2: Influential contributors**
> "[Countries/Authors/Institutions] lead the field. Dominance of [regions] reflects [R&D investment, policy support, industry presence]."

**RQ3: Research themes**
> "Five major themes identified: [list]. Evolution from technical focus to systems perspective."

**RQ4: Intellectual structure**
> "Co-citation analysis reveals interdisciplinary foundations drawing from engineering, behavioral science, economics, and policy studies."

**RQ5: Collaboration patterns**
> "Strong international collaboration (XX% of papers) with distinct regional clusters. North American-European-Asian triad dominates."

**RQ6: Emerging frontiers**
> "Recent shift toward AI/ML applications, smart grid integration, circular economy, and equity considerations."

### 4.2 Theoretical Contributions (300-400 words)

**1. Comprehensive knowledge map**
> "First systematic mapping of [topic] providing holistic view of field structure and evolution."

**2. Identification of research streams**
> "Reveals distinct but interconnected research streams, clarifying theoretical foundations and methodological approaches."

**3. Evolution trajectory**
> "Documents field maturation from narrow technical focus to broader socio-technical systems perspective."

**4. Research gaps identified**
> "Systematic identification of understudied areas provides roadmap for future research."

### 4.3 Practical Implications (300-400 words)

**For Researchers:**
- Identify high-impact journals for submission
- Find potential collaborators
- Discover research gaps
- Understand field evolution

**For Policymakers:**
- Evidence of research priorities
- Identification of knowledge clusters
- International collaboration patterns inform policy design
- Emerging themes guide future investments

**For Industry:**
- Technology trends identification
- Academic-industry collaboration opportunities
- R&D priority setting
- Competitive intelligence

**For Funding Agencies:**
- Research landscape overview
- Identify underfunded areas
- Support strategic collaboration
- Monitor research impact

### 4.4 Research Gaps and Future Directions (400-500 words)

**Gap 1: [Specific Gap]**
- **Current state:** [What's missing]
- **Why important:** [Significance]
- **Future direction:** [Specific research questions]

**Gap 2: [Specific Gap]**
- **Current state:** Limited focus on Global South contexts
- **Why important:** Different adoption patterns, infrastructure challenges
- **Future direction:** Comparative studies, context-specific models

**Gap 3: [Methodological Gaps]**
- **Current state:** Few longitudinal studies, limited real-world data
- **Why important:** Understand actual vs. stated behavior
- **Future direction:** Long-term panel studies, big data analytics

**Gap 4: [Interdisciplinary Gaps]**
- **Current state:** Limited integration of [disciplines]
- **Why important:** [Holistic understanding needed]
- **Future direction:** [Cross-disciplinary approaches]

**Emerging Research Frontiers:**
1. AI/ML for prediction and optimization
2. Circular economy and lifecycle assessment
3. Social equity and justice considerations
4. System integration (V2G, smart grids)
5. Behavioral interventions and nudging

### 4.5 Limitations (200-300 words)

**Data limitations:**
1. WoS coverage not exhaustive (missing some journals, conference papers)
2. English-language bias
3. Citation lag for recent publications
4. 2024 data incomplete

**Methodological limitations:**
1. Keyword-based search may miss relevant papers
2. Manual screening subject to researcher judgment
3. Bibliometric methods show patterns, not causation
4. Clustering algorithms sensitive to parameters

**Scope limitations:**
1. Focus on academic literature (excludes gray literature, industry reports)
2. Specific time period (2015-2024)
3. Single database (WoS)

**Mitigation strategies:**
- Comprehensive search strategy
- Multiple screening stages
- Sensitivity analyses
- Transparent reporting

> "Despite these limitations, the large sample size (X,XXX publications) and systematic approach provide robust insights into the research landscape."

---

## 5. Conclusion (400-500 words)

### 5.1 Summary (150-200 words)

> "This systematic bibliometric analysis mapped the knowledge landscape of [topic] research, analyzing X,XXX publications from 2015-2024. Results reveal exponential growth, strong international collaboration, and field maturation from technical foundations to socio-technical systems perspective. Five major research themes identified: [list]. Co-citation analysis revealed interdisciplinary intellectual structure. Collaboration networks showed [patterns]. Temporal evolution indicated shift from [old focus] to [new focus], with emerging research frontiers in [areas]."

### 5.2 Contributions (100-150 words)

> "This study makes several contributions: (1) comprehensive knowledge map guiding future research, (2) identification of influential works and contributors, (3) revelation of research gaps and opportunities, (4) documentation of field evolution, and (5) practical insights for multiple stakeholders. The synthesis of performance analysis and science mapping provides holistic understanding unavailable from individual studies."

### 5.3 Future Research Agenda (100-150 words)

**Immediate priorities:**
1. [Specific research direction 1]
2. [Specific research direction 2]
3. [Specific research direction 3]

**Long-term directions:**
- Interdisciplinary integration
- Global South perspectives
- Real-world validation
- Systemic approaches

> "Future research should address identified gaps while building on established knowledge foundations. Interdisciplinary collaboration will be crucial for tackling complex socio-technical challenges."

### 5.4 Closing Statement (50-100 words)

> "As [topic] continues evolving rapidly, periodic bibliometric updates will track emerging trends and shifting paradigms. This foundational analysis provides benchmark for future assessments. The systematic approach demonstrated here can be adapted to other research domains, contributing to evidence-based science policy and research management."

---

## References

**Format:** Journal style (APA, Chicago, etc.)

**Organize alphabetically**

**Example entries:**

Aria, M., & Cuccurullo, C. (2017). bibliometrix: An R-tool for comprehensive science mapping analysis. *Journal of Informetrics, 11*(4), 959-975.

Cobo, M. J., López-Herrera, A. G., Herrera-Viedma, E., & Herrera, F. (2011). Science mapping software tools: Review, analysis, and cooperative study among tools. *Journal of the American Society for Information Science and Technology, 62*(7), 1382-1402.

Donthu, N., Kumar, S., Mukherjee, D., Pandey, N., & Lim, W. M. (2021). How to conduct a bibliometric analysis: An overview and guidelines. *Journal of Business Research, 133*, 285-296.

---

## Appendices (Optional)

### Appendix A: Complete Search Strings

### Appendix B: Data Screening Flowchart (PRISMA)

### Appendix C: Additional Tables
- Extended author lists
- Journal rankings
- Country statistics

### Appendix D: Supplementary Figures
- Additional networks
- Sensitivity analyses

---

## Checklist Before Submission

**Content:**
- [ ] All research questions answered
- [ ] All tables/figures referenced in text
- [ ] Consistent terminology throughout
- [ ] Clear, logical flow
- [ ] No orphan headings
- [ ] Proper citations

**Methods:**
- [ ] Search strategy fully documented
- [ ] Inclusion/exclusion criteria clear
- [ ] Data collection process described
- [ ] Software versions reported
- [ ] Parameters/thresholds justified
- [ ] Limitations acknowledged

**Results:**
- [ ] Tables properly formatted
- [ ] Figures high quality (300 DPI+)
- [ ] Captions complete and informative
- [ ] Numbers cross-checked
- [ ] Consistency across sections

**Discussion:**
- [ ] Links to results
- [ ] Theoretical contributions clear
- [ ] Practical implications specific
- [ ] Future directions concrete
- [ ] Limitations honest

**Format:**
- [ ] Journal guidelines followed
- [ ] Word count within limits
- [ ] Reference style correct
- [ ] Supplementary materials prepared
- [ ] Conflict of interest statement
- [ ] Author contributions stated
- [ ] Acknowledgments included
- [ ] Funding disclosed

---

*Template created by Mahbub Hassan*
*Chulalongkorn University*
*Part of Complete Bibliometric Analysis Guide*
*Adapted from multiple Q1 publications in transportation, sustainability, and policy journals*
