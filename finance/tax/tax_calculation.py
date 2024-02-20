import argparse
import sys
from pathlib import Path

# Get the current file path
current_file_path = Path(__file__)
# Get the python_scripts path  path (great grand parent directory)
sys.path.append(str(current_file_path.parent.parent.parent))
from common.txt_support import io_txt_data

def get_tax_brackets_from_csv_to_list(year,filing_status,tax_type):
    if tax_type=='federal':
        # Read data from CSV file
        tax_bracket_file=f"finance/tax/tax_brackets_by_year/federal_tax_brackets_{year}.csv"
    elif tax_type=='state':
        # Read data from CSV file
        tax_bracket_file=f"finance/tax/tax_brackets_by_year/CA_state_tax_brackets_{year}.csv"

    tax_brackets = io_txt_data.read_csv(tax_bracket_file)
    # Remove the header row
    tax_brackets = tax_brackets[1:]

    # get the right bracket for a filing status. Also convert str to float
    if(filing_status==0):
        tax_bracket = [(float(rate), float(fed_income)) for rate, fed_income, _, _ in tax_brackets]
    elif(filing_status==1):
        tax_bracket = [(float(rate), float(fed_income)) for rate, _, fed_income, _ in tax_brackets]
    elif(filing_status==2):
        tax_bracket = [(float(rate), float(fed_income)) for rate, _, _, fed_income in tax_brackets]

    return tax_bracket

def calculate_tax(year,filing_status,income, deduction,tax_type):
    tax_brackets=get_tax_brackets_from_csv_to_list(year,filing_status,tax_type)

    taxable_income = income - deduction
    if taxable_income < 0:
        taxable_income = 0
    
    tax = 0
    previous_bracket_limit = 0
    
    for bracket_rate,bracket_limit in tax_brackets:
        if taxable_income <= previous_bracket_limit:
            break
        bracket_taxable_amount = min(taxable_income, bracket_limit) - previous_bracket_limit
        tax += bracket_taxable_amount * bracket_rate
        previous_bracket_limit = bracket_limit
    
    return tax


def main():
    parser = argparse.ArgumentParser(description="Calculate tax liability.")
    parser.add_argument("year", type=int, help="Tax year")
    parser.add_argument("filing_status", type=int, help="Filing status: 0 -> single, 1-> married jointly filing, 2-> heads of household")
    parser.add_argument("fed_income", type=float, help="fed_income for the year")
    parser.add_argument("fed_deduction", type=float, help="fed_deduction amount")
    parser.add_argument("state_income", type=float, help="state_income for the year")
    parser.add_argument("state_deduction", type=float, help="state_deduction amount")
    parser.add_argument("state_exemption", type=float, help="state_exemption amount")
    args = parser.parse_args()

    year=args.year
    filing_status= args.filing_status
    fed_income = args.fed_income
    fed_deduction = args.fed_deduction
    state_income = args.state_income
    state_deduction = args.state_deduction
    state_exemption=args.state_exemption

    if year<2022 or year >2100:
        print("Invalid tax year")
        return

    if filing_status < 0 or filing_status >2:
        print("Filing status must be from 0 to 2.")
        return

    if fed_income < 0:
        print("fed_income cannot be negative.")
        return
    if fed_deduction < 0:
        print("fed_deduction cannot be negative.")
        return
    if state_income < 0:
        print("state_income cannot be negative.")
        return
    if state_deduction < 0:
        print("state_deduction cannot be negative.")
        return

    fed_tax = calculate_tax(year,filing_status,fed_income,fed_deduction,tax_type='federal')
    print("\nThe estimated federal tax: $", round(fed_tax, 2))
    state_tax = calculate_tax(year,filing_status,state_income,state_deduction,tax_type='state')
    adjust_state_tax=state_tax-state_exemption
    print("\nThe estimated State tax: $", round(adjust_state_tax, 2))

    total_tax=fed_tax+adjust_state_tax
    print("\nTotal estimated tax:",round(total_tax,2))
    print()

if __name__ == "__main__":
    main()
