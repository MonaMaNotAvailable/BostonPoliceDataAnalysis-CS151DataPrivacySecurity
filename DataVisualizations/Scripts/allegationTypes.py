import pandas as pd
import matplotlib.pyplot as plt

#Query 1 visual: bar chart with allegations types frequency
file_path = '../../QueriedCSVOutput/MostCommonAllegations.csv'
df = pd.read_csv(file_path)

# Convert 'allegation' column to string type
df['allegation'] = df['allegation'].astype(str)

# Keep the first 13 rows
df_top = df.iloc[:13]

# Sum up the remaining rows into the 'Others' category
others_frequency = df.iloc[13:]['frequency'].sum()
others_percentage = df.iloc[13:]['percentage'].sum()

# Create a new DataFrame for the 'Others' category
df_others = pd.DataFrame({'allegation': ['Others'],
                          'frequency': [others_frequency],
                          'percentage': [others_percentage]})

# Append the 'Others' row to the top rows
df_final = pd.concat([df_top, df_others], ignore_index=True)

# Now df_final is your updated DataFrame
print(df_final)

# print(df.head())
# Plotting
plt.figure(figsize=(10, 6))  # Set the figure size (optional)
plt.bar(df_final['allegation'], df_final['frequency'], color='plum')  # Create a bar chart
plt.xlabel('Allegation')  # Set the x-axis label
plt.ylabel('Frequency')  # Set the y-axis label
plt.title('Frequency of Allegations')  # Set the title
plt.xticks(rotation=45, ha="right")  # Rotate the x-axis labels for better readability
plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()  # Display the plot