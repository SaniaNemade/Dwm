#data visualization
import matplotlib.pyplot as plt

data = [4,8,15,21,21,24,25,28,34]

# Plotting a histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=10, edgecolor='k', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)

# Displaying the histogram
#plt.show()

# Plotting a scatter plot
x = list(range(1, len(data) + 1))
plt.figure(figsize=(8, 5))
plt.scatter(x, data, c='b', marker='o', label='Data Points')
plt.title('Scatter Plot')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)

# Displaying the scatter plot
plt.legend()
plt.show()


