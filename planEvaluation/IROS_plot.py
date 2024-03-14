import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats



# Given data
planned_time = np.array([0.068, 0.094, 0.070, 0.073, 0.059])

planned_time = np.array([3, 5, 6]) #dangerous, #safest,
planned_time = np.array([3, 5, 6, 4, 5]) #dangerous, #safest, out of battery, other1 (longer & dangerous), other2 (longer & dangerous)


simulated_time = np.array([
   [139.01 + 110 + 80 , 139.8 + 110.4 + 81.1, 138.9 + 115.5 + 82.1, 139.8 + 120.6 + 81, 137.7 + 111 + 80.4, \
      140.6 + 110.7 + 81.7, 139.23 + 110.4 + 81.03, 138.6 + 111 + 80.3, 138.8 + 110.6 + 80.6, 140.4 + 109.8 + 80.9],
   [139.01 + 77 + 80, 139.8 + 77.6 + 81.1, 138.9 + 76.8 + 82.0, 139.8 + 76.9 + 81, 137.7 + 76.8 + 80.3,\
      140.6 + 76.8 +  81.7, 139.23 + 76.34 + 81.03, 138.6 + 77.1 + 80.3, 138.8 + 77.0 + 80.6, 140.4 + 76.8 + 80.9],
   [55 + 57 + 240, 54.6 + 57 + 239.7, 55.1 + 56.8 + 240, 54.7 + 57.2 + 239.9, 55.3 + 57.1 + 240.2, \
    55.01 + 56.9 + 240.6, 54.6 + 56.9 + 239.6, 54.9 + 57.1 + 240.2, 55.3 + 56.9 + 239.8, 55.1 + 55.7 + 240.2],
   [55 + 240, 54.8 + 239.9, 55 + 239.7, 54.6 + 240, 55.2 + 239.7,\
    55.6 + 239.7, 54.1 + 239.6, 54.2 + 238.9, 55.1 + 240.2, 55.1 + 240.3],
   [31.9+ 33 + 239.8, 32.1 + 32.9 + 240.2, 32.5 + 32.9 + 239.4, 32.3+ 33.1 + 240, 31.7 + 33.4 + 240.4,\
     32.2 + 32.8 + 239.8, 32.1+ 32.9 + 239.7, 31.8 + 33 + 239.3, 32 + 33.3 + 240.4, 31.8 + 32.9 + 240.6]
         ])


# convert to minutes
#simulated_time = simulated_time*60
#planned_time = planned_time*60

# Calculate the mean and standard deviation for each plan's simulated times
mean_simulated_time = np.mean(simulated_time, axis=1)
std_dev_simulated_time = np.std(simulated_time, axis=1)
entropy_simulated_time = scipy.stats.entropy(simulated_time, axis=1)
variance_simulated_time = np.var(simulated_time, axis=1)

for m, v, e in zip(mean_simulated_time, variance_simulated_time, entropy_simulated_time):
   print (m, v, e)

# Plotting
f, ax = plt.subplots(figsize=(4, 3))
plt.errorbar(
    planned_time, 
    mean_simulated_time, yerr=std_dev_simulated_time, 
    fmt='o', 
    color = 'k',
    ecolor='k', 
    markersize = 2,
    capsize=4, 
    lw = 0.5, 
    linestyle='None', 
    label='Simulated Time')
print(mean_simulated_time)

i = 1
for xy in zip(planned_time, mean_simulated_time): 
    x,y = xy
    if x==6:
       xytext = (-20, -4)
    else:  
      xytext = (10,-4)                                   
    ax.annotate('$P_%s$' % i, xy=xy, xytext=xytext, textcoords='offset points') 
    i += 1

#ax.set_xticks(planned_time)
#ax.set_yticks(mean_simulated_time)

plt.gcf().text(0.195, 0.08, "(109)", fontsize=10)
# plt.gcf().text(0.6, 0.08, "(114)", fontsize=10)
plt.gcf().text(0.88, 0.08, "(115)", fontsize=10)
plt.gcf().text(0.43, 0.08, "(112)", fontsize=10)
plt.gcf().text(0.66, 0.08, "(114)", fontsize=10)

# cut off too long numbers
# ax.yaxis.set_major_formatter('{x:0<3.0f}')
# ax.xaxis.set_major_formatter('{x:0<1.0f}')


# add some padding
plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)

#ax.yaxis.tick_right()
plt.xticks(planned_time)

# Add x = y line
#plt.plot(planned_time, planned_time, 'k:', lw = 0.3, label='Expected Time')

plt.xlabel('Plan Length')
plt.ylabel('Simulated Execution Time')
plt.title('Execution Time of Different Plans')
#plt.legend()
plt.show()
