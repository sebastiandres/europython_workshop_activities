"""
TODO:
- Rename "Years" as "Year"
- Convert values from columns "Year" and "Values" to numeric values
- Add a new column "source" with the values "hydro", "wind", etc. from the source.
- Convert all columns to lowercase
- Sort the data by indicator, and by year.
- Save the data into file data/net_consumption_energy_sorted.csv

Data: data/gross_energy_production_sorted_solution.csv
"""

import matplotlib.pyplot as plt
import pandas as pd
import os
from highlight_text import fig_text

# Load the data
input_csv_path = os.path.join("data", "gross_energy_production_sorted_solution.csv")
df = pd.read_csv(input_csv_path)

# Compute the minimum and maximum values for x-axis
x_min_value = df["year"].min()
x_max_value = df["year"].max()

# Compute the minimum and maximum values for y-axis
y_min_value = 0
y_max_value = df["value"].max() * 1.05

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(top=0.75)

# Add the format to be multiples of 10,000
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f"{x:,.0f}"))

# Set the x-axis limits
ax.set_xlim(x_min_value, x_max_value)
fig.text(0.5, 0.025, "Years", ha="center", va="bottom")
ax.set_ylim(y_min_value, y_max_value)
fig.text(0.02, 0.725, "Energy [GWh]", ha="left", va="center")

# Remove the top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Save an empty plot
i = 0
figname_path = f"02_gross_energy_production_solution_{i}.png"
plt.savefig(figname_path)


# Save
source_groups = [ ["wind"], ["solar", "hydro"], ["nuclear"], ["thermal"]]
plot_properties = { 
    "wind": { "color": "blue", "ha": "left", "va": "top"}, 
    "solar": { "color": "#ffc100", "ha": "left", "va": "top"}, 
    "hydro": { "color": "green", "ha": "left", "va": "bottom"}, 
    "nuclear": { "color": "purple", "ha": "left", "va": "center"}, 
    "thermal": { "color": "red", "ha": "left", "va": "center"}, 
    }
highlight_properties = [ { "color": plot_properties[key]["color"], "weight": "bold"} for key in plot_properties.keys() ]

# Plot the data
for j, source_group in enumerate(source_groups):
    for source in source_group:
        color = plot_properties[source]["color"]
        df_source = df[df["source"]==source]
        plt.plot(df_source["year"], df_source["value"], color=color)
        x_text = df_source["year"].values[-1]
        y_text = df_source["value"].values[-1]
        ax.text(x_text, y_text, source, **plot_properties[source])
    i = j+1
    figname_path = f"02_gross_energy_production_solution_{i}.png"
    plt.savefig(figname_path)

# Add a plot title
# Set a title with colorful annotations
fig_text(
  x=0.5, y=0.975,
  s="Gross Energy Production in Czechia",
  color="black",
  ax=ax, 
  size=15,
  ha="center",
  va="top",
  weight="bold",
)

subtitle_str = """Renowable energy sources (<wind>, <solar> & <hydro>) are marginally small, without any increasing trend.
<Nuclear> is the second largest source of energy, with a stable production over the years.
<Thermal> is the largest source of energy, and has been decreasing over the last decade.
"""
fig_text(
  x=0.5, y=0.900,
  s=subtitle_str,
  color="black",
  ax=ax, 
  size=12,
  ha="center",
  va="top",
  highlight_textprops=highlight_properties
)

# Show the plot
i+=1
figname_path = f"02_gross_energy_production_solution_{i}.png"
plt.savefig(figname_path)
print(f"open *.png")
print(f"open {figname_path}")
