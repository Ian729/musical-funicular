import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

# Define the file path
file_path = './LAST_UPDATED'

# Initialize lists to store timestamps and counts
timestamps = []
counts = []

# Read the file and parse the data
with open(file_path, 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 2):
        timestamp = lines[i].strip()
        count = int(lines[i+1].strip().split(': ')[1].strip(','))
        timestamps.append(timestamp)
        counts.append(count)

# Create a DataFrame
data = pd.DataFrame({
    'Timestamp': pd.to_datetime(timestamps),
    'Count': counts
})

# Detect outliers using z-score
counts_array = np.array(counts)
z_scores = np.abs(stats.zscore(counts_array))
outlier_threshold = 1.2
outliers = np.where(z_scores > outlier_threshold)

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(data['Timestamp'], data['Count'], marker='o', label='Counts')

# Highlight the outliers with red circles
plt.scatter(data['Timestamp'].iloc[outliers], data['Count'].iloc[outliers],
            color='red', s=300, facecolors='none', edgecolors='red', label='Outliers')

# Add labels, title, and grid
plt.xlabel('Timestamp')
plt.ylabel('Count')
plt.title('Counts Over Time with Outliers Highlighted')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Add legend
plt.legend()

# Save the plot
plot_path = 'plot.png'
plt.savefig(plot_path)