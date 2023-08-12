import pandas as pd

# Method 1: Basic data validation


def find_inconsistencies_basic(data):
    # Perform basic data validation checks
    inconsistencies = []

    # Example: Check if a column contains only numeric values
    numeric_columns = ['column1', 'column2']
    for column in numeric_columns:
        if not pd.to_numeric(data[column], errors='coerce').notnull().all():
            inconsistencies.append(f"Column '{column}' contains non-numeric values.")

    # Add more data validation checks as needed

    return inconsistencies

# Method 2: Custom data validation rules


def find_inconsistencies_custom(data):
    # Define custom data validation rules
    inconsistencies = []

    # Example: Check if a column contains unique values
    unique_columns = ['column1', 'column2']
    for column in unique_columns:
        if not data[column].is_unique:
            inconsistencies.append(f"Column '{column}' does not have unique values.")

    # Add more custom data validation rules as needed

    return inconsistencies


# Example usage
dataset = pd.read_csv('your_dataset.csv')

# Find inconsistencies using the basic data validation method
inconsistencies_basic = find_inconsistencies_basic(dataset)

# Find inconsistencies using custom data validation rules
inconsistencies_custom = find_inconsistencies_custom(dataset)

# Print the detected inconsistencies
print("Inconsistencies (Basic data validation):")
for inconsistency in inconsistencies_basic:
    print(inconsistency)

print("Inconsistencies (Custom data validation):")
for inconsistency in inconsistencies_custom:
    print(inconsistency)
