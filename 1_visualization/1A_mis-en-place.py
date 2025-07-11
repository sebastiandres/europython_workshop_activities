"""
Mis-en-place:
- Clean your data before plotting. Have everything ready before plotting.

Here the example: Transform from vertical bars to horizontal bars, and sort them by value.

Data: Some random data
"""

import matplotlib.pyplot as plt
import pandas as pd
import os

# Load the data
data_dict = {"Chile":30, "Argentina":20, "Brazil":10, "Colombia":40, "Mexico":50}
df = pd.DataFrame(data_dict.items(), columns=["Country", "Value"])

# Default plot
#fig, ax = plt.subplots()
#ax.bar(df["Country"], df["Value"])
#figname = os.path.join("figures", "01A_mis-en-place.png")
#plt.savefig(figname)
#print(f"open {figname}")

# TODO:
"""
df = df.sort_values(by="Value", ascending=True)
fig, ax = plt.subplots()
color_list = ["lightgray"] * len(df)
color_list[-1] = "darkred"
ax.barh(df["Country"], df["Value"], color=color_list)

# Save the figure
figname = os.path.join("figures", "01A_mis-en-place.png")
plt.savefig(figname)
print(f"open {figname}")
"""