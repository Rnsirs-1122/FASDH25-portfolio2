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

# 2B. Using Stanza to Extract Place Names from News Corpus
## Overview
This project extracts all the place entities that are refered to **places** (GPE/LOC) from a large corpus of news articles using the **Stanza NLP library**. The extracted data focuses specifically on **articles written in January 2024**. The final output is a cleaned and normalized list of place names along with their frequency counts, saved in a `ner_counts.tsv` file.

### 1. Install and Import Stanza
We installed the `stanza` library and downloaded the English language model to perform tokenization and Named Entity Recognition (NER).

```python
!pip install stanza
import stanza
stanza.download("en")
nlp = stanza.Pipeline(lang="en", processors='tokenize,ner')

### We cloned our FASDH25-portfolio2 repository which contains the complete corpus of articles.
### We navigated to the /articles folder and selected only those articles that were written in January 2024, using a condition that checks filenames.
### Using the Stanza pipeline, we analyzed each file and extracted entities labeled as GPE (Geo-Political Entities) or LOC (Locations). These were stored in a dictionary with their frequency.
### We cleaned up the extracted entities to merge duplicates and improve consistency by:

Removing possessives (’s, 's)

Removing punctuation

Removing leading "the" in names
### We saved the final dictionary into a .tsv file (ner_counts.tsv) with two columns: name and frequency.
### We printed the file to ensure it was correctly formatted. 
### ner_counts.tsv: A tab-separated file containing place names and how frequently they appear in January 2024 articles.

Gaza_NER2_<your_groupname>.ipynb: The notebook has been renamed with our group name and uploaded to the repository.

#  Named Entity Recognition (NER) Gazetteer Builder

This project takes a list of place names fetched through NER and extracts their geographical coordinates using the **GeoNames API**. The end goal is to build a **gazetteer** a structured table of places along with their latitude and longitude.

---
# C Create a gazetteer for the NER places 

##  What This Project Does

This script reads a file called `ner_counts.tsv`, which contains a list of place names mentioned in news articles or documents after January 2024. It then uses the **GeoNames geocoding API** to find the corresponding **latitude and longitude** for each place.

The final result is a TSV file, saved as:
NER_gazetteer.tsv

## Working (Steps)

**Reading the Place Names**
   The script opens `ner_counts.tsv`, reads the place names line by line, and stores them in a list.

**Geocoding Each Place**
   For each place, the script uses a function get_coordinates() that sends a query to the [GeoNames API](https://www.geonames.org/).
 It fetches the first matching result (if available) and extracts its latitude and longitude.

**Missing Coordinates**
 If no result is found via the API, the coordinates are marked as "NA".

**Manual Filling Coordinates**
After the initial script run, any `"NA"` entries are manually researched using **Google Maps** and updated in the final `NER_gazetteer.tsv` file with the help of **Google Spreadsheets** and the final tsv file is saved back to the portfolio folder.

**Writing the Output:**
 The script writes the final coordinates to a file in the `gazetteer/` folder, with proper tab-separated formatting.

---

How The Project is organized

This project contains several key components organized for clarity and functionality. At the top level, there is a Python script named build_gazetteer.py, which is responsible for creating a structured list of place names — also known as a gazetteer — using Named Entity Recognition (NER) or other methods. Alongside this script, you’ll find the file ner_counts.tsv, which stores the output of the NER process. This file lists place names and the number of times each was mentioned in the dataset.

There is also a folder named gazetteer, which contains a file called NER_gazetteer.tsv. This is the final gazetteer file, containing a list of place names along with their latitude and longitude. It serves as a cleaned and location-enriched reference for place name detection.

Finally, the README.md file (this document) provides a detailed explanation of the project structure, what each file does, and how users can run and understand the code. This organization helps keep the project maintainable, readable, and easy to extend.


---

##  How To Run the Project

### Step 1: Install Python Dependencies

Step 2: Getting a GeoNames Username

Step 3: Running the script

Step 4: Downloading the final script

Step 5: Manually adding coordinates for the places specified with NA with the help go Google Maps

# 4A. Map the regex-extracted placenames 
## Regex-Based Place Name Mapping with Plotly

We visualized place names extracted using **regular expressions** by mapping their frequency across time and space using `plotly.express`.

### Steps Followed

1. **Data Source**: We used `regex_counts.tsv` which contains place names, their frequencies, and the corresponding month of publication.
2. **Geocoding**: Each unique place was geocoded using the `geopy` library and OpenStreetMap’s Nominatim API to obtain latitude and longitude.
3. **Mapping**: We used `plotly.express.scatter_geo` to plot an animated map where each frame represents a different month. The bubble size and color represent the frequency of mentions.

### Design Choices

- **Animation by Month**: This allows users to explore changes over time interactively.
- **Bubble Size & Color**: Both scaled by frequency to intuitively represent intensity of place mentions.
- **Projection**: We used the `natural earth` projection for a clean global view.
- **Dark Theme**: `plotly_dark` was chosen for better visual contrast.

### Saved Outputs

- `regex_map.html`: Fully interactive map (animation, zoom, hover).
- `regex_map.png`: Static image for presentations or reports.

This approach provides both **temporal** and **spatial** context for place name frequencies in the corpus, making patterns easy to detect over time.

# 4B. Map the NER-extracted placenames 
## NER-Based Mapping of Place Name Frequencies (January 2024)

We used Named Entity Recognition (NER) via the Stanza NLP library to extract place names from news articles dated **January 2024**. 

### Data Sources

- `ner_counts.tsv`: Contains place names and their frequencies from January 2024 articles.
- `NER_gazetteer.tsv`: Contains geocoded latitude and longitude for each place.

### Visualization

Using `plotly.express`, we created a **static and interactive map** to display the geographical distribution and frequency of place mentions.

### Design Choices

- **Bubble Size & Color**: Represent the frequency of place mentions.
- **Projection**: Natural Earth — chosen for a balanced global view.
- **Theme**: Dark for high contrast and readability.
- **Interactivity**: Hover to view place names and zoom for detail.

### Outputs

- `ner_map.html`: An interactive map.
- `ner_map.png`: A static image suitable for documentation or slides.

Links for both the maps:
file:///C:/Users/Haroon%20Traders/Downloads/FASDH25-portfolio2/Scripts/regex_map.html
file:///C:/Users/Haroon%20Traders/Downloads/FASDH25-portfolio2/Scripts/NER_map.html

