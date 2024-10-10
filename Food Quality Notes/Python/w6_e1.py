# This exercise is meant to be done in MatLab, though for the sake of learning Python, I will do it in both MatLab and Python.

# ------------------------------ Starting imports ------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Set the average height and standard deviation
H_Avg = 180
H_SD = 7.5

# Generate 100,000 random heights
N = 100000
H = np.random.randn(N, 1) * H_SD + H_Avg


# Plot the histogram of the heights and get the counts and bin edges
counts, bin_edges, _ = plt.hist(H, 100, edgecolor='black', linewidth=0.1, alpha=1)

# Add vertical lines for the average and k standard deviations
k = 2  # Number of standard deviations
plt.axvline(H_Avg + k * H_SD, color='red')
plt.axvline(H_Avg - k * H_SD, color='red')

# Add vertical lines at the edges of each bar, excluding the last bin edge
plt.vlines(bin_edges[:-1], 0, counts, colors='k', linestyles='solid', linewidth=0.2, alpha=0.2)

# Set the title of the plot
plt.title(f"Lines are {k} standard deviations")

# Display the plot
plt.show()