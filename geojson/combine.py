# To get coordinates of a county
# Iterate through all .JSON files in "counties" folder
# Get file name of the .JSON file
# Get centroid.coordinates
# Key value pair of { "center": centroid.coordinates }
# Parse through similar file name "geojson" folder
# get geometries[0] prop

# create new object with code.json filename
# save file in coordinates folder

import os
import json

kenya = {
    "type": "FeatureCollection",
    "features": [

    ],
}
for filename in os.listdir("geojson"):
    
    county_data =         {
            "type": "Feature",
            "id": "01",
            "properties": {"name": "", "density": ""},
            "geometry": {"type": "Polygon", "coordinates": ''},
        }

    f2 = open("geojson/{x}".format(x=filename))
    print(f"{filename}")
    geo = json.load(f2)
    county_name = filename.replace('.json', '').capitalize() + ' County'
    
    print(f"{county_name}")
    
    county_data['properties']['name'] = county_name
    

    # Serializing json
    # json_object = json.dumps(county, indent=4)

# Writing to sample.json
# with open("geojson/{x}".format(x=filename), "w") as outfile:
#     outfile.write(json_object)
