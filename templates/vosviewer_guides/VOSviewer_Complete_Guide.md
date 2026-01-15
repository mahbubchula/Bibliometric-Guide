# VOSviewer Complete Guide
## Professional Network Visualization for Bibliometric Analysis

**Author:** Mahbub Hassan | Chulalongkorn University
**Software Version:** VOSviewer 1.6.20
**Last Updated:** January 2026

---

## 📚 Table of Contents

1. [Installation & Setup](#installation--setup)
2. [Creating Your First Network](#creating-your-first-network)
3. [Co-Authorship Networks](#co-authorship-networks)
4. [Co-Citation Analysis](#co-citation-analysis)
5. [Bibliographic Coupling](#bibliographic-coupling)
6. [Keyword Co-Occurrence](#keyword-co-occurrence)
7. [Customization & Styling](#customization--styling)
8. [Exporting High-Quality Figures](#exporting-high-quality-figures)
9. [Advanced Techniques](#advanced-techniques)
10. [Troubleshooting](#troubleshooting)

---

## 🚀 Installation & Setup

### Step 1: Install Java (Required)

VOSviewer requires Java Runtime Environment (JRE) 8 or higher.

**Check if Java is installed:**
```bash
# Windows (Command Prompt)
java -version

# macOS/Linux (Terminal)
java -version
```

**If Java is not installed:**
1. Download from: https://www.java.com/download/
2. Run installer
3. Restart computer
4. Verify installation

### Step 2: Download VOSviewer

1. Go to: https://www.vosviewer.com/download
2. Download for your operating system:
   - Windows: `VOSviewerSetup.exe`
   - macOS: `VOSviewer.dmg`
   - Linux: `VOSviewer.jar`

### Step 3: Install VOSviewer

**Windows:**
1. Run `VOSviewerSetup.exe`
2. Follow installation wizard
3. Launch from Start Menu or desktop shortcut

**macOS:**
1. Open `VOSviewer.dmg`
2. Drag VOSviewer to Applications folder
3. Launch from Applications

**Linux:**
1. Save `VOSviewer.jar` to preferred location
2. Run: `java -jar VOSviewer.jar`

### Step 4: First Launch

When you launch VOSviewer, you'll see:
- Menu bar (File, Create, View, Tools, Help)
- Toolbar with quick actions
- Empty workspace

---

## 🌐 Creating Your First Network

### Quick Start: Co-Occurrence Network from Biblioshiny

This is the easiest way to start!

#### Step 1: Export Data from Biblioshiny

In R Biblioshiny:
```r
# After loading your data
# Go to: Data > Export data for VOSviewer
# Choose: Author keywords
# Save file: keywords_vosviewer.txt
```

#### Step 2: Import into VOSviewer

1. VOSviewer: **Create > Create map from VOSviewer data**
2. **Browse** → Select your exported file
3. **Next** → VOSviewer reads the data
4. **Next** → Set parameters:
   - **Minimum number of occurrences:** 3
   - (Keywords must appear at least 3 times)
5. **Next** → Select keywords to include:
   - Check all relevant keywords
   - Uncheck generic terms (e.g., "research", "study")
6. **Finish** → Network created!

#### Step 3: View Your Network

**Three views available:**

1. **Network Visualization** (default)
   - Shows connections between items
   - Circle size = number of occurrences
   - Line thickness = co-occurrence strength
   - Colors = clusters (similar items)

2. **Overlay Visualization**
   - Shows temporal evolution
   - Color gradient = average publication year
   - Blue = older topics
   - Yellow/Red = newer topics

3. **Density Visualization**
   - Shows research hotspots
   - Bright = many items nearby
   - Dark = sparse areas

---

## 👥 Co-Authorship Networks

Shows collaboration patterns between authors, countries, or organizations.

### Author Co-Authorship

#### Method 1: From Biblioshiny Export

```r
# In R Biblioshiny
# Data > Export for VOSviewer > Authors
```

Then in VOSviewer:
1. **Create > Create map from VOSviewer data**
2. Select exported file
3. Set minimum documents per author: **2**
4. Finish

#### Method 2: From Raw Data (Web of Science)

1. **Create > Create map from bibliographic database files**
2. **Database:** Select "Web of Science"
3. **Browse:** Select your .txt file
4. **Next**
5. **Type of analysis:** Co-authorship
6. **Unit of analysis:** Authors
7. **Next** → Set threshold:
   - Minimum documents per author: 3-5
   - Minimum citations: 10-20
8. **Next** → Select authors to include
9. **Finish**

### Country Co-Authorship

Shows international collaboration:

1. **Create > Create map from bibliographic database files**
2. Select your data file
3. **Type of analysis:** Co-authorship
4. **Unit of analysis:** Countries
5. Set threshold: Minimum documents per country: 5
6. Finish

**Interpretation:**
- Connected countries = have collaborations
- Link strength = number of co-authored papers
- Clusters = collaboration communities

### Organization Co-Authorship

Shows institutional collaboration:

1. Follow same steps as Country
2. **Unit of analysis:** Organizations
3. Set threshold: Minimum documents per organization: 3
4. **Note:** Organization names may need cleaning!

---

## 📚 Co-Citation Analysis

Shows which papers are cited together (intellectual structure of field).

### Creating Co-Citation Network

#### Step 1: Prepare Data

**Option A: From Scopus**
1. Search your topic in Scopus
2. Select papers
3. Export > CSV Export > Citation information + References
4. Save as `scopus_data.csv`

**Option B: From Web of Science**
1. Search your topic
2. Export > Plain Text > Full Record and Cited References
3. Save as `wos_data.txt`

#### Step 2: Create Network in VOSviewer

1. **Create > Create map from bibliographic database files**
2. Select database type (WoS or Scopus)
3. Browse to your data file
4. **Type of analysis:** Citation
5. **Unit of analysis:** Cited references
6. **Next** → Set parameters:
   - **Minimum citations of a cited reference:** 5-10
   (More = fewer but more important papers)
7. **Next** → Select references
   - VOSviewer shows list of highly cited papers
   - Check papers to include (usually all)
8. **Finish**

#### Step 3: Interpret Results

**Clusters (colors):**
- Each cluster = research theme/subdomain
- Papers in same cluster = conceptually related
- Often represent different research perspectives

**Central papers:**
- Large circles = highly cited
- Connected to many = foundational/seminal

**Peripheral papers:**
- Smaller, fewer connections = niche topics

**Example Clusters in Transportation:**
- Cluster 1 (Red): Electric vehicles technology
- Cluster 2 (Green): Policy and adoption
- Cluster 3 (Blue): Infrastructure planning
- Cluster 4 (Yellow): Environmental impacts

---

## 🔗 Bibliographic Coupling

Shows which papers cite similar references (current research fronts).

### Creating Bibliographic Coupling Network

1. **Create > Create map from bibliographic database files**
2. Select your data file
3. **Type of analysis:** Bibliographic coupling
4. **Unit of analysis:** Documents
5. **Next** → Set threshold:
   - **Minimum citations:** 5-10
   - (Only highly cited papers included)
6. **Next** → Select documents
7. **Finish**

### Interpretation

**Strongly coupled papers:**
- Cite many same references
- Work on similar problems
- Represent current research themes

**Clusters:**
- Each cluster = active research front
- Papers published around same time
- Addressing similar questions

**Comparison with Co-Citation:**
- Co-citation = intellectual base (past)
- Bibliographic coupling = research front (present)

---

## 🔤 Keyword Co-Occurrence

Most popular network type for bibliometric papers!

### Method 1: Author Keywords (Recommended)

1. **Create > Create map from bibliographic database files**
2. Select your WoS or Scopus file
3. **Type of analysis:** Co-occurrence
4. **Unit of analysis:** Author keywords
5. **Next** → Set minimum occurrences: 3-5
6. **Next** → Select keywords
   - Remove generic terms ("model", "method", "analysis")
   - Keep specific domain keywords
7. **Finish**

### Method 2: All Keywords (Author + Index)

1. Same steps as above
2. **Unit of analysis:** All keywords
3. Results include both author keywords and database-assigned keywords
4. Larger network, may need higher threshold (5-10)

### Method 3: Title and Abstract Terms

1. Same setup
2. **Unit of analysis:** All keywords
3. Then **binary counting** or **full counting**
4. **Next** → VOSviewer extracts terms from titles/abstracts
5. Review and select relevant terms
6. Finish

### Cleaning Keywords

VOSviewer has built-in thesaurus:

1. After creating network
2. **Tools > Thesaurus**
3. Merge similar terms:
   - "EV" → "electric vehicle"
   - "machine-learning" → "machine learning"
4. Delete irrelevant terms
5. **Save thesaurus** for future use
6. **Recreate network** with cleaned keywords

---

## 🎨 Customization & Styling

Make your networks publication-quality!

### Changing Colors

**Method 1: Predefined Color Schemes**
1. **View > Colors**
2. Choose scheme:
   - Rainbow
   - Pastel
   - Colorblind-friendly
   - Grayscale

**Method 2: Custom Colors**
1. **View > Colors > Custom...**
2. For each cluster, pick a color
3. Click OK

**Best Practices:**
- Use colorblind-friendly palettes
- Maximum 6-8 distinct colors
- Consistent colors across related figures

### Adjusting Layout

**Zoom:**
- Scroll mouse wheel
- Or **View > Zoom in/out**

**Pan:**
- Click and drag background
- Center on specific item: Double-click it

**Item Size:**
- **View > Item size variation**
- Drag slider: Small → Large

**Label Size:**
- **View > Label size variation**
- Adjust to prevent overlap

**Line Thickness:**
- **View > Line size variation**
- Thicker lines = stronger connections

### Hiding/Showing Elements

**Hide lines (cleaner look):**
- **View > Uncheck "Lines"**
- Shows only circles and labels

**Show/hide labels:**
- **View > Check/uncheck "Labels"**

**Show only selected items:**
1. Click items while holding **Ctrl** (or **Cmd** on Mac)
2. Right-click > **Show selected items**

### Overlay Visualization (Time Evolution)

1. **Switch to Overlay Visualization** tab
2. **View > Colors > Score**
3. Adjust color gradient:
   - Blue = older
   - Red/Yellow = newer
4. Use for trend analysis in papers

### Density Visualization (Hotspots)

1. **Switch to Density Visualization** tab
2. Bright areas = research hotspots
3. **View > Kernel width** → Adjust smoothness
4. **View > Min/max colors** → Change gradient

---

## 💾 Exporting High-Quality Figures

### For Journal Submission (High Resolution)

1. Finalize your network layout
2. **File > Save > Save Image...**
3. Choose format:
   - **PNG** (recommended): 300 DPI minimum
   - **SVG**: Vector (scalable, best quality)
   - **EPS**: For some publishers
4. Set resolution:
   - **Width:** 3000-5000 pixels (for 300 DPI at 10-15cm)
   - Check "Save in high resolution"
5. Save

### Image Settings

**For black & white printing:**
1. **View > Colors > Grayscale**
2. Increase line thickness
3. Use patterns for clusters (if supported)

**For presentations:**
1. Use bright colors
2. Larger labels
3. Fewer items (simplicity)
4. PNG format, 1920x1080 pixels

**For online/web:**
1. PNG or SVG
2. Moderate resolution (1500-2000 px width)
3. File size optimization

---

## 🎓 Advanced Techniques

### Temporal Analysis

Track how research themes evolve over time.

1. Create keyword co-occurrence network
2. **Action > Modify**
3. **Scores > Based on** → Publication year (avg)
4. Switch to **Overlay Visualization**
5. Interpret:
   - Blue keywords = older, established
   - Yellow/Red = emerging topics

### Combining Networks

Analyze multiple aspects together:

1. Create co-citation network
2. **Action > Modify**
3. **Add attribute** → Author keywords
4. View which keywords associate with which papers

### Filtering by Time Period

1. Create network from full dataset
2. **Action > Select > Select items...**
3. Set conditions:
   - Publication year >= 2020
   - Citations >= 10
4. **View > Show selected items**

### Cluster Analysis

Identify and name research themes:

1. Create network (any type)
2. VOSviewer automatically detects clusters
3. Examine each cluster:
   - What items are included?
   - What connects them?
   - Identify common theme
4. Name clusters for your paper:
   - Cluster 1 (Red): "EV Technology"
   - Cluster 2 (Green): "Policy & Adoption"
   - etc.

### Largest Component Only

Show only the main connected network:

1. **Tools > Options**
2. Check "Only show largest component"
3. Hides isolated items

---

## ⚙️ Parameters Guide

### Minimum Occurrences/Documents

**Too low (e.g., 1-2):**
- ❌ Too many items
- ❌ Network overcrowded
- ❌ Difficult to interpret

**Too high (e.g., 20+):**
- ❌ Too few items
- ❌ Miss emerging topics
- ❌ Only show obvious findings

**Recommended:**
- Small dataset (<200 papers): 2-3
- Medium dataset (200-500): 3-5
- Large dataset (500+): 5-10

### Clustering Resolution

Controls number of clusters:

1. **Action > Clustering...**
2. **Resolution:** 0.5 - 2.0
   - Low (0.5-0.8): Fewer, broader clusters
   - Medium (1.0): Default, balanced
   - High (1.5-2.0): More, specific clusters
3. Try different values to find optimal

### Association Strength

How connection strength is calculated:

- **Association strength** (default): Recommended
- **Lin log modularity**: Alternative metric
- **Fractionalization**: For weighted networks

Usually stick with default unless you know what you're doing!

---

## 🐛 Troubleshooting

### Common Issues

**1. "Java not found" error**
- **Solution:** Install Java JRE 8+
- Download from java.com
- Restart computer

**2. VOSviewer won't launch**
- Check Java version: `java -version`
- Update to latest VOSviewer
- Try running as administrator (Windows)

**3. "No items selected" error**
- Threshold too high
- Lower minimum occurrences
- Check data file format

**4. Network looks messy**
- Reduce number of items (higher threshold)
- Hide lines: View > Uncheck "Lines"
- Increase item/label spacing
- Use larger figure size

**5. Labels overlap**
- Reduce label size: View > Label size variation
- Export larger image
- Show fewer labels: Select key items only

**6. Can't import Biblioshiny data**
- Ensure file is VOSviewer format (not regular bibliometric)
- Check file encoding (UTF-8)
- Re-export from Biblioshiny

**7. Organization names inconsistent**
- **Solution:** Manual cleaning required
- Export items list
- Edit in Excel/Notepad
- Standardize names
- Import cleaned list

---

## 📊 Examples for Your Paper

### Figure Captions

**Co-occurrence network:**
> "Figure 3. Keyword co-occurrence network based on author keywords (minimum occurrences = 5). Circle size represents frequency; line thickness represents co-occurrence strength. Colors indicate different thematic clusters identified by VOSviewer clustering algorithm."

**Co-citation network:**
> "Figure 4. Co-citation network of highly cited references (minimum citations = 10). Each node represents a cited reference; links indicate co-citation relationships. Cluster colors represent distinct research themes."

**Overlay visualization:**
> "Figure 5. Temporal evolution of research topics. Colors represent average publication year: blue (older, ~2015-2018) to yellow/red (recent, ~2022-2024). Shows shift from fundamental research (blue) to applied studies (yellow)."

### Interpreting for Results Section

**Example paragraph:**
> "Figure 3 presents the keyword co-occurrence network, revealing five major research clusters. Cluster 1 (red, n=45 keywords) focuses on electric vehicle technology, including battery performance and charging systems. Cluster 2 (green, n=38) emphasizes policy and adoption factors. The strong connection between 'charging infrastructure' and 'user acceptance' (link strength = 25) suggests their interdependent relationship in EV adoption literature."

---

## 📚 Best Practices

### Do's ✅

- Use consistent parameters across similar figures
- Clean keywords before creating networks
- Save high-resolution images (300+ DPI)
- Name and describe clusters clearly
- Combine with Biblioshiny statistics
- Use overlay visualization for trends
- Export to vector format (SVG) when possible

### Don'ts ❌

- Don't overcrowd network (too many items)
- Don't use low-resolution exports for publications
- Don't forget to clean organization names
- Don't mix different network types without explanation
- Don't choose arbitrary thresholds (explain choices)
- Don't use default cluster colors if colorblind-unfriendly

---

## 🎯 Workflow Summary

**Perfect VOSviewer workflow:**

1. **Data Collection** → Get bibliographic data (WoS/Scopus)
2. **Biblioshiny** → Descriptive statistics + export for VOSviewer
3. **VOSviewer** → Create networks
4. **Customize** → Colors, layout, labels
5. **Export** → High-res PNG/SVG
6. **Interpret** → Identify patterns and clusters
7. **Write** → Integrate into paper with clear captions

**Time estimate:** 2-4 hours for complete analysis

---

## 📖 Additional Resources

### Official Documentation
- Manual: https://www.vosviewer.com/documentation/Manual_VOSviewer_1.6.18.pdf
- Website: https://www.vosviewer.com/
- FAQs: https://www.vosviewer.com/faq

### Video Tutorials
- VOSviewer YouTube channel
- Bibliometric analysis workshops
- Research method courses

### Support
- VOSviewer Google Group
- ResearchGate discussions
- Academic librarians

---

## 📧 Questions?

**Need help with VOSviewer?**
- Review this guide carefully
- Check official manual
- Watch video tutorials
- Contact: mahbub.hassan@ieee.org

---

*Created by Mahbub Hassan | Chulalongkorn University*
*Part of Complete Bibliometric Analysis Guide*
*Last Updated: January 2026*
