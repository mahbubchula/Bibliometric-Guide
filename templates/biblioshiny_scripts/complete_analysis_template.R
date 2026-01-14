################################################################################
# Complete Bibliometric Analysis Template - R Biblioshiny
# Author: Mahbub Hassan
# Master's Student, Civil Engineering (Transportation)
# Chulalongkorn University, Bangkok, Thailand
# Contact: mahbub.hassan@ieee.org
################################################################################

# ============================================================================
# SECTION 1: SETUP AND DATA LOADING
# ============================================================================

# Install packages (run once)
# install.packages("bibliometrix")
# install.packages("tidyverse")
# install.packages("ggplot2")

# Load libraries
library(bibliometrix)
library(tidyverse)
library(ggplot2)

# Set working directory
setwd("path/to/your/project")

# Create output directories
dir.create("outputs", showWarnings = FALSE)
dir.create("outputs/plots", showWarnings = FALSE)
dir.create("outputs/tables", showWarnings = FALSE)
dir.create("outputs/networks", showWarnings = FALSE)

# ============================================================================
# SECTION 2: DATA IMPORT AND CONVERSION
# ============================================================================

## Option A: Web of Science Data
# For single file
file <- "data/wos_data.txt"
M <- convert2df(file, dbsource = "wos", format = "plaintext")

# For multiple files
# files <- c("data/wos_001.txt", "data/wos_002.txt", "data/wos_003.txt")
# M <- convert2df(files, dbsource = "wos", format = "plaintext")

## Option B: Scopus Data
# file <- "data/scopus_data.csv"
# M <- convert2df(file, dbsource = "scopus", format = "csv")

# View dataset structure
View(M)
str(M)

# Basic info
cat("Number of documents:", nrow(M), "\n")
cat("Number of fields:", ncol(M), "\n")
cat("Time span:", min(M$PY, na.rm=TRUE), "-", max(M$PY, na.rm=TRUE), "\n")

# ============================================================================
# SECTION 3: DESCRIPTIVE ANALYSIS
# ============================================================================

# Perform bibliometric analysis
results <- biblioAnalysis(M, sep = ";")

# Generate summary statistics
summary_stats <- summary(results, k = 10, pause = FALSE)

# Save summary to file
sink("outputs/tables/summary_statistics.txt")
summary(results, k = 20, pause = FALSE)
sink()

# Extract main information
main_info <- results$MainInformationDF
write.csv(main_info, "outputs/tables/main_information.csv", row.names = FALSE)

# ============================================================================
# SECTION 4: ANNUAL SCIENTIFIC PRODUCTION
# ============================================================================

# Calculate annual production
annual_production <- table(M$PY)
annual_df <- data.frame(
  Year = as.numeric(names(annual_production)),
  Articles = as.numeric(annual_production)
)

# Save data
write.csv(annual_df, "outputs/tables/annual_production.csv", row.names = FALSE)

# Create plot
png("outputs/plots/annual_production.png", width = 1200, height = 800, res = 150)
ggplot(annual_df, aes(x = Year, y = Articles)) +
  geom_line(color = "#FF1493", size = 1.5) +
  geom_point(color = "#4B0082", size = 3) +
  theme_minimal() +
  labs(
    title = "Annual Scientific Production",
    x = "Year",
    y = "Number of Articles"
  ) +
  theme(
    plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
    axis.title = element_text(size = 12, face = "bold")
  )
dev.off()

# Calculate growth rate
AGR <- annualGrowthRate(M)
write.csv(AGR, "outputs/tables/annual_growth_rate.csv")

# ============================================================================
# SECTION 5: MOST CITED PAPERS
# ============================================================================

# Most cited papers (global citations)
CR <- citations(M, field = "article", sep = ";")
most_cited <- CR$Cited[1:20]
write.csv(most_cited, "outputs/tables/most_cited_papers.csv")

# Most cited first authors
CR_authors <- citations(M, field = "author", sep = ";")
most_cited_authors <- CR_authors$Cited[1:20]
write.csv(most_cited_authors, "outputs/tables/most_cited_authors.csv")

# Local citations (within dataset)
LCR <- localCitations(M, sep = ";")
local_cited <- LCR$Papers[1:20,]
write.csv(local_cited, "outputs/tables/local_most_cited.csv")

# ============================================================================
# SECTION 6: MOST PRODUCTIVE AUTHORS
# ============================================================================

# Top authors by number of publications
top_authors <- results$Authors[1:20,]
write.csv(top_authors, "outputs/tables/top_authors.csv")

# Authors productivity over time
AU_prod <- authorProdOverTime(M, k = 10, graph = TRUE)

png("outputs/plots/author_productivity_overtime.png", width = 1400, height = 900, res = 150)
print(AU_prod$graph)
dev.off()

write.csv(AU_prod$dfAU, "outputs/tables/author_production_over_time.csv")

# Author h-index
Hindex <- Hindex(M, field = "author", sep = ";", years = 50)
write.csv(Hindex$H, "outputs/tables/author_hindex.csv")

# ============================================================================
# SECTION 7: MOST RELEVANT SOURCES (JOURNALS)
# ============================================================================

# Top journals
top_sources <- results$Sources[1:20,]
write.csv(top_sources, "outputs/tables/top_sources.csv")

# Source impact
source_impact <- sourceGrowth(M, top = 10, cdf = TRUE)
write.csv(source_impact, "outputs/tables/source_growth.csv")

# Source dynamics plot
png("outputs/plots/source_dynamics.png", width = 1400, height = 900, res = 150)
plot(source_impact, main = "Top Sources Production over Time")
dev.off()

# ============================================================================
# SECTION 8: COUNTRY ANALYSIS
# ============================================================================

# Extract country information
M <- metaTagExtraction(M, Field = "AU_CO", sep = ";")

# Most productive countries
country_prod <- biblioAnalysis(M, sep = ";")
top_countries <- country_prod$Countries[1:20,]
write.csv(top_countries, "outputs/tables/top_countries.csv")

# Country collaboration network
M_country <- biblioNetwork(M, analysis = "collaboration", 
                           network = "countries", sep = ";")

# Plot country collaboration
png("outputs/plots/country_collaboration.png", width = 1400, height = 1000, res = 150)
net_country <- networkPlot(M_country, n = 30, Title = "Country Collaboration Network",
                          type = "auto", size = TRUE, remove.multiple = FALSE,
                          labelsize = 0.8, cluster = "optimal")
dev.off()

# Save network data
write.csv(net_country$nodeDegree, "outputs/tables/country_network_metrics.csv")

# ============================================================================
# SECTION 9: KEYWORD ANALYSIS
# ============================================================================

# Most frequent keywords
top_keywords_author <- results$DE[1:30,]  # Author keywords
write.csv(top_keywords_author, "outputs/tables/top_keywords_author.csv")

if("ID" %in% names(results)) {
  top_keywords_plus <- results$ID[1:30,]  # Keywords Plus (WoS only)
  write.csv(top_keywords_plus, "outputs/tables/top_keywords_plus.csv")
}

# Keyword growth over time
topKW <- KeywordGrowth(M, Tag = "DE", sep = ";", top = 10, cdf = TRUE)
write.csv(topKW, "outputs/tables/keyword_growth.csv")

png("outputs/plots/keyword_growth.png", width = 1400, height = 900, res = 150)
plot(topKW, main = "Keyword Growth Over Time")
dev.off()

# ============================================================================
# SECTION 10: KEYWORD CO-OCCURRENCE NETWORK
# ============================================================================

# Create keyword co-occurrence network
NetMatrix <- biblioNetwork(M, analysis = "co-occurrences", 
                           network = "keywords", sep = ";")

# Plot keyword network
png("outputs/plots/keyword_cooccurrence.png", width = 1600, height = 1200, res = 150)
net_keywords <- networkPlot(NetMatrix, normalize = "association", 
                           n = 50, Title = "Keyword Co-occurrence Network",
                           type = "fruchterman", size = TRUE,
                           remove.multiple = FALSE, labelsize = 0.7,
                           cluster = "walktrap", community.repulsion = 0.1)
dev.off()

# Save network statistics
write.csv(net_keywords$nodeDegree, "outputs/tables/keyword_network_metrics.csv")
write.csv(net_keywords$cluster_res, "outputs/tables/keyword_clusters.csv")

# ============================================================================
# SECTION 11: CO-CITATION NETWORK
# ============================================================================

# Co-citation network (references cited together)
NetMatrix_cocit <- biblioNetwork(M, analysis = "co-citation", 
                                network = "references", sep = ";")

# Plot co-citation network
png("outputs/plots/cocitation_network.png", width = 1600, height = 1200, res = 150)
net_cocit <- networkPlot(NetMatrix_cocit, n = 30, 
                        Title = "Co-Citation Network",
                        type = "fruchterman", size = TRUE,
                        remove.multiple = FALSE, labelsize = 0.6,
                        cluster = "louvain")
dev.off()

write.csv(net_cocit$nodeDegree, "outputs/tables/cocitation_metrics.csv")

# ============================================================================
# SECTION 12: BIBLIOGRAPHIC COUPLING
# ============================================================================

# Bibliographic coupling (papers citing similar references)
NetMatrix_coupling <- biblioNetwork(M, analysis = "coupling", 
                                   network = "references", sep = ";")

# Plot coupling network
png("outputs/plots/coupling_network.png", width = 1600, height = 1200, res = 150)
net_coupling <- networkPlot(NetMatrix_coupling, n = 30,
                           Title = "Bibliographic Coupling Network",
                           type = "fruchterman", size = TRUE,
                           remove.multiple = FALSE, labelsize = 0.6)
dev.off()

write.csv(net_coupling$nodeDegree, "outputs/tables/coupling_metrics.csv")

# ============================================================================
# SECTION 13: COLLABORATION NETWORK (AUTHORS)
# ============================================================================

# Author collaboration network
NetMatrix_collab <- biblioNetwork(M, analysis = "collaboration", 
                                 network = "authors", sep = ";")

# Plot collaboration network
png("outputs/plots/author_collaboration.png", width = 1600, height = 1200, res = 150)
net_collab <- networkPlot(NetMatrix_collab, n = 50,
                         Title = "Author Collaboration Network",
                         type = "auto", size = TRUE,
                         remove.multiple = FALSE, labelsize = 0.5,
                         cluster = "optimal")
dev.off()

write.csv(net_collab$nodeDegree, "outputs/tables/collaboration_metrics.csv")

# ============================================================================
# SECTION 14: THEMATIC MAP
# ============================================================================

# Create thematic map
Map <- thematicMap(M, field = "DE", n = 250, minfreq = 5,
                  stemming = FALSE, size = 0.7, n.labels = 4)

# Plot thematic map
png("outputs/plots/thematic_map.png", width = 1600, height = 1200, res = 150)
plot(Map$map)
dev.off()

# Save thematic clusters
write.csv(Map$words, "outputs/tables/thematic_clusters.csv")

# ============================================================================
# SECTION 15: THEMATIC EVOLUTION
# ============================================================================

# Define time periods (adjust years as needed)
years <- c(2013, 2017, 2020, 2023)

# Thematic evolution analysis
nexus <- thematicEvolution(M, field = "DE", years = years, 
                          n = 100, minFreq = 2)

# Plot evolution
png("outputs/plots/thematic_evolution.png", width = 1800, height = 1200, res = 150)
plotThematicEvolution(nexus$Nodes, nexus$Edges)
dev.off()

# ============================================================================
# SECTION 16: CONCEPTUAL STRUCTURE MAP (MCA/CA)
# ============================================================================

# Conceptual structure using Multiple Correspondence Analysis
CS <- conceptualStructure(M, field = "DE", method = "MCA", 
                         minDegree = 5, clust = 5, 
                         stemming = FALSE, labelsize = 8,
                         documents = 20)

# ============================================================================
# SECTION 17: TREND TOPICS
# ============================================================================

# Identify trending topics
topicTrends <- fieldByYear(M, field = "DE", timespan = c(2013:2023), 
                          min.freq = 3, n.items = 5, graph = TRUE)

png("outputs/plots/trending_topics.png", width = 1400, height = 1000, res = 150)
plot(topicTrends)
dev.off()

# ============================================================================
# SECTION 18: THREE FIELDS PLOT
# ============================================================================

# Sankey diagram: Authors - Keywords - Sources
png("outputs/plots/three_fields_plot.png", width = 1800, height = 1200, res = 150)
threeFieldsPlot(M, fields = c("AU", "DE", "SO"), n = c(15, 15, 15))
dev.off()

# ============================================================================
# SECTION 19: HISTORIOGRAPH (HISTORICAL CITATION NETWORK)
# ============================================================================

# Create historiograph (most cited papers and their citations)
histResults <- histNetwork(M, min.citations = 10, sep = ";")

# Plot historiograph
png("outputs/plots/historiograph.png", width = 1800, height = 1200, res = 150)
net_hist <- histPlot(histResults, n = 20, size = 5, labelsize = 4)
dev.off()

# ============================================================================
# SECTION 20: EXPORT FOR VOSVIEWER
# ============================================================================

# Export data in VOSviewer format
# Create files that VOSviewer can read directly

# Export citation network
write.table(M[,c("SR", "CR")], "outputs/vosviewer_citation_data.txt", 
           sep = "\t", row.names = FALSE, quote = FALSE)

# Export keyword data
keywords_export <- M[,c("SR", "DE", "ID")]
write.table(keywords_export, "outputs/vosviewer_keyword_data.txt",
           sep = "\t", row.names = FALSE, quote = FALSE)

# ============================================================================
# SECTION 21: GENERATE COMPREHENSIVE REPORT
# ============================================================================

cat("\n")
cat("================================================================================\n")
cat("                    BIBLIOMETRIC ANALYSIS COMPLETE!                             \n")
cat("================================================================================\n")
cat("\n")
cat("Analysis Summary:\n")
cat("-----------------\n")
cat("Total Documents:", nrow(M), "\n")
cat("Time Span:", min(M$PY, na.rm=TRUE), "-", max(M$PY, na.rm=TRUE), "\n")
cat("Total Authors:", length(unique(unlist(strsplit(M$AU, ";")))), "\n")
cat("Total Sources:", length(unique(M$SO)), "\n")
cat("\n")
cat("Output Files Generated:\n")
cat("------------------------\n")
cat("• Tables: outputs/tables/\n")
cat("• Plots: outputs/plots/\n")
cat("• Networks: outputs/networks/\n")
cat("\n")
cat("Next Steps:\n")
cat("-----------\n")
cat("1. Review all generated plots and tables\n")
cat("2. Import network data into VOSviewer for advanced visualization\n")
cat("3. Interpret results in context of your research question\n")
cat("4. Draft your bibliometric analysis paper\n")
cat("\n")
cat("Happy analyzing! 🎉\n")
cat("================================================================================\n")

# ============================================================================
# END OF SCRIPT
# ============================================================================

# Save workspace (optional)
# save.image("outputs/bibliometric_analysis_workspace.RData")

# To load saved workspace later:
# load("outputs/bibliometric_analysis_workspace.RData")
