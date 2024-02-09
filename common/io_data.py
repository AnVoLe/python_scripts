import csv

def export_to_csv(data, file_path, headers=None):
    """
    Export data to a CSV file.

    Args:
        data: A list of tuples representing the data to be exported.
        file_path: The file path where the CSV file will be saved.
        headers (optional): A list of strings representing the column headers.
                            If provided, it will be written as the first row in the CSV file.
    """
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if headers:
            writer.writerow(headers)
        writer.writerows(data)

def print_to_console(data, headers=None):
    """
    Print data to the console.

    Args:
        data: A list of tuples representing the data to be printed.
        headers (optional): A list of strings representing the column headers.
                            If provided, it will be printed as the first row in the console.
    """
    # Print column headers
    if headers:
        print(", ".join(headers))
    
    # Print data rows
    for row in data:
        print(", ".join(map(str, row)))
