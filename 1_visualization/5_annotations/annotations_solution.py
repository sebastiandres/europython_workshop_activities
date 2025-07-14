"""
COLORS:
- Use annotations to add text with multiple colors

TODO:
1. Replace the texts with a title with annotations: https://github.com/znstrider/highlight_text
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
from pypalettes import load_cmap
from highlight_text import fig_text
import numpy as np

x = np.linspace(0, 4, 100)
y1 = x # Linear
y2 = x**2 # Squared
y3 = x**3 # Cubed

fig, ax = plt.subplots()

# Choose from:  'tab10', 'tab20', 'tab20b', 'tab20c', 'Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2', 'Set1', 'Set2', 'Set3', 'petroff10'
#colors = mpl.color_sequences["tab20c"]
colors = load_cmap("AsteroidCity1").colors

# Set the background color of the figure
fig_bg_color = "white"
fig.set_facecolor(fig_bg_color)

# Set the background color of the axis
ax_bg_color = "white"
ax.set_facecolor(ax_bg_color)

# Plot the data
ax.plot(x, y1, color=colors[0])
ax.plot(x, y2, color=colors[1])
ax.plot(x, y3, color=colors[2])

# Set a title with colorful annotations
fig_text(
  x=0.5, y=0.975,
  s="An example title for a plot\nwith <linear>, <quadratic> and <cubic> functions.",
  color="black",
  ax=ax, 
  size=12,
  ha="center",
  va="top",
  highlight_textprops=[
    {"color": colors[0], "weight": "bold"},
    {"color": colors[1], "weight": "bold"},
    {"color": colors[2], "weight": "bold"},
  ],
)

# Remove the spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add labels
fig.text(x=0.50, y=0.025, s="x [units]", ha="center", fontsize=10, color="black")
fig.text(x=0.02, y=0.850, s="y [units]", ha="left", fontsize=10, color="black")

# Save the figure
figname = "annotations_solution.png"
plt.savefig(figname)
print(f"open {figname}")
