"""
Do a progression of plots with the same data

1. Showing the last 3: hydro, wind, solar.
2. Showing next one: nuclear.
3. Showing the next one: thermal.
4. Highlight the last one on red: nuclear.
"""
import matplotlib.pyplot as plt
import pandas as pd
import os

# Load the data
data_dict = {"thermal":39506.288, "hydro":3416.997, "wind":701.606, "solar":3210.432, "nuclear":30410.464}
df = pd.DataFrame(data_dict.items(), columns=["Source", "Value"])

# Sort the bars decreasingly by value
df = df.sort_values(by="Value", ascending=True)

# Define the colors
color_list = ["lightgray"] * len(df)
color_list[-2] = "darkred"

# Plot the bars
fig, ax = plt.subplots()
ax.barh(df["Source"], df["Value"], color=color_list)

# Remove top and right splines
ax.spines[["top", "right"]].set_visible(False)

# Remove the ticks on the left
ax.tick_params(left=False)

# Change the ticks on the bottom to be multiples of 10000
ax.xaxis.set_major_locator(plt.MultipleLocator(10000))

# Add the format to be multiples of 10,000
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f"{x:,.0f}"))

# Add gray line to the major ticks
#ax.xaxis.grid(True, linestyle="-", color="gray", alpha=0.25)

# Add a title
ax.set_title("Czechia Gross Energy Production by source (2023)")

# Add xlabel
ax.set_xlabel("Value (GWh)")

# Save the figure
figname = "progression_exercise.png"
plt.savefig(figname)
print(f"open {figname}")