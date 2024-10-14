from matplotlib import pyplot as plt
import numpy as np

# Absorption over iron content (mg Fe/50mL) for known samples
# Format is (content, absorption)
known_data: list[tuple[float, float]] = [
    (0.00, 0.000),
    (0.05, 0.202),
    (0.10, 0.426),
    (0.15, 0.628),
    (0.20, 0.820),
    (0.25, 1.021)
]

# Extract scatter data through unpacking via list comprehension
x_data = [datum[0] for datum in known_data]
y_data = [datum[1] for datum in known_data]

# Create plottable points for line of best fit
line_samplepoints = np.linspace(0, 0.3, 2)

# Find line of best fit
line_of_best_fit = np.poly1d(np.polyfit(x_data, y_data, 1))

# Finish up
axes = plt.axes() # Get a handle to the plotter
plt.xlabel("Iron content (mg Fe / 50mL)") # Label x axis
plt.ylabel("Absorption") # Label y axis
plt.plot(line_samplepoints, line_of_best_fit(line_samplepoints), "r") # Plot line of best fit
axes.scatter(x_data, y_data) # Plot scatter data
plt.grid() # Enable plot grid
print(f"{line_of_best_fit.c[1]} absorption per (mg Fe / 50mL)") # Expose polynomial coefficient for x^1
plt.show() # Show the final plot
