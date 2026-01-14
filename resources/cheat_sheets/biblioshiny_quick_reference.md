# 📚 Biblioshiny Quick Reference Cheat Sheet

## Essential Commands

### Setup & Launch
```r
# Install package (once)
install.packages("bibliometrix")

# Load library
library(bibliometrix)

# Launch Biblioshiny interface
biblioshiny()

# Launch on specific port
biblioshiny(port = 8080)
```

### Data Import
```r
# Web of Science (single file)
M <- convert2df("data.txt", dbsource = "wos", format = "plaintext")

# Web of Science (multiple files)
files <- c("file1.txt", "file2.txt", "file3.txt")
M <- convert2df(files, dbsource = "wos", format = "plaintext")

# Scopus
M <- convert2df("data.csv", dbsource = "scopus", format = "csv")

# PubMed
M <- convert2df("data.txt", dbsource = "pubmed", format = "pubmed")
```

### Basic Analysis
```r
# Perform bibliometric analysis
results <- biblioAnalysis(M, sep = ";")

# Summary statistics
summary(results, k = 10, pause = FALSE)

# Plot results
plot(results, k = 10, pause = FALSE)
```

### Annual Production
```r
# Calculate annual growth rate
AGR <- annualGrowthRate(M)

# View growth rate
AGR
```

### Citation Analysis
```r
# Most cited papers
CR <- citations(M, field = "article", sep = ";")
CR$Cited[1:20]

# Most cited authors
CR <- citations(M, field = "author", sep = ";")
CR$Cited[1:20]

# Local citations
LCR <- localCitations(M, sep = ";")
LCR$Papers[1:20,]
```

### Author Analysis
```r
# Author productivity over time
AU <- authorProdOverTime(M, k = 10, graph = TRUE)

# Author h-index
Hindex <- Hindex(M, field = "author", sep = ";", years = 50)
Hindex$H
```

### Country Analysis
```r
# Extract country metadata
M <- metaTagExtraction(M, Field = "AU_CO", sep = ";")

# Country analysis
results <- biblioAnalysis(M, sep = ";")
results$Countries
```

### Keyword Analysis
```r
# Keyword growth
topKW <- KeywordGrowth(M, Tag = "DE", sep = ";", top = 10, cdf = TRUE)

# Plot keyword trends
plot(topKW)
```

### Network Analysis
```r
# Co-occurrence network (keywords)
NetMatrix <- biblioNetwork(M, analysis = "co-occurrences", 
                           network = "keywords", sep = ";")

# Co-citation network
NetMatrix <- biblioNetwork(M, analysis = "co-citation", 
                           network = "references", sep = ";")

# Bibliographic coupling
NetMatrix <- biblioNetwork(M, analysis = "coupling", 
                           network = "references", sep = ";")

# Author collaboration
NetMatrix <- biblioNetwork(M, analysis = "collaboration", 
                           network = "authors", sep = ";")

# Country collaboration
NetMatrix <- biblioNetwork(M, analysis = "collaboration", 
                           network = "countries", sep = ";")
```

### Network Visualization
```r
# Plot network
net <- networkPlot(NetMatrix, 
                  normalize = "association",  # or "jaccard", "salton"
                  n = 50,                      # number of nodes
                  Title = "Network Title",
                  type = "fruchterman",        # or "circle", "kamada"
                  size = TRUE,                 # node size by frequency
                  remove.multiple = FALSE,
                  labelsize = 0.7,
                  cluster = "walktrap",        # or "louvain", "optimal"
                  community.repulsion = 0.1)

# Access network metrics
net$nodeDegree    # Node centrality
net$cluster_res   # Cluster membership
```

### Thematic Analysis
```r
# Thematic map
Map <- thematicMap(M, field = "DE", n = 250, minfreq = 5,
                  stemming = FALSE, size = 0.7, n.labels = 4)
plot(Map$map)

# Conceptual structure (MCA)
CS <- conceptualStructure(M, field = "DE", method = "MCA",
                         minDegree = 5, clust = 5,
                         stemming = FALSE, labelsize = 8,
                         documents = 20)
```

### Thematic Evolution
```r
# Define time periods
years <- c(2013, 2017, 2020, 2023)

# Evolution analysis
nexus <- thematicEvolution(M, field = "DE", years = years,
                          n = 100, minFreq = 2)

# Plot evolution
plotThematicEvolution(nexus$Nodes, nexus$Edges)
```

### Historical Analysis
```r
# Historiograph (citation network)
histResults <- histNetwork(M, min.citations = 10, sep = ";")
histPlot(histResults, n = 20, size = 5, labelsize = 4)
```

### Advanced Visualizations
```r
# Three fields plot (Sankey diagram)
threeFieldsPlot(M, fields = c("AU", "DE", "SO"), n = c(15, 15, 15))

# Trending topics
topicTrends <- fieldByYear(M, field = "DE", 
                          timespan = c(2013:2023),
                          min.freq = 3, n.items = 5, 
                          graph = TRUE)
```

### Data Export
```r
# Save as CSV
write.csv(M, "bibliometric_data.csv", row.names = FALSE)

# Save specific results
write.csv(results$Authors, "top_authors.csv")
write.csv(results$Sources, "top_journals.csv")

# Save plots
png("plot.png", width = 1200, height = 800, res = 150)
plot(results, k = 10)
dev.off()

# Save workspace
save.image("analysis.RData")

# Load workspace
load("analysis.RData")
```

## Common Parameters

### Network Types
- `"keywords"` - Keyword co-occurrence
- `"authors"` - Author collaboration
- `"references"` - Citation analysis
- `"countries"` - Country collaboration
- `"sources"` - Journal collaboration

### Analysis Types
- `"co-occurrences"` - Co-occurrence network
- `"co-citation"` - Co-citation network
- `"coupling"` - Bibliographic coupling
- `"collaboration"` - Collaboration network

### Layout Algorithms
- `"fruchterman"` - Force-directed (default, best for most)
- `"kamada"` - Kamada-Kawai
- `"circle"` - Circular layout
- `"auto"` - Automatic selection

### Clustering Algorithms
- `"walktrap"` - Community detection (recommended)
- `"louvain"` - Louvain method
- `"optimal"` - Optimal modularity
- `"edge.betweenness"` - Edge betweenness

### Normalization Methods
- `"association"` - Association strength (recommended)
- `"jaccard"` - Jaccard index
- `"salton"` - Salton index
- `"inclusion"` - Inclusion index

## Troubleshooting

### Issue: Package installation fails
```r
# Try installing dependencies first
install.packages(c("dplyr", "ggplot2", "igraph", "FactoMineR"))
# Then retry bibliometrix
install.packages("bibliometrix")
```

### Issue: Biblioshiny won't launch
```r
# Try different port
biblioshiny(port = 8888)

# Check if package is loaded
library(bibliometrix)
```

### Issue: Data import error
```r
# Check file format
# WoS: Must be plain text with full record + cited references
# Scopus: Must be CSV with all fields

# Check file path
file.exists("your_file.txt")  # Should return TRUE

# Try with full path
M <- convert2df("C:/Users/YourName/Documents/data.txt", 
               dbsource = "wos", format = "plaintext")
```

### Issue: Empty or missing fields
```r
# Check if field exists
"DE" %in% names(M)  # Check for author keywords
"ID" %in% names(M)  # Check for Keywords Plus

# View field names
names(M)

# Check for missing values
sum(is.na(M$DE))
```

### Issue: Network plot is cluttered
```r
# Reduce number of nodes
net <- networkPlot(NetMatrix, n = 30)  # Instead of 50

# Increase minimum frequency
NetMatrix <- biblioNetwork(M, analysis = "co-occurrences",
                           network = "keywords", sep = ";",
                           n = 30)  # Only top 30 keywords

# Adjust label size
net <- networkPlot(NetMatrix, labelsize = 0.5)  # Smaller labels
```

## Tips & Best Practices

### Data Quality
✅ Always use "Full Record and Cited References" when exporting
✅ Check for duplicate records: `M <- M[!duplicated(M$SR),]`
✅ Verify time span: `range(M$PY, na.rm=TRUE)`
✅ Check author names: `M$AU[1:10]`

### Analysis Strategy
1. Start with descriptive statistics
2. Identify most cited papers and authors
3. Analyze temporal trends
4. Create keyword networks
5. Perform thematic analysis
6. Generate visualizations

### Visualization Guidelines
- Use high resolution for publications: `res = 300`
- Save as PNG for presentations, PDF for papers
- Consistent color schemes across figures
- Clear, readable labels (`labelsize = 0.7-1.0`)
- Include titles and legends

### Performance Optimization
- Filter large datasets: `M <- M[M$PY >= 2010,]`
- Limit network size: `n = 30-50` nodes
- Use `normalize = "association"` for better clusters
- Save intermediate results to avoid reprocessing

## Field Codes Reference

| Code | Description |
|------|-------------|
| AU   | Authors |
| TI   | Title |
| SO   | Source (Journal) |
| PY   | Publication Year |
| AB   | Abstract |
| DE   | Author Keywords |
| ID   | Keywords Plus (WoS) |
| CR   | Cited References |
| TC   | Times Cited |
| DI   | DOI |
| SR   | Short Reference |
| AU_CO | Authors' Countries |
| AU1_CO | First Author's Country |

## Resources

- 📖 Official Documentation: https://www.bibliometrix.org
- 📚 Package Manual: https://cran.r-project.org/web/packages/bibliometrix/
- 🎥 Video Tutorials: https://www.bibliometrix.org/tutorials.html
- 💬 Support Forum: https://github.com/massimoaria/bibliometrix/issues

---

**Created by Mahbub Hassan | Chulalongkorn University**
