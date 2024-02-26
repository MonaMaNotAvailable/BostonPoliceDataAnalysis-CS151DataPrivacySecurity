import pandas as pd
import matplotlib.pyplot as plt

#Query 2 visual: bar chart with allegations types frequency
file_path = '/Users/mona/Downloads/HighestNeighAllegations.csv'
df = pd.read_csv(file_path)
# print(df)

# # Plotting the pie chart
# plt.figure(figsize=(10, 8))  # Set figure size
# plt.pie(df['frequency'], labels=df['neighborhood'], autopct='%1.1f%%', startangle=140)
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.title('Frequency Distribution by Neighborhood')  # Add title
# plt.show()

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the pie chart without labels
wedges, texts, autotexts = ax.pie(
    df['frequency'],
    autopct=lambda pct: "{:.1f}%".format(pct) if pct > 1 else '',
    startangle=140,
    textprops=dict(color="w")
)

# Remove the percentage labels from the wedges
for autotext in autotexts:
    autotext.set_visible(False)

# Generate the legend by combining category names with their corresponding percentages
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(df['neighborhood'], df['frequency']/df['frequency'].sum()*100)]

# Place the legend outside the pie chart
ax.legend(wedges, labels, title="Neighborhoods", loc='center left', bbox_to_anchor=(0.7, 0.2))

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Set the title for the pie chart
plt.title('Allegation Frequency Distribution by Neighborhoods')

# Show the plot
plt.show()