import numpy as np
import matplotlib.pyplot as plt

# Execution times (in microseconds)

#execution_times = [
#    123, 24, 21, 20, 20, 20, 22, 20, 30, 44, 20, 20, 15, 14, 18, 12, 13, 11, 13, 11
#]

#execution_times = [
#    235, 94, 78, 24, 21, 55, 44, 23, 20, 20, 19, 23, 26, 23, 39, 24, 20, 20, 20, 20
#]

execution_times = [
    166338, 235351, 167130, 171230, 172221, 166416, 169773, 238198, 234800, 266876, 
    256917, 168645, 166132, 177233, 174194, 238387, 168821, 338898, 206388, 166164
]

execution_times = [
    202577, 208096, 149550, 564318, 203360, 146148, 165605, 337631, 187515, 190775, 
    146799, 158047, 206540, 201915, 149494, 146329, 320729, 204567, 308517, 146052
]

# Calculate Q1, Q3, and IQR
Q1 = np.percentile(execution_times, 25)
Q3 = np.percentile(execution_times, 75)
IQR = Q3 - Q1

# Determine outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
filtered_times = [time for time in execution_times if lower_bound <= time <= upper_bound]

# Calculate mean and standard deviation for filtered data
mean_time = np.mean(filtered_times)
std_dev_time = np.std(filtered_times)

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.boxplot(filtered_times, vert=False)
plt.title(f"Execution Time Boxplot\nMean: {mean_time:.2f} us | Std Dev: {std_dev_time:.2f} us")
plt.xlabel("Execution Time (us)")
plt.show()

