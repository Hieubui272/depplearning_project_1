import pandas as pd

# Load and check CSV file
labels_df = pd.read_csv('/content/G1020/G1020.csv')
print(labels_df.columns)
