import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()

ax1 = fig.add_subplot(1, 1, 1)
ax1.set_facecolor('orange')
ax2 = fig.add_axes([0.5, 0.5, 0.3, 0.3])

t = np.arange(0, 1, 0.01)
s = np.sin(t)

ax2.plot(t, s, linewidth=2)
ax2.patch.set_alpha(0.01)

plt.show()