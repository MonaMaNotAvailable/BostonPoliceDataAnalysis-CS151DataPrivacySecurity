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
    variance = (2 * (sensitivity ** 2)) / (epsilon ** 2)
    # Calculate standard error (standard deviation)
    standard_error = np.sqrt(variance)
    # Calculate the range of expected noisy count
    lower_bound = true_count - 2 * standard_error
    upper_bound = true_count + 2 * standard_error

    print(f"True count: {true_count}")
    print(f"Noisy count: {noisy_count:.2f}")
    print(f"Calculated standard error: {standard_error:.2f}")
    print(f"Expected range of noisy count: ({lower_bound:.2f}, {upper_bound:.2f})")

# Example usage
true_count = [10553]
# sensitivity for differenrt queries, currently its just having the value for query1 
sensitivities = [2406]
epsilon_values = [20, 1]

for epsilon in epsilon_values:
    for sensitivity in sensitivities:
        noisy_count =  #get noisy count from the execute privacy function
        print(f"Using epsilon = {epsilon}")
        evaluate_accuracy(true_count, noisy_count, sensitivity, epsilon)
        print("\n")