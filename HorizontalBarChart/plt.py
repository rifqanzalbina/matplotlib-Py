# Library Import 
import matplotlib.pyplot as plt
import numpy as np

# === Codes ===
np.random.seed(1968080123)

plt.rcdefaults()
fig, ax = plt.subplots()

people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance,xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()
ax.set_xlabel('Performance')
ax.set_title("How Fast do you want to go today?")
plt.show()
# === EndCodes ===