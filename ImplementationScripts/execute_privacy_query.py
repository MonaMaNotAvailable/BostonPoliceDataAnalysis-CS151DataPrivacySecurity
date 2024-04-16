import pandas as pd
from snsql import Privacy
import snsql
from prettytable import PrettyTable
from example_query import queries

def execute_privacy_query(query_info):
    """
    Executes a differentially private SQL query using the SmartNoise SQL toolkit
    and prints the results in a table format.

    Parameter: query_info which contains: 
        name (str): name of the query.
        csv_path (str): Path to the CSV file containing the data.
        meta_path (str): Path to the YAML metadata file.
        query (str): SQL query to be executed.
        epsilon (float): Privacy parameter epsilon. Default is 20.0.
        delta (float): Privacy parameter delta. Default is 0.01.
    """
    privacy = Privacy(epsilon=query_info['epsilon'], delta=query_info['delta'])
    pums = pd.read_csv(query_info['csv_path'])
    reader = snsql.from_df(pums, privacy=privacy, metadata=query_info['meta_path'])
    result = reader.execute(query_info['query'])
    return result

def display_results(result):
    table = PrettyTable()
    table.field_names = result[0]  # Assuming the first row contains column names
    for row in result[1:]:
        table.add_row(row)
    print(table)

def main():
    results = {}
    for query_info in queries:
        result = execute_privacy_query(query_info)
        results[query_info['name']] = result
        print(f"Results for {query_info['name']}:")
        display_results(result)
        print("\n")

if __name__ == "__main__":
    main()