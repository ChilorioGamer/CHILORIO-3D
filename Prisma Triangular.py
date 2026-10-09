import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 1. Vértices (Triángulo Inferior vs Triángulo Superior)
A = (0, 0, 0)
B = (2, 0, 0)
C = (1, 1.73, 0)

D = (0, 0, 3)
E = (2, 0, 3)
F = (1, 1.73, 3)

caras = [
    [A, B, C],  # Base inferior
    [D, E, F],  # Base superior
    [A, B, E, D], # Cara lateral 1
    [B, C, F, E], # Cara lateral 2
    [C, A, D, F]  # Cara lateral 3
]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

coleccion = Poly3DCollection(caras, alpha=0.4, facecolors='purple', edgecolor='black', linewidth=1.5)
ax.add_collection3d(coleccion)

vertices = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F}
for nombre, (x, y, z) in vertices.items():
    ax.scatter(x, y, z, color='black', s=50)
    ax.text(x, y, z + 0.1, nombre, fontsize=11)

ax.set_xlim(-1, 3)
ax.set_ylim(-1, 3)
ax.set_zlim(-0.5, 3.5)
ax.set_title("Prisma Triangular")
plt.show()