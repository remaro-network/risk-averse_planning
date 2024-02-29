import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


m1, m2 = 130, 100
s1, s2 =  45,  25
x1_min  = 120
x2_min = 90

y1_color = [0, 0.05, 0.5]
y2_color = [0, 0.5, 0.05]


def normal(x, m, s):
    return np.exp(-1/2*((x - m)/s)**2)/(s*np.sqrt(2*np.pi))

m = (m1 + m2)/2
x = np.linspace(0, 2*m, 1000)
# x_fail = np.linspace(0, x_min, 1000)
# x_diff = np.linspace(-m, m, 10000)
# x_best = np.linspace(0, m, 10000)
# x_bounded = np.linspace(m1-3*s1, m1+3*s1,10000)
bx1=np.arange(0,m1,10)
bx2=np.arange(0,m2,10)



y1 = normal(x, m1, s1)
y2 = normal(x, m2, s2)
# y1_fail = normal(x_fail, m1, s1)
# y2_fail = normal(x_fail, m2, s2)
# y_diff  = normal(x_diff, m1 - m2, np.sqrt(s1**2 + s2**2))
# y_best  = normal(x_min, m1, np.sqrt(s1**2))
by1 = normal(bx1, m1, s1)
by2 = normal(bx2, m2, s2)

# fig = plt.plot(figsize=(12, 4))
fig = plt.figure(figsize=(6, 4), dpi=80)

plt.plot(x, y1, color=y1_color, label=r"$R_1 \sim$" + " norm" + fr"$\left( {m1}, {s1}^2 \right)$", zorder=20)
plt.fill_between(bx1, by1, color='lightblue', zorder=15)
plt.plot(x, y2, color=y2_color, label=r"$R_2 \sim$" + " norm" + fr"$\left( {m2}, {s2}^2 \right)$", zorder=25)
plt.fill_between(bx2, by2, color='lightgreen', zorder=15)

plt.axvline(x=x2_min, linestyle='dashed', color='g', alpha=0.5, ymin=0.025, ymax=0.975, label=r"$R2_{min} = $" + f"{x2_min}", zorder=30)
plt.axvline(x=x1_min, linestyle='dashed', color='b', alpha=0.5, ymin=0.025, ymax=0.975, label=r"$R1_{min} = $" + f"{x1_min}", zorder=30)

plt.title(r"$P(R_2) \; \ll  \; P(R_1)$")
plt.xlabel('Rewards:  ' + r'$R_1, \; R_2$')
plt.ylabel('Probability')
plt.legend()

plt.savefig('image_var.pdf', format='pdf')

plt.show()
