from io_data import export_to_csv, print_to_console

# Example usage
data = [("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9")]
headers = ["A", "B", "C"]

# Export data to CSV file
export_to_csv(data, "output.csv", headers=headers)

# Print data to console
print_to_console(data, headers=headers)
