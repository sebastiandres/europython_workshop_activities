"""
01_progression.py

Use plt.save_fig() to save partial figures, so you can control exactly what the audience is seeing.

Data: data/net_consumption_energy.csv
Columns:
territory, indicator, source, years, value
"""

import matplotlib.pyplot as plt
import pandas as pd
import os

# Load the data
input_csv_path = os.path.join("data", "net_consumption_energy_sorted.csv")
df = pd.read_csv(input_csv_path)

# Compute the minimum and maximum values for x-axis
x_min_value = df["years"].min()
x_max_value = df["years"].max()

# Compute the minimum and maximum values for y-axis
y_min_value = 0
y_max_value = df["value"].max() * 1.05

# Plot the data
fig, ax = plt.subplots()

# Set the x-axis limits
ax.set_xlim(x_min_value, x_max_value)
ax.set_xlabel("Years")
ax.set_ylim(y_min_value, y_max_value)
ax.set_ylabel("Energy [units?]")

# Save
source_groups = [ ["wind", "solar", "hydro"], ["thermal"], ["nuclear"], ]
for i, source_group in enumerate(source_groups):
    df_source = df[df["source"].isin(source_group)]
    plt.plot(df_source["years"], df_source["value"])
    fig_path = os.path.join("figures", f"02_net_consumption_energy_{i}.png")
    plt.savefig(fig_path)

# Show the plot
fig_path = os.path.join("figures", f"02_net_consumption_energy_{i+1}.png")
plt.savefig(fig_path)
print(f"open figures/02_*.png")
