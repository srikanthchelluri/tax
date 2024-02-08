#!/usr/bin/env python3
import argparse
import sys
import yaml

def calculate_tax(salary, tax_brackets):
    tax = 0
    prev_bmax = 0
    for bmax, btax in tax_brackets:
        if salary < bmax or bmax == -1:
            tax += (salary - prev_bmax) * btax
            return tax
        tax += (bmax - prev_bmax) * btax
        prev_bmax = bmax
    return sys.minsize

def load_constants():
    with open('./constants.yaml', 'r') as f:
        return yaml.safe_load(f)

def print_constants(year, wages, tax_loss_harvesting, ny_percentage, va_percentage):
    print('CONSTANTS')
    print('Year:', "%.0f" % args.year)
    print('Wages:', "%.0f" % args.wages)
    print('Tax loss harvesting:', "%.0f" % args.tax_loss_harvesting)
    print('NY percentage:', "%.3f" % args.ny_percentage)
    print('VA percentage:', "%.3f" % args.va_percentage)
    print()

def print_taxes(federal_tax, social_security_tax, medicare_tax, ny_tax, va_tax, nyc_tax):
    print('TAXES')
    print('Federal:', "%.0f" % federal_tax)
    print('Social security:', "%.0f" % social_security_tax)
    print('Medicare:', "%.0f" % medicare_tax)
    print('NY state:', "%.0f" % ny_tax)
    print('VA state:', "%.0f" % va_tax)
    print('NYC local:', "%.0f" % nyc_tax)
    print()
    print('SUMMARY')
    taxes = federal_tax + social_security_tax + medicare_tax + ny_tax + va_tax + nyc_tax
    print('Total taxes:', "%.0f" % taxes)
    print('Tax percentage', "%.3f" % (taxes / args.wages))
    net = args.wages - taxes
    print('Net:', "%.0f" % net)
    print('Net percentage', "%.3f" % (net / args.wages))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, default=2023, help="Year for tax calculation")
    parser.add_argument("--wages", type=float, help="Total wages")
    parser.add_argument("--tax-loss-harvesting", type=float, default=3000, help="Tax loss harvesting amount")
    parser.add_argument("--ny-percentage", type=float, help="Percentage of time in NY")
    parser.add_argument("--va-percentage", type=float, help="Percentage of time in VA")
    args = parser.parse_args()

    # Load constants
    constants = load_constants()

    # Create data structures to calculate taxes
    federal_tax_brackets = [(b['max'], b['rate']) for b in constants[args.year]['federal']['brackets']]
    federal_standard_deduction = constants[args.year]['federal']['standardDeduction']

    social_security_tax_brackets = [(b['max'], b['rate']) for b in constants[args.year]['federal']['socialSecurity']]

    medicare_tax_brackets = [(b['max'], b['rate']) for b in constants[args.year]['federal']['medicare']]

    ny_state_tax_brackets = [(b['max'], b['rate']) for b in constants[args.year]['state']['ny']['brackets']]
    ny_state_standard_deduction  = constants[args.year]['state']['ny']['standardDeduction']

    va_state_tax_brackets = [(b['max'], b['rate']) for b in constants[args.year]['state']['va']['brackets']]
    va_state_standard_deduction = constants[args.year]['state']['va']['standardDeduction']

    nyc_local_tax_brackets = [(b['max'], b['rate']) for b in constants[args.year]['local']['nyc']['brackets']]
    nyc_local_standard_deduction = constants[args.year]['local']['nyc']['standardDeduction']

    # Calculate taxes
    federal_tax = calculate_tax(args.wages - args.tax_loss_harvesting - federal_standard_deduction, federal_tax_brackets)
    social_security_tax = calculate_tax(args.wages, social_security_tax_brackets)
    medicare_tax = calculate_tax(args.wages, medicare_tax_brackets)

    va_tax = calculate_tax((args.wages - args.tax_loss_harvesting - va_state_standard_deduction) * args.va_percentage, va_state_tax_brackets)
    ny_tax_raw = 0
    ny_tax = 0
    if args.ny_percentage > 0:
        ny_tax_raw = calculate_tax((args.wages - args.tax_loss_harvesting - ny_state_standard_deduction), ny_state_tax_brackets)
        ny_tax = ny_tax_raw - va_tax
    nyc_tax = calculate_tax((args.wages - args.tax_loss_harvesting - nyc_local_standard_deduction) * args.ny_percentage, nyc_local_tax_brackets)

    # Print outputs
    print_constants(
        args.year,
        args.wages,
        args.tax_loss_harvesting,
        args.ny_percentage,
        args.va_percentage)
    print_taxes(
        federal_tax,
        social_security_tax,
        medicare_tax,
        ny_tax,
        va_tax,
        nyc_tax)
