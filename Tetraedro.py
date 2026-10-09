import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 1. Vértices del Tetraedro
A = (1, 1, 1)
B = (1, -1, -1)
C = (-1, 1, -1)
D = (-1, -1, 1)

caras = [
    [A, B, C],
    [A, B, D],
    [A, C, D],
    [B, C, D]
]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 2. Dibujar Caras
coleccion = Poly3DCollection(caras, alpha=0.5, facecolors='lime', edgecolor='green', linewidth=1.5)
ax.add_collection3d(coleccion)

# 3. Dibujar Vértices y Etiquetas
puntos = {"A": A, "B": B, "C": C, "D": D}
for nombre, (x, y, z) in puntos.items():
    ax.scatter(x, y, z, color='purple', s=70)
    ax.text(x, y, z + 0.15, nombre, fontsize=12)

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_title("Tetraedro Regulación")
plt.show()