import sys
from pathlib import Path

# Get the current file path
current_file_path = Path(__file__)
# Get the python_scripts path  path (great grand parent directory)
sys.path.append(str(current_file_path.parent.parent.parent))
from common.txt_support import io_txt_data

federal_tax_brackets_2022 = [
    (0.10, 10275, 20550, 14650),
    (0.12, 41775, 83550, 55900),
    (0.22, 89075, 178150, 89050),
    (0.24, 170050, 340100, 170050),
    (0.32, 215950, 431900, 215950),
    (0.35, 539900, 647850, 539900),
    (0.37, float('inf'), float('inf'), float('inf'))
]

CA_state_tax_brackets_2022 = [
    (0.01, 10099, 20198, 20212),
    (0.02, 23942, 47884, 47887),
    (0.04, 37788, 75576, 61730),
    (0.06, 52455, 104910, 76397),
    (0.08, 66295, 132590, 90240),
    (0.093, 338639, 677278, 460547),
    (0.103, 406364, 812728, 552658),
    (0.113, 677275, 1354550, 921095),
    (0.123, float('inf'), float('inf'), float('inf'))
]

federal_tax_brackets_2023 = [
    (0.10, 11000, 22000, 15700),
    (0.12, 44725, 89450, 59850),
    (0.22, 95375, 190750, 95350),
    (0.24, 182100, 364200, 182100),
    (0.32, 231250, 462500, 231250),
    (0.35, 578125, 693750, 578100),
    (0.37, float('inf'), float('inf'), float('inf'))
]

CA_state_tax_brackets_2023 = [
    (0.01, 10412, 20824, 20839),
    (0.02, 24684, 49368, 49371),
    (0.04, 38959, 77918, 63644),
    (0.06, 54081, 108162, 78765),
    (0.08, 68350, 136700, 93037),
    (0.093, 349137, 698274, 474824),
    (0.103, 418961, 837922, 569790),
    (0.113, 698271, 1396542, 949649),
    (0.123, float('inf'), float('inf'), float('inf'))
]


# Create a dictionary to hold tax brackets for different years
tax_brackets_by_year = {
    'federal_tax_brackets_2022': federal_tax_brackets_2022,
    'CA_state_tax_brackets_2022': CA_state_tax_brackets_2022,
    'federal_tax_brackets_2023':federal_tax_brackets_2023,
    'CA_state_tax_brackets_2023': CA_state_tax_brackets_2023,
    # Add other years as needed...
}


header=["Tax Rate","For Single Filers","For Married Individuals Filling Joint","For Heads of households"]
output_path=Path("finance/tax/tax_brackets_by_year")

# Iterate over the dictionary and write data to csv files
for type_year, brackets in tax_brackets_by_year.items():
    file_name=type_year+".csv"
    output_tax_bracket_file=output_path/file_name
    io_txt_data.write_csv(output_tax_bracket_file,brackets,header)

