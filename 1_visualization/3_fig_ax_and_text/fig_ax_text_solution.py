"""
FIG, AX, TEXT:
- fig: Always ranges from 0 to 1 (for both x and y)
- ax: Ranges from the data limits
- text: Can be used for fig or ax. Serves to annotate the plot.

TODO:
1. Set the background color of the figure (lightgray)
2. Set the background color of the axis (lightblue)
3. Plot a text on the top center of the figure, as a title
4. Plot a text on the bottom right of the figure, to indicate each type of line
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4, 100)
y1 = x # Linear
y2 = x**2 # Squared
y3 = x**3 # Cubed

fig, ax = plt.subplots()

# Set the background color of the figure
fig_bg_color = "lightgray"
fig.set_facecolor(fig_bg_color)

# Set the background color of the axis
ax_bg_color = "lightblue"
ax.set_facecolor(ax_bg_color)

# Plot the data
ax.plot(x, y1, color="red")
ax.plot(x, y2, color="blue")
ax.plot(x, y3, color="green")

# Plot the text
ax.text(x=x[-1], y=y1[-1], s="Linear ", color="red", ha="right")
ax.text(x=x[-1], y=y2[-1], s="Squared ", color="blue", ha="right")
ax.text(x=x[-1], y=y3[-1], s="Cubed ", color="green", ha="right")

# Set the title
fig.text(x=0.5, y=0.95, s="Linear, Squared and Cubed", ha="center", fontsize=16, color="black")

# Add labels
fig.text(x=0.50, y=0.025, s="x [units]", ha="center", fontsize=10, color="black")
fig.text(x=0.02, y=0.850, s="y [units]", ha="left", fontsize=10, color="black")

# Save the figure
figname = "fig_ax_text_solution.png"
plt.savefig(figname)
print(f"open {figname}")
