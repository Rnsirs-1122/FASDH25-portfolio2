import pandas as pd
import plotly.express as px

# Load data
ner_counts = pd.read_csv(r"C:\Users\Haroon Traders\Downloads\FASDH25-portfolio2/ner_counts.tsv", sep="\t")
coordinates = pd.read_csv(r"C:\Users\Haroon Traders\Downloads\FASDH25-portfolio2/ner_gazetteer.tsv", sep="\t")


# Clean column names
ner_counts.columns = ner_counts.columns.str.strip()
coordinates.columns = coordinates.columns.str.strip()


# Function to clean coordinate values
def clean_coordinate(coord):
    if isinstance(coord, str):
        # Remove degree symbols, quotes, etc.
        coord = coord.split('°')[0]  # Take part before degree symbol
        coord = coord.split('′')[0]  # Take part before minute symbol
        coord = coord.split('"')[0]  # Take part before second symbol
        # Handle cases like "35.1231°" which becomes "35.1231"
        try:
            return float(coord)
        except ValueError:
            return None
    return coord


coordinates['latitude'] = coordinates['latitude'].apply(clean_coordinate)
coordinates['longitude'] = coordinates['longitude'].apply(clean_coordinate)





# Rename columns in coordinates to match ner_counts and plotting requirements



#ner_counts = ner_counts.rename(columns={"name": "placename", "frequency": "ner_count"})
#coordinates = coordinates.rename(columns={"Name": "Place", "Latitude": "latitude", "Longitude": "longitude"})

ner_counts = ner_counts.rename(columns={"name": "Place", "frequency": "ner_count"})
coordinates = coordinates.rename(columns={"name": "Place"})





# Merge data on 'placename'
data = pd.merge(ner_counts, coordinates, on="Place")

# Ensure 'ner_count' is numeric and drop rows with missing values
data["count"] = pd.to_numeric(data["ner_count"], errors="coerce")
data = data.dropna(subset=["ner_count", "latitude", "longitude"])

fig = px.scatter_map(
    data,
    lat="latitude",
    lon="longitude",
    hover_name="Place",
    size="count",
    color="count",
    title="NER-extracted Places",
    zoom=2,
)

fig.show()

# Save map to an HTML file
fig.write_html("NER_map.html")
