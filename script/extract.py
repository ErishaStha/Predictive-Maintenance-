import pandas as pd

# Load dataset
df = pd.read_csv('project-folderdataraw_data.csv')

# Preview data
print(df.head())

# Check structure
print(df.info())
