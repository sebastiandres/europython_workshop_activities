"""
01_mis-en-place.py

Sort the data by indicator, and by year.

Data: data/net_consumption_energy.csv
Columns:
"Indicator","Territory","Years","Value"
"""

import matplotlib.pyplot as plt
import pandas as pd
import os

# Load the data
input_csv_path = os.path.join("data", "net_consumption_energy_original.csv")
df_all = pd.read_csv(input_csv_path)

# Preprocess the data
## Convert Years and Value to numeric
df_all["Years"] = pd.to_numeric(df_all["Years"], errors="coerce")
df_all["Value"] = pd.to_numeric(df_all["Value"], errors="coerce")
## Select the country Czechia
df = df_all[df_all["Territory"] == "Czechia"]
## Print the first rows
print(df.head())

# Add a simpler "source" column for each type of energy
source = df["Indicator"].str.split(" - ").str[1]
df["Source"] = source.str.split(" ").str[0]

# Sort the data by indicator, and by year
#df = df.sort_values(by=["Source", "Years"])

# All columns in lowercase
df.columns = df.columns.str.lower()
df = df[["territory", "indicator", "source", "years", "value"]]

# Save the sorted data
output_csv_path = os.path.join("data", "net_consumption_energy_sorted.csv")
df.to_csv(output_csv_path, index=False)

# Plot the data
fig, ax = plt.subplots()

# Save
all_sources = df["source"].unique()
for i, source in enumerate(all_sources):
    df_source = df[df["source"] == source]
    plt.plot(df_source["years"], df_source["value"], label=source)

# Show the plot
fig_path = os.path.join("figures", f"01_net_consumption_energy.png")
plt.savefig(fig_path)
print(f"open figures/01_*.png")
