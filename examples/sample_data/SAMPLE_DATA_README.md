# Sample Bibliographic Data

**Purpose:** Practice datasets for learning bibliometric analysis

---

## 📁 Files Included

### 1. sample_wos_transport.txt
**Format:** Web of Science (WoS) Plain Text
**Records:** 3 sample articles
**Topic:** Transportation Engineering & Sustainability
**Use:** Practice importing WoS data into Biblioshiny

**How to Use:**
```r
# In Biblioshiny
# 1. Data > Load Data
# 2. Select "Web of Science (PlainText .txt)"
# 3. Upload this file
# 4. Click Convert
```

### 2. sample_scopus_transport.csv
**Format:** Scopus CSV Export
**Records:** 6 sample articles
**Topic:** Transportation Engineering & Urban Planning
**Use:** Practice importing Scopus data into Biblioshiny

**How to Use:**
```r
# In Biblioshiny
# 1. Data > Load Data
# 2. Select "Scopus (.csv)"
# 3. Upload this file
# 4. Click Convert
```

---

## 📊 Dataset Characteristics

### Sample Papers Cover:
- Electric vehicle adoption
- Autonomous vehicles
- Public transport optimization
- Bicycle sharing systems
- Traffic flow prediction using ML
- Climate change and infrastructure

### Citation Network:
- Papers cite each other
- Realistic reference patterns
- Different publication years (2023-2024)
- Various journals

### Author Diversity:
- Multiple countries (China, USA, Thailand, etc.)
- Different institutions
- Co-authorship patterns
- Correspondence authors

---

## 🎯 Learning Exercises

### Exercise 1: Basic Statistics
1. Import data into Biblioshiny
2. Generate main information table
3. Create annual production plot
4. Identify most cited papers

**Expected Results:**
- 3 documents (WoS) or 6 documents (Scopus)
- Publication years: 2023-2024
- Citation counts: 18-85
- Multiple countries

### Exercise 2: Author Analysis
1. Generate author productivity
2. Create author co-citation network
3. Identify corresponding authors
4. Analyze h-index

**What to Look For:**
- Different collaboration patterns
- Single-author vs multi-author papers
- International collaborations

### Exercise 3: Keyword Analysis
1. Extract author keywords
2. Create keyword co-occurrence network
3. Identify trending topics
4. Generate word cloud

**Expected Keywords:**
- Electric vehicles
- Smart cities
- Machine learning
- Sustainability
- Urban planning

### Exercise 4: Journal Analysis
1. Identify source journals
2. Calculate journal impact
3. Analyze publication patterns
4. Generate Bradford's law plot

**Journals in Sample:**
- Transportation Research Part D
- Journal of Transport Geography
- Transportation Research Record
- Cities
- Transport Policy

### Exercise 5: VOSviewer Network
1. Export data for VOSviewer
2. Create co-authorship network
3. Build keyword co-occurrence
4. Generate citation network

---

## 🔍 Data Fields Explained

### Web of Science Fields:
```
PT = Publication Type (J = Journal)
AU = Authors (surname, initials)
AF = Author Full Names
TI = Title
SO = Source (journal name)
LA = Language
DT = Document Type
DE = Author Keywords
ID = Keywords Plus
AB = Abstract
C1 = Author Addresses
RP = Reprint Author
EM = Email Address
RI = ResearcherID
OI = ORCID
FU = Funding
CR = Cited References
NR = Number of References
TC = Times Cited
Z9 = Total Citations (WoS)
U1/U2 = Usage Counts
PY = Publication Year
VL = Volume
BP = Beginning Page
DI = DOI
```

### Scopus Fields:
```
Authors = Author names
Title = Article title
Year = Publication year
Source title = Journal name
Volume/Issue = Journal volume and issue
Page start/end = Page numbers
Cited by = Citation count
DOI = Digital Object Identifier
Abstract = Article abstract
Author Keywords = Keywords by authors
Index Keywords = Indexed keywords
References = Cited references
Correspondence Address = Corresponding author
```

---

## 💡 Tips for Practice

### Best Practices:
1. **Start Small:** Use these samples before real data
2. **Compare Formats:** Try both WoS and Scopus
3. **Check Data Quality:** Look for missing fields
4. **Validate Results:** Numbers should match documentation
5. **Export Results:** Save tables and figures

### Common Issues:
❌ **Wrong file format selected** → Use correct importer
❌ **Encoding errors** → Use UTF-8 encoding
❌ **Missing data** → Some fields may be empty
❌ **Citation mismatch** → Normal in sample data

### Advanced Practice:
1. **Merge Datasets:** Combine WoS + Scopus
2. **Custom Queries:** Filter by year/author
3. **Network Analysis:** Export to VOSviewer
4. **Time Trends:** Analyze temporal patterns
5. **Collaboration:** Study author networks

---

## 📝 Real Data Collection

When ready for real analysis:

### Web of Science:
1. Go to https://www.webofscience.com
2. Design your search query
3. Select results (max 500-1000 per export)
4. Export as "Plain Text" with "Full Record and Cited References"
5. Save as .txt file

### Scopus:
1. Go to https://www.scopus.com
2. Perform your search
3. Select all results
4. Export > CSV Export
5. Select "Citation information" and "Bibliographic information"
6. Download file

### Quality Checks:
✅ All records have DOI
✅ Author names consistent
✅ Abstracts included
✅ References complete
✅ Keywords present

---

## 🚀 Next Steps

After practicing with sample data:

1. **Collect Real Data:** Use your research topic
2. **Larger Dataset:** Aim for 200-500 papers
3. **Multiple Sources:** Combine databases if possible
4. **Clean Data:** Remove duplicates and errors
5. **Run Full Analysis:** Use all Biblioshiny features
6. **Create Visualizations:** Generate publication-quality figures
7. **Write Paper:** Use results in your manuscript

---

## 📧 Need Help?

**Questions about the sample data?**
- Check course modules for detailed guides
- Review R script templates
- Consult Biblioshiny documentation

**Ready for real analysis?**
- Follow Module 2: Data Collection
- Use search query templates
- Review data quality guidelines

---

## 📚 Related Files

- **R Template:** `templates/biblioshiny_scripts/complete_analysis_template.R`
- **Cheat Sheet:** `resources/cheat_sheets/biblioshiny_quick_reference.md`
- **Course:** `index.html` → Module 3: R Biblioshiny Analysis

---

*Sample data created for educational purposes*
*Based on realistic transportation engineering research*
*Mahbub Hassan | Chulalongkorn University*
