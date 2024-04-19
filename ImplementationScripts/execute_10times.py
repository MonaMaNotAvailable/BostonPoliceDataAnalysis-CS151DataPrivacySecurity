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
        for _ in range(10):  # Repeat 10 times for each epsilon
            privacy = Privacy(epsilon=epsilon, delta=query_info['delta'])
            reader = snsql.from_df(pums, privacy=privacy, metadata=query_info['meta_path'])
            result = reader.execute(query_info['query'])
            if 'aggregated_column' in query_info:
                tempSum = display_results(result, query_info['aggregated_column'])
            else:
                tempSum = display_results(result)
            epsilon_results.append(tempSum)  # Append each result to the list
        
        execute10Times[epsilon] = epsilon_results  # Store results of 10 runs for this epsilon
    return execute10Times


def display_results(result, aggregrated_column = 1):
    if isinstance(result[0], list):  # Check if result contains column names
        table = PrettyTable()
        table.field_names = result[0]
        sum = 0
        for row in result[1:]:
            sum += row[aggregrated_column]
            table.add_row(row)
    return sum

def main():
    plot_execution_data = {}

    for query_info in queries:
        results = execute_privacy_query(query_info)
        plot_execution_data[query_info['name']] = results  # Store results for this query

    # Example of how to print the collected data
    for query_name, data in plot_execution_data.items():
        for epsilon, results in data.items():
            print(f"{query_name} for epsilon={epsilon}: {results}")


    # Plot the results
    plot_query_results(plot_execution_data)

def plot_query_results(plot_data):
    print(plot_data)
    plt.figure(figsize=(10, 8))

    # Define a color map
    colors = list(mcolors.TABLEAU_COLORS)  # This will provide a list of color names

    for query_name, data in plot_data.items():
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
    plt.ylabel(f'{query_name}')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()