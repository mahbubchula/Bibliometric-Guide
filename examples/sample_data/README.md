# Sample Datasets

This folder contains example bibliometric data for practice and learning.

## Available Datasets

### 1. Sample Web of Science Data
**File:** `sample_wos.txt` (to be added)
- **Topic:** Transportation Engineering
- **Records:** ~100 papers
- **Format:** Plain text (.txt)
- **Time span:** 2015-2023
- **Use case:** Practice data import and basic analysis

### 2. Sample Scopus Data
**File:** `sample_scopus.csv` (to be added)
- **Topic:** Sustainable Mobility
- **Records:** ~100 papers
- **Format:** CSV
- **Time span:** 2015-2023
- **Use case:** Compare WoS vs Scopus formats

## How to Use

### For Biblioshiny:
```r
library(bibliometrix)

# Load Web of Science data
M <- convert2df("examples/sample_data/sample_wos.txt", 
                dbsource = "wos", 
                format = "plaintext")

# Or load Scopus data
M <- convert2df("examples/sample_data/sample_scopus.csv",
                dbsource = "scopus",
                format = "csv")

# Run analysis
results <- biblioAnalysis(M)
summary(results, k=10)
```

### For VOSviewer:
1. Open VOSviewer
2. Create → Create map based on bibliographic data
3. Read data from bibliographic database files
4. Select the sample file
5. Follow the wizard

## Adding Your Own Data

To add your own sample datasets:
1. Ensure you have rights to share the data
2. Anonymize if necessary
3. Add a descriptive name
4. Update this README with:
   - File name
   - Topic/field
   - Number of records
   - Time span
   - Any special notes

## Data Sources

Sample data collected from:
- Web of Science (Clarivate)
- Scopus (Elsevier)
- Public domain sources

**Note:** All data used for educational purposes only.

## Need More Data?

Check these public repositories:
- [OpenAlex](https://openalex.org/)
- [Semantic Scholar](https://www.semanticscholar.org/)
- [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/)
- [arXiv](https://arxiv.org/)

---

**Questions?** Contact: mahbub.hassan@ieee.org
