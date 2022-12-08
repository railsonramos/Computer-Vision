import numpy as np
import matplotlib.pyplot as plt
wt = 800000000
lamb = 299792458/wt
dis_max = 400000

d = range(dis_max)
for i in range(dis_max):
    wr_el= -10*np.log10(wt)-20*np.log10(lamb)+20*np.log10(i)+20*np.log10(4*np.pi)

fig, ax = plt.subplots()  # inicializa Figure e Axes
ax.plot(d, wr_el,marker='o')
plt.xticks(range(0,dis_max+1))
plt.yticks(range(0, 1000000000000+1, 10))
plt.title("Gaussian Noise")
plt.xlabel("Deg_Level")
plt.ylabel("Accuracy(%)")
plt.legend(['Sem restauração', 'Com restauração'], loc='best')


plt.show()