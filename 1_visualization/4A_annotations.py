"""

# Anotaciones

Las anotaciones son esenciales: permiten dar contexto, enfasis, y guiar la interpretación del lector. Permiten dar contexto y anotar solo algunos casos y outliers que queremos que destaquen.

Opciones en matplotlib:
- `ax.text()` y `fig.text()`: anotaciones generales
- `plt.title()` y `ax.set_title()`: titulos
- `ax.set_xlabel()` y `ax.set_ylabel()`: para los nombres de los ejes
- `ax.annotate()` para combinar texto con flechas!!!

Strong opinion: use only `ax.text` and `fig.text`. It's all you need, they encompass the other methods.

Notas personales:
- No es claro cómo realiza la rotación.
- Propiedades del bbox se deben pasar en un diccionario aparte.
- La posición del texto se indica respecto al texto, no al bounding box.

"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [3, 2, 1])

ax.text(x=2, y=1, s="An annotation", size=12, color="black", ha="left")
ax.text(x=1.5, y=1.5, s="Another annotation", size=14, color="#AA3388", ha="center")

# Or with unpacking
text_style = dict(size=14, color="red", ha="right")
ax.text(x=2, y=3, s="And last annotation", **text_style)

plt.show()