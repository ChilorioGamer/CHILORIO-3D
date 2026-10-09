import matplotlib.pyplot as plt
import numpy as np

# 1. Generar coordenadas paramétricas para el Cilindro
z = np.linspace(0, 3, 30)
theta = np.linspace(0, 2 * np.pi, 30)
theta_grid, z_grid = np.meshgrid(theta, z)

radio = 1.5
x_grid = radio * np.cos(theta_grid)
y_grid = radio * np.sin(theta_grid)

# 2. Configurar gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 3. Dibujar Malla de Superficie (Cuerpo del cilindro)
ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.6, cmap='Blues', edgecolor='navy', linewidth=0.3)

# Dibujar anillos límite (aristas de base y tapa)
ax.plot(x_grid[0], y_grid[0], z_grid[0], color='darkblue', linewidth=2)
ax.plot(x_grid[-1], y_grid[-1], z_grid[-1], color='darkblue', linewidth=2)

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-0.5, 3.5)
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")
ax.set_title("Cilindro 3D")
plt.show()