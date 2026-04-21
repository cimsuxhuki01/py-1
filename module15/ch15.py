import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv('module15/weather_tokyo_data.csv')
for col in ['temperature', 'humidity', 'atmospheric pressure']:
    # Convert to string first
    df[col] = df[col].astype(str)

    # Remove spaces
    df[col] = df[col].str.strip()

    # Handle negative values written like (0.3)
    df[col] = df[col].str.replace("(", "-")
    df[col] = df[col].str.replace(")", "")

    # Remove commas
    df[col] = df[col].str.replace(",", "")

    # Convert to float
    df[col] = df[col].astype(float)

df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['day'].astype(str))
df['month'] = df['date'].dt.month

# Average temperature
print(f"Average temperature: {df['temperature'].mean():.2f}°C")

# Monthly averages
monthly_avg = df.groupby('month')['temperature'].mean()
sns.barplot(x=monthly_avg.index, y=monthly_avg.values)
plt.title('Average Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.show()

# Hottest & coldest days
print("\nHottest Day:\n", df.loc[df['temperature'].idxmax()])
print("\nColdest Day:\n", df.loc[df['temperature'].idxmin()])

# Seasonal averages
def get_season(m): 
    return ['Winter','Spring','Summer','Autumn'][(m%12)//3]

df['season'] = df['month'].apply(get_season)
seasonal_avg = df.groupby('season')['temperature'].mean()
print("\nSeasonal Average Temperatures:\n", seasonal_avg.round(2))

# Line plot for seasonal averages
sns.lineplot(x=seasonal_avg.index, y=seasonal_avg.values)
plt.title('Seasonal Average Temperature')
plt.ylabel('Temperature (°C)')
plt.show()

# Bar plot for seasonal averages
sns.barplot(x='season', y='temperature', data=df)
plt.title('Temperature by Season')
plt.ylabel('Temperature (°C)')
plt.show()
