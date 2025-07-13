"""
TODO:
- Create a plot of the gross energy production in Czechia by source, 
applying the ideas of the previous exercises.

Data: data/gross_energy_production_sorted.csv
"""

import matplotlib.pyplot as plt
import pandas as pd
import os
from highlight_text import fig_text

# Load the data
input_csv_path = os.path.join("data", "gross_energy_production_sorted.csv")
df = pd.read_csv(input_csv_path)

# Compute the minimum and maximum values for x-axis
x_min_value = 0
x_max_value = 1

# Compute the minimum and maximum values for y-axis
y_min_value = 0
y_max_value = 1

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(top=0.75)

# Add the format to be multiples of 10,000
#ax.yaxis.set_major_formatter


# Set the x-axis limits
#ax.set_xlim
#fig.text
#ax.set_ylim
#fig.text

# Remove the top and right spines
#ax.spines
#ax.spines

# Save
source_groups = [ ["wind"], ["solar", "hydro"], ["nuclear"], ["thermal"]]
#plot_properties = 
#highlight_properties = 

# Plot the data
for i, source_group in enumerate(source_groups):
    for source in source_group:
      ax.text(i/5, i/5, "to-do")
    figname_path = f"02_gross_energy_production_exercise_{i}.png"
    plt.savefig(figname_path)

# Add a plot title
# Set a title with colorful annotations
fig_text#

subtitle_str = """Renowable energy sources (wind, solar & hydro) are marginally small, without any increasing trend.
Nuclear is the second largest source of energy, with a stable production over the years.
Thermal is the largest source of energy, and has been decreasing over the last decade.
"""
fig_text(
  x=0.5, y=0.900,
  s=subtitle_str,
  color="black",
  ax=ax, 
  size=12,
  ha="center",
  va="top",
  #highlight_textprops=highlight_properties
)

# Show the plot
i+=1
figname_path = f"02_gross_energy_production_exercise_{i}.png"
plt.savefig(figname_path)
print(f"open *.png")
print(f"open {figname_path}")
