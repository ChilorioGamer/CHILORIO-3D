import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 1. Definir Vértices del Cubo
vertices = {
    'A': (0, 0, 0), 'B': (2, 0, 0), 'C': (2, 2, 0), 'D': (0, 2, 0),
    'E': (0, 0, 2), 'F': (2, 0, 2), 'G': (2, 2, 2), 'H': (0, 2, 2)
}

# Definición de las 6 caras
caras = [
    [vertices['A'], vertices['B'], vertices['C'], vertices['D']], # Inferior
    [vertices['E'], vertices['F'], vertices['G'], vertices['H']], # Superior
    [vertices['A'], vertices['B'], vertices['F'], vertices['E']], # Frontal
    [vertices['C'], vertices['D'], vertices['H'], vertices['G']], # Trasera
    [vertices['A'], vertices['D'], vertices['H'], vertices['E']], # Izquierda
    [vertices['B'], vertices['C'], vertices['G'], vertices['F']]  # Derecha
]

# 2. Crear la escena 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 3. Dibujar Caras
coleccion = Poly3DCollection(caras, alpha=0.3, facecolors='cyan', edgecolor='black', linewidth=1.5)
ax.add_collection3d(coleccion)

# 4. Dibujar Vértices y Nombres
for nombre, (x, y, z) in vertices.items():
    ax.scatter(x, y, z, color='red', s=50)
    ax.text(x, y, z + 0.1, nombre, fontsize=10)

# Configurar vista
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 3)
ax.set_zlim(-1, 3)
ax.set_title("Cubo 3D")
plt.show()