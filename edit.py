import csv

input_csv = "car_data.csv"
output_csv = "output.csv"

# Open the input CSV file
with open(input_csv, 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Extract the values from the first column
    first_column_values = [row[1] for row in reader]

# Open the output CSV file
with open(output_csv, 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    
    # Write the first column values to the output CSV file
    for value in first_column_values:
        writer.writerow([value])