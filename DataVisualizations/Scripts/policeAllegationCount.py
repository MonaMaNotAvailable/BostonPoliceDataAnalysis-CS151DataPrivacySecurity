import pandas as pd
import matplotlib.pyplot as plt

#Query 2 visual: bar chart with allegations types frequency
file_path = '/Users/mona/Downloads/OfficersDemographicAllegationsPer.csv'
df_original = pd.read_csv(file_path)
# print(df_original)

# Keep the first 12 rows
df = df_original.iloc[:12]
print(df)

# Pivot the DataFrame to create a matrix with first_name as columns, neighborhood as rows,
# and allegation_percentage as values
pivot_df = df.pivot_table(
    index='neighborhood', 
    columns='first_name', 
    values='allegation_percentage', 
    aggfunc='sum',
    fill_value=0
)

# Plot a stacked bar chart
pivot_df.plot(
    kind='bar', 
    stacked=True, 
    figsize=(10, 6)
)

# Customize the plot with labels and title
plt.xlabel('Neighborhood')
plt.ylabel('Total Allegation Percentage')
plt.title('Allegation Percentage by Neighborhood and Officer')
plt.legend(title='First Name', bbox_to_anchor=(1.05, 1), loc='upper left')

# Improve layout to accommodate the legend
plt.tight_layout()

# Show the plot
plt.show()