import matplotlib.pyplot as plt
import numpy as np


m1, m2 = 120, 100
s1, s2 =  30,  10
x_min  = 75

y1_color = [0, 0.05, 0.5]
y2_color = [0, 0.5, 0.05]


def normal(x, m, s):
    return np.exp(-1/2*((x - m)/s)**2)/(s*np.sqrt(2*np.pi))

m = (m1 + m2)/2
x = np.linspace(0, 2*m, 1000)
x_fail = np.linspace(0, x_min, 1000)
x_diff = np.linspace(-m, m, 10000)
x_best = np.linspace(0, m, 10000)

y1 = normal(x, m1, s1)
y2 = normal(x, m2, s2)
y1_fail = normal(x_fail, m1, s1)
y2_fail = normal(x_fail, m2, s2)
y_diff  = normal(x_diff, m1 - m2, np.sqrt(s1**2 + s2**2))
y_best  = normal(x_best, m1 - m2, np.sqrt(s1**2 + s2**2))

# fig = plt.plot(figsize=(12, 4))
fig = plt.figure(figsize=(6, 4), dpi=80)

plt.plot(x, y1, color=y1_color, label=r"$R_1 \sim$" + " norm" + fr"$\left( {m1}, {s1}^2 \right)$", zorder=20)
plt.fill_between(x_fail, y1_fail, color=y1_color, alpha=0.33, zorder=10)
plt.plot(x, y2, color=y2_color, label=r"$R_2 \sim$" + " norm" + fr"$\left( {m2}, {s2}^2 \right)$", zorder=25)
plt.fill_between(x_fail, y2_fail, color=y2_color, alpha=0.67, zorder=15)
plt.axvline(x=x_min, linestyle='dashed', color='r', alpha=0.5, ymin=0.025, ymax=0.975, label=r"$R_{min} = $" + f"{x_min}", zorder=30)

plt.title(r"$P\left(R_2 < R_{min}\right) \; \ll  \; P\left(R_1 < R_{min}\right)$")
plt.xlabel('Rewards:  ' + r'$R_1, \; R_2$')
plt.ylabel('Probability')
plt.legend()

plt.savefig('image_var.pdf', format='pdf')

plt.show()
