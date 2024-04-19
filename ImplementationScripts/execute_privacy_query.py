import pandas as pd
from snsql import Privacy
import snsql
from prettytable import PrettyTable
from example_query import queries
import time
import matplotlib.pyplot as plt

def execute_privacy_query(query_info):
    """
    Executes a differentially private SQL query using the SmartNoise SQL toolkit
    and prints the results in a table format.

    Parameter: query_info which contains: 
        name (str): name of the query.
        csv_path (str): Path to the CSV file containing the data.
        meta_path (str): Path to the YAML metadata file.
        query (str): SQL query to be executed.
        epsilon_range (list of floats): Privacy parameter epsilon. Default is 20.0.
        delta (float): Privacy parameter delta. Default is 0.01. It represents the probability of the mechanism's privacy guarantee being violated. 
        In other words, it allows for a small chance of additional privacy leakage.
        A delta of 0 would correspond to pure epsilon-differential privacy, meaning the guarantee holds with absolute certainty.
    """
    pums = pd.read_csv(query_info['csv_path'])
    results = []
    for epsilon in query_info['epsilon_range']:
        privacy = Privacy(epsilon=epsilon, delta=query_info['delta'])
        reader = snsql.from_df(pums, privacy=privacy, metadata=query_info['meta_path'])
        start_time = time.time()
        result = reader.execute(query_info['query'])
        end_time = time.time()
        duration = end_time - start_time
        results.append((epsilon, result, duration))
    return results  

def display_results(result, aggregrated_column = 1):
    if isinstance(result[0], list):  # Check if result contains column names
        table = PrettyTable()
        table.field_names = result[0]
        sum = 0
        for row in result[1:]:
            sum += row[aggregrated_column]
            table.add_row(row)
        print(table)
        print(sum)
    else:
        print("No results to display.")

def main():
    plot_data = {}  # Dictionary to hold data for plotting

    for query_info in queries:
        results = execute_privacy_query(query_info)
        epsilons = []
        durations = []
        for epsilon, result, duration in results:
            print(f"Results for {query_info['name']} with epsilon={epsilon}:")
            if 'aggregrated_column' in query_info:
                display_results(result, query_info['aggregrated_column'])
            else:
                display_results(result)
            print("\n")
            epsilons.append(epsilon)
            durations.append(duration)
        
        # Store the data for plotting
        plot_data[query_info['name']] = (epsilons, durations)

    # Plot the results
    plot_query_runtimes(plot_data)

def plot_query_runtimes(plot_data):
    plt.figure(figsize=(10, 5))
    for query_name, (epsilons, durations) in plot_data.items():
        plt.plot(epsilons, durations, marker='o', label=f'{query_name} runtimes')
    
    plt.title('Query Runtime vs Epsilon')
    plt.xlabel('Epsilon')
    plt.ylabel('Runtime (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()