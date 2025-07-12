"""
Mis-en-place:
- Clean your data before plotting. 
- Have everything ready before plotting.

TO-DO LIST:
1. Change the vertical bars to horizontal bars.
2. Sort the bars decreasingly by value.
3. Use a different color for the second bar.

Data: Czechia Gross Energy Production by source (2023)
"""

import matplotlib.pyplot as plt
import pandas as pd
import os

# Load the data: 
data_dict = {"thermal":39506.288, "hydro":3416.997, "wind":701.606, "solar":3210.432, "nuclear":30410.464}
df = pd.DataFrame(data_dict.items(), columns=["Source", "Value"])

# Sort the bars decreasingly by value

# Plot the bars
fig, ax = plt.subplots()
ax.bar(df["Source"], df["Value"])

# Add a title
ax.set_title("Czechia Gross Energy Production by source (2023)")

# Add xlabel
ax.set_ylabel("Value (GWh)")

# Save the figure
figname = "mis-en-place_exercise.png"
plt.savefig(figname)
print(f"open {figname}")