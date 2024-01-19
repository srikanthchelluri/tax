#!/usr/bin/env python3
import sys

# this is inaccurate, assumes you're taxed across all states

# 2024, single

FEDERAL_TAX_BRACKET_TO_RATE = [
    (11600, 0.1),
    (47150, 0.12),
    (100525, 0.22),
    (191950, 0.24),
    (243725, 0.32),
    (609350, 0.35),
    (sys.maxsize, 0.37),
]
NEW_YORK_STATE_TAX_BRACKET_TO_RATE = [
    (8500, 0.04),
    (11700, 0.045),
    (13900, 0.0525),
    (80650, 0.055),
    (215400, 0.06),
    (1077550, 0.0695),
    (5000000, 0.0965),
    (25000000, 0.103),
    (sys.maxsize, 0.109),
]
CONNECTICUT_STATE_TAX_BRACKET_TO_RATE = [
    (10000, 0.02),
    (50000, 0.045),
    (100000, 0.055),
    (200000, 0.06),
    (250000, 0.065),
    (500000, 0.069),
    (sys.maxsize, 0.0699),
]
VIRGINIA_STATE_TAX_BRACKET_TO_RATE = [
    (3000, 0.02),
    (5000, 0.03),
    (17000, 0.05),
    (sys.maxsize, 0.0575)
]
NEW_YORK_CITY_TAX_BRACKET_TO_RATE = [
    (12000, 0.0378),
    (25000, 0.03762),
    (50000, 0.03819),
    (sys.maxsize, 0.03867),
]

FEDERAL_BONUS_WITHOLDING_RATE = [(sys.maxsize, 0.22)]
NEW_YORK_STATE_BONUS_WITHOLDING_RATE = [(sys.maxsize, 0.117)]
NEW_YORK_CITY_BONUS_WITHOLDING_RATE = [(sys.maxsize, 0.0425)]
CONNECTICUT_STATE_BONUS_WITHHOLDING_RATE = [(sys.maxsize, 0)]
VIRGINIA_BONUS_WITHHOLDING_RATE = [(sys.maxsize, 0.0575)]

SOCIAL_SECURITY_CONTRIBUTION_LIMIT_TO_RATE = [
    (168600, 0.062),
    (sys.maxsize, 0),
]

MEDICARE_CONTRIBUTION_LIMIT_TO_RATE = [
    (200000, 0.0145),
    (sys.maxsize, 0.0145 + 0.009),
]

def calculate_tax(salary, tax_brackets):
    tax = 0
    last = False
    prev_up_to = 0
    for up_to, rate in tax_brackets:
        if last:
            break
        if salary < up_to:
            up_to = salary
            last = True
        tax += (up_to - prev_up_to) * rate
        prev_up_to = up_to
    return tax

salary = 1
bonus = 1

print('salary', salary)
print('bonus', bonus)
print()

fed_salary_tax = calculate_tax(salary, FEDERAL_TAX_BRACKET_TO_RATE)

ny_salary_tax = calculate_tax(salary, NEW_YORK_STATE_TAX_BRACKET_TO_RATE)
ct_salary_tax = calculate_tax(salary, CONNECTICUT_STATE_TAX_BRACKET_TO_RATE)
va_salary_tax = calculate_tax(salary, VIRGINIA_STATE_TAX_BRACKET_TO_RATE)

nyc_salary_tax = calculate_tax(salary, NEW_YORK_CITY_TAX_BRACKET_TO_RATE)

fed_bonus_tax = calculate_tax(bonus, FEDERAL_BONUS_WITHOLDING_RATE)

ny_bonus_tax = calculate_tax(bonus, NEW_YORK_CITY_BONUS_WITHOLDING_RATE)
ct_bonus_tax = calculate_tax(bonus, CONNECTICUT_STATE_BONUS_WITHHOLDING_RATE)
va_bonus_tax = calculate_tax(bonus, VIRGINIA_BONUS_WITHHOLDING_RATE)

social_security_tax = calculate_tax(salary + bonus, SOCIAL_SECURITY_CONTRIBUTION_LIMIT_TO_RATE)
medicare_tax = calculate_tax(salary + bonus, MEDICARE_CONTRIBUTION_LIMIT_TO_RATE)

total_tax = fed_salary_tax + ny_salary_tax + ct_salary_tax + va_salary_tax + nyc_salary_tax + fed_bonus_tax + ny_bonus_tax + ct_bonus_tax + va_bonus_tax + social_security_tax + medicare_tax

print('fed_salary_tax', fed_salary_tax)
print('ny_salary_tax', ny_salary_tax)
print('ct_salary_tax', ct_salary_tax)
print('va_salary_tax', va_salary_tax)
print('nyc_salary_tax', nyc_salary_tax)
print('fed_bonus_tax', fed_bonus_tax)
print('ny_bonus_tax', ny_bonus_tax)
print('ct_bonus_tax', ct_bonus_tax)
print('va_bonus_tax', va_bonus_tax)
print('social_security_tax', social_security_tax)
print('medicare_tax', medicare_tax)
print()

print('total tax', total_tax)
print('total take home', salary + bonus - total_tax)
print('total tax percentage', total_tax / (salary + bonus))
print('total take home percentage', 1 - total_tax / (salary + bonus))
