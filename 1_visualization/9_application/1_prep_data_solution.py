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
df_all = df_all.rename(columns={"Years":"Year"})

## Convert Years and Value to numeric
df_all["Year"] = pd.to_numeric(df_all["Year"], errors="coerce")
df_all["Value"] = pd.to_numeric(df_all["Value"], errors="coerce")

## Select the country Czechia
df = df_all[df_all["Territory"] == "Czechia"]

## Add a simpler "source" column for each type of energy
source = df["Indicator"].str.split(" - ").str[1]
df["Source"] = source.str.split(" ").str[0]

## All columns in lowercase
df.columns = df.columns.str.lower()

## Sort the data by indicator, and by year
df = df.sort_values(by=["source", "year"])

# Save
output_columns = ["territory", "indicator", "source", "year", "value"]
output_df = df[output_columns]

## Save the sorted data
output_csv_filepath = os.path.join("data", "gross_energy_production_sorted_solution.csv")
output_df.to_csv(output_csv_filepath, index=False)

# Some printing
print(f"Saved into file {output_csv_filepath}")
print(output_df.head())
