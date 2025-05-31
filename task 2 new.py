# Import required libraries
import pandas as pd

# Load dataset
df = pd.read_csv("C:\\Users\\Divya T C\\Downloads\\Titanic-Dataset (1).csv")

# Fix column names
df.columns = df.columns.str.strip()

# Debugging Step: Print actual column names
print("Columns in dataset:", df.columns.tolist())

# Ensure 'Age' exists before accessing it
if "Age" not in df.columns:
    print("Column 'Age' not found in dataset! Adding a default column.")
    df["Age"] = 0  # Assign default values if missing
else:
    df["Age"].fillna(df["Age"].median(), inplace=True)

# Print dataset info
print("\nDataset Info:")
print(df.info())