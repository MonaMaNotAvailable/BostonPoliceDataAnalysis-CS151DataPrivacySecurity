# Exact count of total number of allegations raised in different neighborhoods - 4139
# Exact or original count of total number of allegations raised for different category or type of allegations - 10553
import numpy as np
import matplotlib.pyplot as plt

def evaluate_accuracy(sensitivity, epsilon):
    """
    Evaluates the accuracy of the noisy count.

    Parameters:
        sensitivity (int): The sensitivity of the query.
        epsilon (float): The privacy budget.
    """
    # Calculate variance
    variance = (2 * (sensitivity ** 2)) / (epsilon ** 2)
    # Calculate standard error (standard deviation)
    standard_error = np.sqrt(variance)
    print(f"Calculated standard error: {standard_error:.2f}")
    return(standard_error)

def plot_standard_errors(epsilons, errors):
    """
    Plots the epsilon values against their corresponding standard errors.

    Parameters:
        epsilons (list of float): The epsilon values.
        errors (list of float): The corresponding standard errors.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(epsilons, errors, marker='o', linestyle='-', color='violet',)
    plt.title('Query 5: Shootings Count by Neighborhood -- Standard Error vs Epsilon')
    plt.xlabel('Epsilon')
    plt.ylabel('Standard Error')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Example usage
    # true_count = 4139
    sensitivity = 59 #808 #365001 #59 #1051 #2406
    start =  0.05#100 #9 #0.05 #0.1 #1.0
    end =  3.0#500 #60 #3.0 #4.0 #5.0         50/5 -> 10
     # Generating 10 points from 92 to 1486

    epsilon_values = np.linspace(start, end, 10, dtype=float).tolist()   #[0.01, 0.1, 0.5]
    standard_errors = []

    for epsilon in epsilon_values:
            print(f"Using epsilon = {epsilon}")
            error = evaluate_accuracy(sensitivity, epsilon)
            standard_errors.append(error)
            print("\n")

    # print(evaluate_accuracy(59, 3))
    # print(evaluate_accuracy(59, 0.05))
    # print(evaluate_accuracy(59, 2.02))
    # print(evaluate_accuracy(59, 40))
    # print(evaluate_accuracy(59, 10))
    
    # Plot the results
    plot_standard_errors(epsilon_values, standard_errors)
    print(epsilon_values)
