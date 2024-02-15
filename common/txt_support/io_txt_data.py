import csv

def read_csv(filename):
    """
    Reads data from a CSV file and returns it as a list of lists.
    
    Args:
    - filename: The name of the CSV file to read from.
    
    Returns:
    - A list of lists containing the data from the CSV file.
    """
    data = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def write_csv(filename, data, header=None):
    """
    Writes data to a CSV file.
    
    Args:
    - filename: The name of the CSV file to write to.
    - data: A list of lists where each inner list represents a row.
    - header: Optional. A list representing the header row.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        if header:
            writer.writerow(header)
        writer.writerows(data)

import re

def filter_txt_file(file_path, pattern):
    """
    Reads a text file, filters out each line by a pattern using regular expressions (re),
    and saves the filtered lines to a list.
    
    Args:
    - file_path: The path to the text file.
    - pattern: The regular expression pattern to filter the lines.

    Returns:
    - A list containing the lines that match the pattern.
    """
    filtered_lines = []
    compiled_pattern = re.compile(pattern)  # Compile the pattern

    with open(file_path, 'r') as file:
        for line in file:
            if compiled_pattern.search(line):  # Use the compiled pattern
                filtered_lines.append(line)
    return filtered_lines

def write_lines_to_txt_file(file_path, lines):
    """
    Writes lines from a list to a text file.
    
    Args:
    - file_path: The path to the text file.
    - lines: A list containing the lines to be written to the file.
    """
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line)


import re
def find_pattern_groups_in_txt_file(file_path, pattern, groups):
    """
    Finds a pattern in each line of a text file using regular expressions (re)
    and extracts specified groups from matching lines.
    
    Args:
    - file_path: The path to the text file.
    - pattern: The regular expression pattern to search for.
    - groups: A list of group indices to extract from matching lines.
    
    Returns:
    - A list of lists containing the specified groups extracted from all matching lines.
    """
    extracted_groups = []
    compiled_pattern = re.compile(pattern)  # Compile the pattern

    with open(file_path, 'r') as file:
        for line in file:
            match = compiled_pattern.search(line)
            if match:
                extracted_line_groups = [match.group(i) for i in groups]
                extracted_groups.append(extracted_line_groups)
    return extracted_groups


