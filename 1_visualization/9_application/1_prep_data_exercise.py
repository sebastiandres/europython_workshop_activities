"""
TODO:
- Rename "Years" as "Year"
- Convert values from columns "Year" and "Values" to numeric values
- Add a new column "source" with the values "hydro", "wind", etc. from the source.
- Convert all columns to lowercase
- Sort the data by indicator, and by year.
- Save the data into file data/net_consumption_energy_sorted.csv

Data: data/gross_energy_production_original.csv
"""

import matplotlib.pyplot as plt
import pandas as pd
import os

# Load the data
input_csv_filepath = os.path.join("data", "gross_energy_production_original.csv")
df_all = pd.read_csv(input_csv_filepath)
print(f"Processing the file {input_csv_filepath}")
print(df_all.head())
print("")

# Preprocess the data
## Rename column Years
#df_all = df_all.rename(...)

## Convert Years and Value to numeric
#df_all["Year"] = 
#df_all["Value"] = 

## Select the country Czechia
df = df_all[df_all["Territory"] == "Czechia"]

## Add a simpler "source" column for each type of energy
#df["source"] = 

## All columns in lowercase
#df.columns = df.columns.str.lower()

## Sort the data by indicator, and by year
#df = 

# Save
#output_columns = ["territory", "indicator", "source", "year", "value"]
output_df = df #df[output_columns]

## Save the sorted data
output_csv_filepath = os.path.join("data", "gross_energy_production_sorted.csv")
output_df.to_csv(output_csv_filepath, index=False)

# Some printing
print(f"Saved into file {output_csv_filepath}")
print(output_df.head())
