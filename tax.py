#!/usr/bin/env python3
import sys
import yaml

YEAR = 2023
WAGES = -1
TAX_LOSS_HARVESTING = 3000
NY_PERCENTAGE = 0.65
VA_PERCENTAGE = 0.35

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

constants = {}
with open('./constants.yaml', 'r') as f:
    constants = yaml.safe_load(f)

federal_tax_brackets = [(b['max'], b['rate']) for b in constants[YEAR]['federal']['brackets']]
federal_standard_deduction = constants[YEAR]['federal']['standardDeduction']

social_security_tax_brackets = [(b['max'], b['rate']) for b in constants[YEAR]['federal']['socialSecurity']]

medicare_tax_brackets = [(b['max'], b['rate']) for b in constants[YEAR]['federal']['medicare']]

ny_state_tax_brackets = [(b['max'], b['rate']) for b in constants[YEAR]['state']['ny']['brackets']]
ny_state_standard_deduction  = constants[YEAR]['state']['ny']['standardDeduction']

va_state_tax_brackets = [(b['max'], b['rate']) for b in constants[YEAR]['state']['va']['brackets']]
va_state_standard_deduction = constants[YEAR]['state']['va']['standardDeduction']

nyc_local_tax_brackets = [(b['max'], b['rate']) for b in constants[YEAR]['local']['nyc']['brackets']]
nyc_local_standard_deduction = constants[YEAR]['local']['nyc']['standardDeduction']


federal_tax = calculate_tax(WAGES - TAX_LOSS_HARVESTING - federal_standard_deduction, federal_tax_brackets)
social_security_tax = calculate_tax(WAGES, social_security_tax_brackets)
medicare_tax = calculate_tax(WAGES, medicare_tax_brackets)

va_tax = calculate_tax((WAGES - TAX_LOSS_HARVESTING - va_state_standard_deduction) * VA_PERCENTAGE, va_state_tax_brackets)
ny_tax_raw = 0
ny_tax = 0
if NY_PERCENTAGE > 0:
    ny_tax_raw = calculate_tax((WAGES - TAX_LOSS_HARVESTING - ny_state_standard_deduction), ny_state_tax_brackets)
    ny_tax = ny_tax_raw - va_tax
nyc_tax = calculate_tax((WAGES - TAX_LOSS_HARVESTING - nyc_local_standard_deduction) * NY_PERCENTAGE, nyc_local_tax_brackets)

print('CONSTANTS')
print('Year:', "%.0f" % YEAR)
print('Wages:', "%.0f" % WAGES)
print('Tax loss harvesting:', "%.0f" % TAX_LOSS_HARVESTING)
print('NY percentage:', "%.3f" % NY_PERCENTAGE)
print('VA percentage:', "%.3f" % VA_PERCENTAGE)
print()
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
print('Tax percentage', "%.3f" % (taxes / WAGES))
net = WAGES - taxes
print('Net:', "%.0f" % net)
print('Net percentage', "%.3f" % (net / WAGES))
