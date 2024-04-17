# Exact count of total number of allegations raised in different neighborhoods - 4139
# Exact or original count of total number of allegations raised for different category or type of allegations - 10553
import numpy as np
def evaluate_accuracy(true_count, noisy_count, sensitivity, epsilon):
    """
    Evaluates the accuracy of the noisy count.

    Parameters:
        true_count (int): The actual count of the data.
        noisy_count (float): The count after adding noise.
        sensitivity (int): The sensitivity of the query.
        epsilon (float): The privacy budget.
    """
    # Calculate variance
    variance = (2 * (sensitivity ** 2)) / (epsilon ** 2) # 2 *
    # Calculate standard error (standard deviation)
    standard_error = np.sqrt(variance)
    # Calculate the range of expected noisy count
    # lower_bound = true_count - 2 * standard_error
    # upper_bound = true_count + 2 * standard_error

    print(f"True count: {true_count}")
    print(f"Noisy count: {noisy_count:.2f}")
    print(f"Calculated standard error: {standard_error:.2f}")
    # print(f"Expected range of noisy count: ({lower_bound:.2f}, {upper_bound:.2f})")

if __name__ == "__main__":
    # Example usage
    true_count = 4139
    sensitivity = 1051
    epsilon_values = [92]
    noisy_count = 4075

    for epsilon in epsilon_values:
            print(f"Using epsilon = {epsilon}")
            evaluate_accuracy(true_count, noisy_count, sensitivity, epsilon)
            print("\n")