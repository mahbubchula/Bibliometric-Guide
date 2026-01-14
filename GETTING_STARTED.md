# 🚀 Getting Started with Bibliometric Analysis

## Welcome! 👋

This guide will help you get started with your bibliometric analysis journey in just a few simple steps.

---

## Step 1: Choose Your Path

### Path A: I Just Want to Learn (Recommended for Beginners)
1. Open `index.html` in your web browser
2. Start with Module 1: Introduction
3. Follow the interactive course sequentially
4. No installation required yet!

### Path B: I'm Ready to Analyze My Data
1. Complete installation prerequisites (see below)
2. Collect your data from Web of Science or Scopus
3. Follow Module 3 for Biblioshiny or Module 4 for VOSviewer
4. Use the provided templates

---

## Step 2: Install Prerequisites

### For Biblioshiny (R-based Analysis)

#### Install R
1. Go to [https://cran.r-project.org/](https://cran.r-project.org/)
2. Download R for your operating system:
   - **Windows**: Click "Download R for Windows" → "base" → Download
   - **macOS**: Click "Download R for macOS" → Choose your version
   - **Linux**: Follow distribution-specific instructions
3. Run the installer with default settings
4. Verify installation: Open R and check version

#### Install RStudio (Optional but Recommended)
1. Go to [https://posit.co/download/rstudio-desktop/](https://posit.co/download/rstudio-desktop/)
2. Download the free version
3. Install after R is installed
4. Launch RStudio

#### Install Bibliometrix Package
Open R or RStudio and run:
```r
install.packages("bibliometrix")
library(bibliometrix)
biblioshiny()  # Launch the interface
```

### For VOSviewer (Visualization Tool)

#### Install Java (if not already installed)
1. Check if Java is installed:
   - Open terminal/command prompt
   - Type: `java -version`
   - If you see version info, you're good to go!

2. If Java is not installed:
   - Go to [https://www.java.com/download/](https://www.java.com/download/)
   - Download and install Java Runtime Environment (JRE)

#### Install VOSviewer
1. Go to [https://www.vosviewer.com/download](https://www.vosviewer.com/download)
2. Download for your operating system
3. Extract the ZIP file
4. Run VOSviewer:
   - **Windows**: Double-click `VOSviewer.jar` or `VOSviewer.exe`
   - **macOS**: Double-click `VOSviewer.jar`
   - **Linux**: Run `java -jar VOSviewer.jar`

---

## Step 3: Get Data Access

### Option 1: Institutional Access (Recommended)
Check if your university provides access to:
- **Web of Science** (Clarivate)
- **Scopus** (Elsevier)

For Chulalongkorn University students:
1. Go to library website: [https://www.car.chula.ac.th/](https://www.car.chula.ac.th/)
2. Navigate to "Databases"
3. Search for "Web of Science" or "Scopus"
4. Login with your student credentials

### Option 2: Alternative Access
- Use **Google Scholar** (free but limited)
- Request access through your department
- Use publicly available datasets from our examples folder

---

## Step 4: Test Your Setup

### Test Biblioshiny
```r
# In R or RStudio
library(bibliometrix)

# Check package version (should be 4.x or higher)
packageVersion("bibliometrix")

# Launch Biblioshiny
biblioshiny()

# A browser window should open automatically!
```

### Test VOSviewer
1. Launch VOSviewer
2. If the program opens successfully, you're ready!
3. Try the tutorial: File → Open → Select example data

---

## Step 5: Try Your First Analysis

### Quick Start with Sample Data

We provide sample datasets in the `examples/` folder:
- `sample_wos_data.txt` - Web of Science format
- `sample_scopus_data.csv` - Scopus format

#### Using Biblioshiny:
```r
library(bibliometrix)

# Load sample data
file <- "examples/sample_wos_data.txt"
M <- convert2df(file, dbsource = "wos", format = "plaintext")

# Generate summary
results <- biblioAnalysis(M)
summary(results, k=10)

# Create visualization
plot(results, k=10, pause=FALSE)
```

#### Using VOSviewer:
1. Open VOSviewer
2. Click "Create" → "Create map based on bibliographic data"
3. Select "Read data from bibliographic database files"
4. Choose `examples/sample_wos_data.txt`
5. Click "Next" and follow the wizard

---

## Common Issues & Solutions

### Issue: R Installation Fails on Windows
**Solution**: Install Rtools
- Download from: [https://cran.r-project.org/bin/windows/Rtools/](https://cran.r-project.org/bin/windows/Rtools/)
- Run installer
- Retry R installation

### Issue: VOSviewer Won't Open
**Solution**: Java version mismatch
- Ensure Java 8 or higher is installed
- Try running from command line: `java -jar VOSviewer.jar`
- Check Java version: `java -version`

### Issue: Biblioshiny Interface Won't Load
**Solution**: Port conflict
```r
# Try a different port
biblioshiny(port=8080)
# or
biblioshiny(port=8888)
```

### Issue: Can't Access Web of Science/Scopus
**Solution**: Check institutional access
- Contact your library
- Verify you're on campus network or using VPN
- Try alternative databases

---

## Next Steps

Once everything is set up:

1. **Beginner Path**:
   - Complete Module 1: Introduction
   - Practice with sample datasets
   - Learn data collection strategies

2. **Intermediate Path**:
   - Collect your own data
   - Follow Biblioshiny tutorial
   - Create your first visualizations

3. **Advanced Path**:
   - Combine Biblioshiny and VOSviewer
   - Analyze your research field
   - Write your paper

---

## Need Help?

- 📖 Check the [FAQ](resources/faq.md)
- 🎥 Watch [Video Tutorials](resources/video_tutorials/)
- 💬 Join discussions in [Issues](https://github.com/mahbubchula/Bibliometric-Analysis-by-Mahbub/issues)
- 📧 Contact: mahbub.hassan@ieee.org

---

## Checklist Before Starting

- [ ] R installed (version 4.0+)
- [ ] RStudio installed (optional)
- [ ] bibliometrix package installed
- [ ] Java installed (for VOSviewer)
- [ ] VOSviewer downloaded
- [ ] Database access confirmed
- [ ] Sample data tested
- [ ] Ready to learn!

---

## Quick Reference Card

### Essential R Commands
```r
# Launch Biblioshiny
library(bibliometrix)
biblioshiny()

# Load data
M <- convert2df("file.txt", dbsource="wos", format="plaintext")

# Basic analysis
results <- biblioAnalysis(M)
summary(results, k=10)

# Create plot
plot(results, k=10)
```

### Essential VOSviewer Steps
1. **Create Map**: File → Create → Choose data type
2. **Customize**: Use toolbar to adjust layout, colors, labels
3. **Export**: File → Save map/network → Choose format

---

<div align="center">

### You're All Set! 🎉

**Now open `index.html` and start your bibliometric analysis journey!**

Made with ❤️ by Mahbub Hassan | Chulalongkorn University

</div>
