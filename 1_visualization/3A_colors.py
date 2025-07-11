"""
Colors:

- ax.facecolor, fig.facecolor
- Colors in matplotlib
- Themes
- Stealing colors from an image
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [1, 4, 9, 16]
y3 = [1, 8, 27, 64]

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
plt.show()

