import pandas as pd

# Load dataset
df = pd.read_csv(r"..\Data\Vehicle performance.csv")

# Preview data
print(df.head())

# Check structure
print(df.info())
