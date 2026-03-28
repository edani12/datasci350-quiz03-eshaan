import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Read the streaming platform data
with open('streaming_data.txt', 'r') as f:
    lines = f.readlines()

# Skip the header comment and read the data
data_str = ''.join(lines[1:])
from io import StringIO
df = pd.read_csv(StringIO(data_str), sep=r'\s+')

# Convert date column to datetime objects
df['date'] = pd.to_datetime(df['date'])

# Print basic statistics
print("Streaming Platform Analysis:")
print("============================")
print(f"Total days analysed: {len(df)}")
print(f"Total hours watched: {df['hours_watched'].sum():,.0f}")
print(f"Average daily hours watched: {df['hours_watched'].mean():,.0f}")
print(f"Total new subscribers: {df['new_subscribers'].sum():,}")
print(f"Average daily churn rate: {df['churn_rate'].mean():.2f}%")
peak_idx = df['hours_watched'].idxmax()
peak_date = str(df.at[peak_idx, 'date'])
print(f"Peak viewing day: {peak_date} with {df.at[peak_idx, 'hours_watched']:,} hours")

# Find most popular genre
genre_counts = df['top_genre'].value_counts()
print(f"Most frequent top genre: {genre_counts.index[0]} ({genre_counts.iloc[0]} days)")

# Create a visualisation
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
sns.set_style("whitegrid")

# Plot 1: Hours watched and new subscribers
ax1.plot(df['date'], df['hours_watched'], marker='o', color='dodgerblue', linewidth=2, label='Hours Watched')
ax1.set_xlabel('Date')
ax1.set_ylabel('Hours Watched', color='dodgerblue')
ax1.set_title('Daily Viewing Hours and New Subscribers', fontsize=14, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='dodgerblue')
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, alpha=0.3)

ax1b = ax1.twinx()
ax1b.plot(df['date'], df['new_subscribers'], marker='s', color='forestgreen', linewidth=2, label='New Subscribers')
ax1b.set_ylabel('New Subscribers', color='forestgreen')
ax1b.tick_params(axis='y', labelcolor='forestgreen')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax1b.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# Plot 2: Genre popularity
genre_totals = df.groupby('top_genre')['hours_watched'].sum().sort_values()
bars = ax2.barh(genre_totals.index, genre_totals.values, color=sns.color_palette("viridis", len(genre_totals)))
ax2.set_xlabel('Total Hours Watched')
ax2.set_title('Total Viewing Hours by Genre', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='x')

# Add value labels on bars
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax2.text(width + max(genre_totals) * 0.01, bar.get_y() + bar.get_height()/2,
             f'{width:,.0f}', ha='left', va='center')

plt.tight_layout()
fig.suptitle('30-Day Streaming Platform Performance Report', fontsize=18, fontweight='bold', y=1.02)

# Save the figure
plt.savefig('streaming_analysis.png', bbox_inches='tight', dpi=300)
print("\nAnalysis complete. Results saved to 'streaming_analysis.png'")
