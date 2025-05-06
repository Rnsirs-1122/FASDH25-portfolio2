# FASDH25-portfolio2
A repository for students' portfolios for mini-project 2

#  Extracting and Counting Place Mentions in Gaza Articles  

This project **analyzes text articles** to count how often different places in **Gaza** are mentioned. It uses 

A **gazetteer** (list of place names and their variations)  
**Regular expressions (regex)** to find place mentions  
 **Filtering** to include only articles from the **current war (October 7, 2023, onward)**  
 **Monthly mention counting** to track trends over time  
 **A tsv output file** for structured data analysis  

---

## Project Folder Structure  

Here is how the project is organized  

 
FASDH25-PORTFOLIO2
|---- scripts
	|----- regex_script_final
	|----- regex_counts.tsv
|------ README.md
|------ gazetteers
	|-----countries.tsv
	|-----geonames_gaza_selection.tsv
	|-----README
---

##  How the Script Works  

###  **Load the Gazetteer (List of Place Names)**  
The script reads the **gazetteer** (`geonames_gaza_selection.tsv`).

Instead of looking for only the **asciiname**, the script builds a **regex pattern** that matches **any** of the alternative names.  

Example for **Khan Younis**:  

Khan Younis|KhanYounis|Khan Younis camp|Mukhayyam Khan Yunis



This **improves recall** (i.e., it catches more mentions).  

---

###  **Scan Articles for Place Mentions**  
- The script **reads all `.txt` files** in the `corpus/` folder.  
- It **skips** any article **published before October 7, 2023**.  
- It searches for **each place name** (using regex) inside the article text.  

 The filename format must be:  
YYYY-MM-DD_article_name.txt


Example:  
2023-10-15_Gaza_Crisis.txt


---

###  **Count Mentions Per Month**  
- The script keeps track of how often each place is mentioned **each month**.  
- It stores the results in a **nested dictionary**:  

```python
{
  "Gaza": {
    "2023-10": 14,
    "2023-11": 21
  },
  "Rafah": {
    "2023-10": 5,
    "2023-11": 8
  }
}
 Save the Results in regex_counts.tsv
The final results are stored in a tab-separated values (TSV) file, regex_counts.tsv, which contains

placename	month	count
Gaza 	2023-10	14
Rafah	2023-11	8
Khan Younis	2023-11	6

