import pandas as pd

# Load dataset
df = pd.read_csv(r'Vehicle performance')

# Preview data
print(df.head())

# Check structure
print(df.info())
