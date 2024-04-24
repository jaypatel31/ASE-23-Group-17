import pandas as pd
import numpy as np

# Specify the path to your CSV file
csv_file_path = './Trial04_y.csv'

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Check if the CSV file has at least 100 rows
if len(df) < 100:
    print("Error: The CSV file does not have enough rows.")
    exit()

# Randomly select 100 row indices
random_indices = np.random.choice(len(df), 200, replace=False)

# Iterate over the randomly selected row indices and modify the second column
for idx in random_indices:
    # Generate a random integer value between 0 and 3 (inclusive)
    new_value = np.random.randint(4)
    
    # Update the value in the second column (index 1)
    df.iloc[idx, 1] = new_value

# Save the modified DataFrame back to a new CSV file
output_csv_path = 'modified_output4.csv'
df.to_csv(output_csv_path, index=False)

print(f"Successfully modified and saved 100 rows to '{output_csv_path}'.")