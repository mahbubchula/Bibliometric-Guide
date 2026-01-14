# Templates & Resources

This folder contains code templates and guides for bibliometric analysis.

## 📂 Folder Structure

### 📁 biblioshiny_scripts/
R scripts and templates for Biblioshiny analysis
- `complete_analysis_template.R` - Full analysis workflow (⭐ Main template)

### 📁 vosviewer_guides/
Step-by-step guides for VOSviewer
- Network creation tutorials
- Visualization customization guides
- Export instructions

### 📁 paper_templates/
Academic writing templates
- Bibliometric paper structure
- Methods section templates
- Results reporting templates
- PRISMA diagram templates

## 🔥 Featured: Complete Analysis Template

**File:** `biblioshiny_scripts/complete_analysis_template.R`

### What It Does:
✅ Imports data from WoS, Scopus, or PubMed  
✅ Generates 20+ statistical tables  
✅ Creates 15+ publication-quality plots  
✅ Performs all major bibliometric analyses  
✅ Exports data for VOSviewer  
✅ Produces comprehensive reports  

### Quick Start:
```r
# 1. Open the template in RStudio
# 2. Change the file path to your data
file <- "path/to/your/data.txt"

# 3. Run the script section by section
# 4. Find all outputs in 'outputs/' folder
```

### Analyses Included:
- Descriptive statistics
- Annual production trends
- Citation analysis
- Author productivity
- Country collaboration
- Keyword analysis
- Co-occurrence networks
- Co-citation analysis
- Bibliographic coupling
- Thematic mapping
- Thematic evolution
- And much more!

## 📝 How to Use Templates

### For Beginners:
1. Start with the complete analysis template
2. Read the comments carefully
3. Run one section at a time
4. Check the outputs folder after each section
5. Modify parameters as needed

### For Advanced Users:
1. Extract relevant sections
2. Customize for your specific needs
3. Combine with your own code
4. Contribute improvements back!

## 🤝 Contributing Templates

Have a useful template? Share it!

### To Add a Template:
1. Ensure code is well-commented
2. Add a header with:
   - Purpose
   - Author
   - Date
   - Required packages
   - Example usage
3. Test thoroughly
4. Submit a pull request

### Template Guidelines:
- ✅ Clear, descriptive names
- ✅ Comprehensive comments
- ✅ Error handling included
- ✅ Example data provided
- ✅ Output descriptions
- ✅ Dependencies listed

## 📚 Additional Resources

### R Packages Used:
- `bibliometrix` - Main analysis package
- `dplyr` - Data manipulation
- `ggplot2` - Visualizations
- `igraph` - Network analysis
- `FactoMineR` - Multivariate analysis

### Installation:
```r
install.packages(c("bibliometrix", "dplyr", "ggplot2"))
```

### Documentation:
- [Bibliometrix Official Site](https://www.bibliometrix.org)
- [R Documentation](https://www.rdocumentation.org/)
- [VOSviewer Manual](https://www.vosviewer.com/documentation/Manual_VOSviewer_1.6.18.pdf)

## 🆘 Need Help?

- Check the [Quick Reference Guide](../resources/cheat_sheets/biblioshiny_quick_reference.md)
- Open an issue on GitHub
- Contact: mahbub.hassan@ieee.org

---

**Happy Analyzing!** 🎉
