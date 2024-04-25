import pandas as pd
from snsql import Privacy
import snsql
import time
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from example_query import queries
import numpy as np
import random

def execute_privacy_query(query_info):
    pums = pd.read_csv(query_info['csv_path'])
    execute_times = {}  # Dictionary to hold execution times for each epsilon

    for epsilon in query_info['epsilon_range']:
        epsilon_times = []  # List to store execution times of 10 runs for this epsilon
        for i in range(20):
            print(f"Iteration {i+1} for epsilon {epsilon}")
            start_time = time.time()  # Start time
            privacy = Privacy(epsilon=epsilon, delta=query_info['delta'])
            reader = snsql.from_df(pums, privacy=privacy, metadata=query_info['meta_path'])
            reader.execute(query_info['query'])
            execution_time = time.time() - start_time  # Execution time
            epsilon_times.append(execution_time)
        
        execute_times[epsilon] = epsilon_times
    return execute_times

def execute_privacy_query_with_delay(query_info):
    pums = pd.read_csv(query_info['csv_path'])
    execute_times = {}  # Dictionary to hold execution times for each epsilon

    for epsilon in query_info['epsilon_range']:
        epsilon_times = []  # List to store execution times of 10 runs for this epsilon
        for i in range(20):
            print(f"Iteration {i+1} for epsilon {epsilon}")
            start_time = time.time()  # Start time
            privacy = Privacy(epsilon=epsilon, delta=query_info['delta'])
            reader = snsql.from_df(pums, privacy=privacy, metadata=query_info['meta_path'])
            reader.execute(query_info['query'])
            # Introduce a random delay to mitigate timing attacks
            random_delay = random.uniform(0.1, 0.5)  # Random delay between 0.1 and 0.5 seconds
            time.sleep(random_delay)
            execution_time = time.time() - start_time + random_delay # Execution time
            epsilon_times.append(execution_time)
        
        execute_times[epsilon] = epsilon_times
    return execute_times

def plot_query_results(plot_data):
    plt.figure(figsize=(10, 8))  # Single figure for all queries
    colors = list(mcolors.TABLEAU_COLORS)  # Color map
    color_index = 0  # Color index for distinguishing different queries

    for query_name, data in plot_data.items():
        color = colors[color_index % len(colors)]  # Assign a color
        color_index += 1
        
        for epsilon, times in data.items():
            mean_time = np.mean(times)  # Calculate the mean execution time
            plt.scatter([epsilon] * len(times), times, alpha=0.7, marker='x', color=color)
            plt.scatter(epsilon, mean_time, color=color, edgecolors='black', label=f'{query_name} ε={epsilon} mean: {mean_time:.2f}s', zorder=5)
        
    plt.title('Execution Time of Queries Across Different Epsilons')
    plt.xlabel('Epsilon')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # Save the figure
    plt.savefig(f"{query_name}.png")
    plt.close()  # Close the figure after saving to free up memory

def main():
    plot_execution_data = {}

    for query_info in queries:
        # results = execute_privacy_query(query_info)
        results = execute_privacy_query_with_delay(query_info)
        plot_execution_data[query_info['name']] = results
        print(plot_execution_data)

    plot_query_results(plot_execution_data)

if __name__ == "__main__":
    main()