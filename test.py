import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta

# Generate sample data with dates
dates = pd.date_range(start='2023-01-01', periods=100)
random_values = [random.randint(0, 36) for _ in range(100)]

data = {
    'Date': dates,
    'ResistanceSumD': random_values
}

df = pd.DataFrame(data)

# Sort DataFrame by date (optional)
df = df.sort_values(by='Date')

# Plotting with Matplotlib
plt.figure(figsize=(10, 6))  # Adjust figure size if needed

plt.plot(df['Date'], df['ResistanceSumD'], marker='o', linestyle='-', color='b', label='ResistanceSumD')

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('ResistanceSumD')
plt.title('ResistanceSumD over Time')

# Format x-axis as dates (optional)
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))

# Rotate x-axis labels (optional)
plt.xticks(rotation=45)

# Show legend (optional)
plt.legend()

# Display plot
plt.tight_layout()
plt.show()