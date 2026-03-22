import pandas as pd

# Load dataset
df = pd.read_csv('C:/Users/erish/Downloads/vehicle-etl-pipeline/Data/project-folderdataraw_data.csv')

# Preview data
print(df.head())

# Check structure
print(df.info())
