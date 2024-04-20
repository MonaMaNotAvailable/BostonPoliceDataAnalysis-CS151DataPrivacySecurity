import pandas as pd
from snsql import Privacy
import snsql
from prettytable import PrettyTable
from example_query import queries
import time
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def execute_privacy_query(query_info):
    pums = pd.read_csv(query_info['csv_path'])
    execute10Times = {}  # Dictionary to hold 10 results for each epsilon

    for epsilon in query_info['epsilon_range']:
        epsilon_results = []  # List to store results of 10 runs for this epsilon
        for i in range(10):  # Repeat 10 times for each epsilon
            print(f"Iteration {i+1} for epsilon {epsilon}")
            privacy = Privacy(epsilon=epsilon, delta=query_info['delta'])
            reader = snsql.from_df(pums, privacy=privacy, metadata=query_info['meta_path'])
            result = reader.execute(query_info['query'])
            print(f"Result for iteration {i+1}: {result[1]}")  # Logging the result
            if 'aggregated_column' in query_info:
                tempSum = display_results(result, query_info['aggregated_column'])
            else:
                tempSum = display_results(result)
            epsilon_results.append(tempSum)  # Append each result to the list
        
        execute10Times[epsilon] = epsilon_results  # Store results of 10 runs for this epsilon
    return execute10Times


def display_results(result, aggregrated_column = 1):
    if isinstance(result[0], list):  # Check if result contains column names
        # Get the value from the first row of data (not the header)
        value = result[1][aggregrated_column]
        return value
    else:
        print("No results to display.")
        return None

def main():

    for query_info in queries:
        plot_execution_data = {}

        results = execute_privacy_query(query_info)
        plot_execution_data[query_info['name']] = results  # Store results for this query

        # Example of how to print the collected data
        for query_name, data in plot_execution_data.items():
            for epsilon, results in data.items():
                print(f"{query_name} for epsilon={epsilon}: {results}")

        # Plot the results
        plot_query_results(plot_execution_data)

def plot_query_results(plot_data):

    for query_name, data in plot_data.items():
        plt.figure(figsize=(10, 8))  # Create a new figure for each query

        # Define a color map
        colors = list(mcolors.TABLEAU_COLORS)  # This will provide a list of color names

        color_index = 0  # Reset color index for each query

        for epsilon, sums in data.items():
            # Ensure the color cycles back to the start if there are more epsilons than colors
            color = colors[color_index % len(colors)]
            color_index += 1

            # Use the same color for scatter and vlines
            plt.scatter([epsilon] * len(sums), sums, alpha=0.7, marker='x', color=color)

            # Draw vertical lines to show the range
            ymin = min(sums)
            ymax = max(sums)
            plt.vlines(x=epsilon, ymin=ymin, ymax=ymax, color=color, linewidth=1)

        plt.title(f'Distribution of {query_name} across Different Epsilons')
        plt.xlabel('Epsilon')
        plt.ylabel('tempSum')
        plt.grid(True)
        plt.tight_layout()

        # Save the figure
        plt.savefig(f"{query_name}.png")
        plt.close()  # Close the figure after saving to free up memory

if __name__ == "__main__":
    main()