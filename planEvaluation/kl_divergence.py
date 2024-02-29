import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt
# import tensorflow as tf
import seaborn as sns
# sns.set()

def kl_divergence(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))

def normal(x, m, s):
    return np.exp(-1/2*((x - m)/s)**2)/(s*np.sqrt(2*np.pi))

# x = np.arange(-10, 10, 0.001)
# print(x)
m1, m2 = 120, 100
s1, s2 =  30,  10
x_min  = 75

y1_color = [0, 0.05, 0.5]
y2_color = [0, 0.5, 0.05]

m = (m1 + m2)/2
x = np.linspace(0, 2*m, 1000)
x_fail = np.linspace(0, x_min, 1000)

# p = norm.pdf(x, m1, s1)
# q = norm.pdf(x, m2, s2)
# plt.title('KL(P||Q) = %1.3f' % kl_divergence(p, q))
# plt.plot(x, p)
# plt.plot(x, q, c='red')

y1 = normal(x, m1, s1)
y2 = normal(x, m2, s2)
y1_fail = normal(x_fail, m1, s1)
y2_fail = normal(x_fail, m2, s2)

plt.plot(x, y1, color=y1_color, label=r"$R_1 \sim$" + " norm" + fr"$\left( {m1}, {s1}^2 \right)$", zorder=20)
# plt.fill_between(x_fail, y1_fail, color=y1_color, alpha=0.33, zorder=10)
plt.plot(x, y2, color=y2_color, label=r"$R_2 \sim$" + " norm" + fr"$\left( {m2}, {s2}^2 \right)$", zorder=25)
# plt.fill_between(x_fail, y2_fail, color=y2_color, alpha=0.67, zorder=15)
plt.title('KL(' +r'$R_1 || R_2$'+') = %1.3f' % kl_divergence(y1, y2))
plt.xlabel('Rewards:  ' + r'$R_1, \; R_2$')
plt.ylabel('Probability')
plt.legend()

plt.savefig('image_var.pdf', format='pdf')
