import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ============================
# 1. DEFINIR LOS VÉRTICES
# ============================

A = (1,1,1)
B = (3,1,1)
C = (3,3,1)
D = (1,3,1)
E = (1,1,3)
F = (3,1,3)
G = (3,3,3)
H = (1,3,3)

vertices = [A, B, C, D, E, F, G, H]

# ============================
# 2. CREAR LA FIGURA 3D
# ============================

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ============================
# 3. DIBUJAR LA CARA
# ============================

cara = Poly3DCollection(
    [vertices],
    alpha=0.4,
    edgecolor="black"
)

ax.add_collection3d(cara)

# ============================
# 4. DIBUJAR LOS VÉRTICES
# ============================

for nombre, vertice in zip(["A", "B", "C", "D", "E", "F", "G", "H"], vertices):

    x, y, z = vertice

    ax.scatter(x, y, z, s=80)

    ax.text(
        x,
        y,
        z + 0.1,
        nombre,
        fontsize=12
    )

# ============================
# 5. DIBUJAR LAS ARISTAS
# ============================

aristas = [
    (A, B),
    (B, C),
    (C, D),
    (D, A),
    (B, F),
    (A, E),
    (D, H),
    (C, G)
]

for inicio, fin in aristas:

    ax.plot(
        [inicio[0], fin[0]],
        [inicio[1], fin[1]],
        [inicio[2], fin[2]],
        linewidth=2
    )

# ============================
# 6. CONFIGURAR LA ESCENA
# ============================

ax.set_xlim(-1, 5)
ax.set_ylim(-1, 4)
ax.set_zlim(-1, 2)

ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")

ax.set_title(
    "Cuadrado formado por vértices, aristas y una cara"
)

plt.show()