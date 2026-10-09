import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 1. Vértices
A = (-1, -1, 0)
B = (1, -1, 0)
C = (1, 1, 0)
D = (-1, 1, 0)
P = (0, 0, 2)  # Cúspide de la pirámide

vertices = [A, B, C, D, P]

# 2. Caras (Base + 4 Caras Triangulares)
caras = [
    [A, B, C, D], # Base
    [A, B, P],    # Cara 1
    [B, C, P],    # Cara 2
    [C, D, P],    # Cara 3
    [D, A, P]     # Cara 4
]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 3. Dibujar Caras
coleccion = Poly3DCollection(caras, alpha=0.4, facecolors='orange', edgecolor='darkred', linewidth=1.5)
ax.add_collection3d(coleccion)

# 4. Dibujar Vértices
nombres = ["A", "B", "C", "D", "P"]
for nombre, (x, y, z) in zip(nombres, vertices):
    ax.scatter(x, y, z, color='blue', s=60)
    ax.text(x, y, z + 0.1, nombre, fontsize=11)

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-0.5, 2.5)
ax.set_title("Pirámide de Base Cuadrada")
plt.show()