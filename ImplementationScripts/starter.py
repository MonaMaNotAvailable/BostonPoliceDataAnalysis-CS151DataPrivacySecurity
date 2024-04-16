import snsql
from snsql import Privacy
import pandas as pd
from prettytable import PrettyTable
privacy = Privacy(epsilon=20.0, delta=0.01)

csv_path = 'DatasetForPrivacy/bpd-allegations.csv'
meta_path = 'DatasetForPrivacy/bpd-allegations.yaml'
# csv_path = 'DatasetForPrivacy/test.csv'
# meta_path = 'DatasetForPrivacy/test.yaml'

pums = pd.read_csv(csv_path)
reader = snsql.from_df(pums, privacy=privacy, metadata=meta_path)
query = """
SELECT 
    allegation,
    COUNT(*) AS frequency
FROM 
    bpd_allegations.bpd_allegations
GROUP BY 
    allegation
ORDER BY 
    frequency DESC;
"""
result = reader.execute(query)
# print(result)
table = PrettyTable()
table.field_names = result[0] 

# Add the rest of the data
for row in result[1:]:
    table.add_row(row)

print(table)