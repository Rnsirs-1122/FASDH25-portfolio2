'''This is your starting script for today's Python class.

This script contains the code we wrote last week
to count the number of times each place in Gaza
is mentioned in our corpus.

Now, we want to store this count into a tsv file.

I have written a function (write csv) to do this -
but it has some mistakes in it.

Please fix the mistakes and call the function
to write the 

'''
# importing re module to search for words using patterns
import re
# importing os to deal with folders and paths
import os
# importing pandas in order to get the outputs in the form of table
import pandas as pd


# define which folder to use:

# have to set a path to the folder where our articles exist we want to work on
folder = "../articles"  


# load the gazetteer from the tsv file:
# have to open the gazetter file where the place names are present we have to work on
path = "../gazetteers/geonames_gaza_selection.tsv"
with open(path, "r", encoding = "utf-8") as file:
    data = file.read()
rows = data.strip().split("\n")

# crating a dictionary to map each place to all its known name variatons 
main_names = {}

# skipping the first line and then going through each place name in the list
for row in rows[1:]:
    columns = row.split("\t") # splitting the row through tab to get individual columns
    asciiname = columns[0].strip() # getting the standard name of places
    main_name = asciiname.lower() # converting into lowercase for easier matching which would be needed later
    name = columns [4].strip().lower() # including alternate name to making the matching complete
    alternatenames = columns[5] # getting columns (comma separated alternate names)

# creating a list of lowercase alternate names
    alternatenames_list = [alt.strip().lower() for alt in alternatenames.split(",") if alt.strip()]
    main_names[main_name] = [main_name, name] + alternatenames_list
    

# build a dictionary of patterns from the place names in the first column:
# creating dictionary to show how many times each place is mentioned in each month
mentions_per_month = {}


# count the number of times each pattern is found in the entire folder:
for filename in os.listdir(folder):
    date = filename[:10] # extracting the date part from the filename
    if date>= "2023-10-07": # selecting articles published after October 7 
        month = filename[:7] # asking to extract only year and month
        
        # build the file path:
        file_path = os.path.join(folder, filename)
        #print(f"The path to the article is: {file_path}")

        # load the article (text file) into Python:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read() # this one is the full article text

        # find all the occurences of the patterns in the text:
        for main_name, other_names in main_names.items():
            # creating a pattern that resembles any name variation for this place
            expression = r"\b("+"|".join(map(re.escape, other_names)) + r")\b"

            # searching for matches of this pattern in the article text
            matches = re.findall(expression, text, flags = re.IGNORECASE)
            n_matches = len(matches) # conting the number of time the place was mentioned
            # add the number of times it was found to the total frequency:
            if n_matches>0:
                # creating a record for the place seen for the first time
                if main_name not in mentions_per_month:
                    mentions_per_month[main_name] = {}
                #     
                mentions_per_month[main_name][month] = (mentions_per_month[main_name].get(month, 0) + n_matches)

# printing the result 
for place, months in mentions_per_month.items():
    print(f"{place}:") # print name of the place
    for month, n_matches in months.items():
        print(f"{month}:{n_matches}") # print count of mentions per month                                                

# call the function to write your tsv file:
# defining name of columns for the table we are going to create
columns = ["asciiname", "month","frequency"]

# decide a name for output file to save the results
tsv_filename = "regex_counts.tsv"

import pandas as pd

rows = []

# add place/month/n_matches to the list
for main_name, months in mentions_per_month.items():
    for month, n_matches in months.items():
        # every row is a list with name, month, and frequency
        rows.append([main_name, month, n_matches])

# converting list of rows into DataFrame
df = pd.DataFrame(rows, columns = columns)

# sorting the table to make it easy to read, place name first and then month
df.sort_values(by =["asciiname", "month"], inplace = True)

# Lastly saving the table to a tsv file, using tab to separate columns
df.to_csv(tsv_filename, sep="\t", index = False)


        
 

        

