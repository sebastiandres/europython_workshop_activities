"""
Mixed bag of tricks:
- ax vs fig: how to use them
- Avoid the plot bounding box: splines
- Ticks: how to control them
- Alpha: how to control the transparency of elements
- zorder: to control the order of elements
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [1, 4, 9, 16]
y3 = [1, 8, 27, 64]
colors = ["#476F84", "#A4BED5", "#72874E"]

fig, ax = plt.subplots()

ax.plot(x, y1, color=colors[0], lw=4, zorder=3, alpha=0.25)
ax.plot(x, y2, color=colors[1], lw=4, zorder=2, alpha=0.5)
ax.plot(x, y3, color=colors[2], lw=4, zorder=1, alpha=0.75)
ax.spines[["top", "right"]].set_visible(False)

# Annotate the last point of each line
ax.text(x=4.1, y=y1[-1], s="Linear", color=colors[0], weight="bold")
ax.text(x=4.1, y=y2[-1], s="Squared", color=colors[1], weight="bold")
ax.text(x=4.1, y=y3[-1], s="Cubed", color=colors[2], weight="bold")
plt.show()

# TODO:
# Explain ax vs fig (on text)
# Explain splines
# Explain ticks

plt.savefig("figures/02A_mixed_bag.png")