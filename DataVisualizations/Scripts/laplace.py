import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import laplace

# Increase the overall font size
plt.rcParams.update({'font.size': 16})  # Adjust the size as needed

# Set up the mean and calculate sigmas from variances
mean = 59 
variance_1 = 1706.20527399
epsilon_1 = 2.02
sigma_1 = np.sqrt(variance_1 / 2)

variance_2 = 69.62
epsilon_2 = 10
sigma_2 = np.sqrt(variance_2 / 2)

# Set the range for x based on the larger sigma to ensure both distributions are visible
x_range = max(sigma_1, sigma_2)
x = np.linspace(mean - 4*x_range, mean + 4*x_range, 1000)

# Generate the y values for both distributions
y_1 = laplace.pdf(x, loc=mean, scale=sigma_1)
y_2 = laplace.pdf(x, loc=mean, scale=sigma_2)

# Plotting the Laplace distributions
plt.figure(figsize=(12, 6))
# plt.plot(x, y_1, label=f'Variance = {variance_1}, Epsilon = {epsilon_1}', color='pink')
plt.plot(x, y_2, label=f'Variance = {variance_2}, Epsilon = {epsilon_2}', color='magenta')
plt.axvline(mean, color='purple', linestyle='--', label=f'Mean = {mean}')
plt.title('Laplace Distributions')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()