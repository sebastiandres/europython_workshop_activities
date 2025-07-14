"""
COLORS:
- How to indicate colors
- Colors in matplotlib themes
- Getting colors from images and websites

TODO:
1. Test different themes from matplotlib: https://matplotlib.org/stable/gallery/color/color_sequences.html
2. Test different themes from pypalettes: https://python-graph-gallery.com/color-palette-finder/
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
from pypalettes import load_cmap
import numpy as np

x = np.linspace(0, 4, 100)
y1 = x # Linear
y2 = x**2 # Squared
y3 = x**3 # Cubed

fig, ax = plt.subplots()

# Choose from:  'tab10', 'tab20', 'tab20b', 'tab20c', 'Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2', 'Set1', 'Set2', 'Set3', 'petroff10'
#colors = mpl.color_sequences["tab20c"]
colors = load_cmap("Acadia").colors

# Set the background color of the figure
fig_bg_color = "lightgray"
fig.set_facecolor(fig_bg_color)

# Set the background color of the axis
ax_bg_color = "white"
ax.set_facecolor(ax_bg_color)

# Plot the data
ax.plot(x, y1, color=colors[0])
ax.plot(x, y2, color=colors[1])
ax.plot(x, y3, color=colors[2])

# Plot the text
ax.text(x=x[-1], y=y1[-1], s="Linear ", color=colors[0], ha="right")
ax.text(x=x[-1], y=y2[-1], s="Squared ", color=colors[1], ha="right")
ax.text(x=x[-1], y=y3[-1], s="Cubed ", color=colors[2], ha="right")

# Set the title
fig.text(x=0.5, y=0.95, s="Linear, Squared and Cubed", ha="center", fontsize=16, color="black")

# Add labels
fig.text(x=0.50, y=0.025, s="x [units]", ha="center", fontsize=10, color="black")
fig.text(x=0.02, y=0.850, s="y [units]", ha="left", fontsize=10, color="black")

# Save the figure
figname = "colors_solution.png"
plt.savefig(figname)
print(f"open {figname}")
