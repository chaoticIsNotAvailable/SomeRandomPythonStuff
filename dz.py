
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = [1,2,3,1,3,2]
x = np.array([1,2,3,1,3,2])
x = pd.Series(np.array([1,2,3,1,3,2]))

plt.figure(figsize=(8,4))
plt.plot(x, linewidth=2, color='green', marker='*', linestyle='dashed', label='line_1')
plt.legend()
plt.grid(color='gray', linestyle='-', linewidth=1.5)
plt.yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5,5])
plt.xticks()
plt.xlabel('Ось абсцисс')
plt.ylabel('Ось ординат')
plt.show()

