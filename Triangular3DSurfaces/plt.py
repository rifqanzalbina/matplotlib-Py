# Import Library
import matplotlib.pyplot as plt
import numpy as np

# === Codes ===
n_radii = 8
n_angles = 36

radii = np.linspace(0.125,1.0,n_radii)
angles = np.linspace(0,2*np.pi,n_angles,endpoint=False)[...,np.newaxis]

x = np.append(0,(radii*np.cos(angles)).flatten())
y = np.append(0,(radii*np.sin(angles)).flatten())

z = np.sin(-x*y)
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x,y,z,linewidth=0.2,antialiased=True)
plt.show()
# === EndCodes ===