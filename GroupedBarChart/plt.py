# Import Library
import matplotlib.pyplot as plt
import numpy as np

# === Codes ===
species = ("Adellie","Chinstrap","Guntur")
penguins_means = {
    'Bill Depth': (18.35,18.43,14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length':(189.96, 195.82, 217.89),
}

x = np.arange(len(species))
width = 0.25
multiplier = 1

fig,ax = plt.subplots(layout="constrained")
for attribute, measurement in penguins_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects,padding=3)
    multiplier += 1

ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc="upper left",ncols=3)
ax.set_ylim(0,250)
plt.show()
# === EndCOdes ===