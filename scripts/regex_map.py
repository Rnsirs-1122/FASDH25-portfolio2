#importing the libraries into the script:

import plotly.express as px
import pandas as pd
import re
import os

# Load the TSV data containing regex-extracted place names and frequencies
freq_path = "regex_counts.tsv"
freq_df = pd.read_csv(freq_path, sep="\t")

# Load the tsv file with the frequency data into a dataframe:
coordinates_path= "../gazetteers/geonames_gaza_selection.tsv"
coordinates_df = pd.read_csv(coordinates_path, sep="\t")

# Rename Columns to Have a Common Merge Column
# The frequency data uses "Asciiname", and the coordinate data uses "asciiname"
# We rename both to the same name: "placename", so we can merge them
freq_df.rename(columns={"asciiname": "placename"}, inplace=True)    # Rename in frequency dataframe
coordinates_df.rename(columns={"asciiname": "placename"}, inplace=True)

freq_df['placename'] = freq_df['placename'].str.strip().str.lower()
coordinates_df['placename'] = coordinates_df['placename'].str.strip().str.lower() # Had to use AI for assitance in this specific code



merged_df = pd.merge(freq_df, coordinates_df, on="placename", how="inner")
# Check column names after merge
print(merged_df.columns)

# Create the animated map of place names with frequency as size and color
fig = px.scatter_map(
    merged_df,
    lat="latitude", 
    lon="longitude",
    size="frequency", 
    color="frequency",
    hover_name="placename",
    animation_frame="month",
    map_style="open-street-map",
    zoom = 6,
    size_max= 20,
    center={"lat": 31.5, "lon": 34.5},
    height=700
)


# Save interactive map as HTML
fig.write_html("regex_map.html")

# Save static map as PNG (requires kaleido)
fig.write_image("regex_map.png")



