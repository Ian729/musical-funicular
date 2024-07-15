import matplotlib.pyplot as plt
import pandas as pd

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

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(data['Timestamp'], data['Count'], marker='o')
plt.xlabel('Timestamp')
plt.ylabel('Count')
plt.title('Counts Over Time')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plot_path = 'plot.png'
plt.savefig(plot_path)