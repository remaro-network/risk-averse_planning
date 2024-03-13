import numpy as np
import matplotlib.pyplot as plt

# Given data
planned_time = np.array([3, 5, 6, 4, 5]) #dangerous, #safest, out of battery, other1, other2

simulated_time = np.array([
   [139.01 + 110 + 80 , 139.8 + 110.4 + 81.1, 138.9 + 115.5 + 82.1, 139.8 + 120.6 + 81, 137.7 + 111 + 80.4, \
      140.6 + 110.7 + 81.7, 139.23 + 110.4 + 81.03, 138.6 + 111 + 80.3, 138.8 + 110.6 + 80.6, 140.4 + 109.8 + 80.9],
   [139.01 + 77 + 80, 139.8 + 77.6 + 81.1, 138.9 + 76.8 + 82.0, 139.8 + 76.9 + 81, 137.7 + 76.8 + 80.3,\
      140.6 + 76.8 +  81.7, 139.23 + 76.34 + 81.03, 138.6 + 77.1 + 80.3, 138.8 + 77.0 + 80.6, 140.4 + 76.8 + 80.9],
   [55 + 57 + 140, 54.6 + 57 + 139.7, 55.1 + 56.8 + 140, 54.7 + 57.2 + 139.9, 55.3 + 57.1 + 140.2, \
    55.01 + 56.9 + 140.6, 54.6 + 56.9 + 139.6, 54.9 + 57.1 + 140.2, 55.3 + 56.9 + 139.8, 55.1 + 55.7 + 140.2],
   [139.01 + 77 + 80, 139.8 + 77.6 + 81.1, 138.9 + 76.8 + 82.0, 139.8 + 76.9 + 81, 137.7 + 76.8 + 80.3,\
      140.6 + 77 + 81.7, 139.23 + 77.6 + 81.1, 138.6 + 76.8 + 82.0, 138.8 + 76.9 + 81, 140.4 + 76.8 + 80.3],
   [139.01 + 77 + 80, 139.8 + 77.6 + 81.1, 138.9 + 76.8 + 82.0, 139.8 + 76.9 + 81, 137.7 + 76.8 + 80.3,\
      140.6 + 77 + 80, 139.23 + 77.6 + 81.1, 138.6 + 76.8 + 82.0, 138.8 + 76.9 + 81, 140.4 + 76.8 + 80.3]
         ])

# Calculate the mean and standard deviation for each plan's simulated times
mean_simulated_time = np.mean(simulated_time, axis=1)
std_dev_simulated_time = np.std(simulated_time, axis=1)

# Plotting
plt.figure(figsize=(6, 4))
plt.errorbar(
    planned_time, 
    mean_simulated_time, yerr=std_dev_simulated_time, 
    fmt='o', 
    color = 'k',
    ecolor='k', 
    markersize = 3,
    capsize=2, 
    lw = 0.5, 
    linestyle='None', 
    label='Simulated Time')

# Add x = y line
plt.plot(planned_time, planned_time, 'k:', lw = 0.3, label='Expected Time')

plt.xlabel('Expected Running Time for a Robot Plan')
plt.ylabel('Simulated Running Time for a Robot Plan')
plt.title('Scatter plot of Expected vs. Simulated Running Time')
plt.legend()
plt.show()