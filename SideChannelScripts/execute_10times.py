import pandas as pd
from snsql import Privacy
import snsql
import time
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from example_query import queries
import numpy as np
import random
plt.rcParams.update({'font.size': 20})

rangeVal = 10

def execute_privacy_query(query_info):
    pums = pd.read_csv(query_info['csv_path'])
    execute_times = {}  # Dictionary to hold execution times for each epsilon

    for epsilon in query_info['epsilon_range']:
        epsilon_times = []  # List to store execution times of 10 runs for this epsilon
        for i in range(rangeVal):
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
        for i in range(rangeVal):
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
    plt.figure(figsize=(10, 8))

    # Get unique colors for each query
    colors = list(mcolors.TABLEAU_COLORS)

    for _, (query_name, data) in enumerate(plot_data.items()):

        for method_index, (method, results) in enumerate(data.items()):
            x_axis = (method_index+2)/2
            print(x_axis)
            color = colors[method_index % len(colors)]
            mean_time = np.mean(results)
            min_time = min(results)
            max_time = max(results)
            for times in results:
                plt.scatter(x_axis, times, alpha=0.5, color=color)
            # Plot overall mean time, adjusting the position
            plt.scatter(x_axis, mean_time, color=color, edgecolors='black', label=f'{method} - mean: {mean_time:.2f}s')
            # Draw vertical line for the overall mean time, adjusting the position
            plt.vlines(x_axis, ymin=min_time, ymax=max_time, color=color, linestyle='-', linewidth=2)

    # Adjust the ticks to center them between the methods
    plt.xticks([])
    plt.title('Execution Time Comparison of Queries With and Without Delay')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.xlim(0, 3)
    # plt.ylim(2, 4)
    plt.show()

def main():
    plot_execution_data = {}

    for query_info in queries:
        results_no_delay = execute_privacy_query(query_info)
        results_with_delay = execute_privacy_query_with_delay(query_info)

        # Merge results to compare
        for epsilon in query_info['epsilon_range']:
            plot_execution_data[query_info['name']] = {
                'No Delay': results_no_delay[epsilon],
                'With Delay': results_with_delay[epsilon]
            }
    
    plot_query_results(plot_execution_data)

if __name__ == "__main__":
    main()