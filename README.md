# `taxes`

Usage:

```bash
> python tax.py --help
usage: tax.py [-h] [--year YEAR] [--wages WAGES] [--tax-loss-harvesting TAX_LOSS_HARVESTING] [--ny-percentage NY_PERCENTAGE] [--ct-percentage CT_PERCENTAGE] [--va-percentage VA_PERCENTAGE]

options:
  -h, --help            show this help message and exit
  --year YEAR           Year for tax calculation
  --wages WAGES         Total wages
  --tax-loss-harvesting TAX_LOSS_HARVESTING
                        Tax loss harvesting amount
  --ny-percentage NY_PERCENTAGE
                        Percentage of time in NY
  --ct-percentage CT_PERCENTAGE
                        Percentage of time in CT
  --va-percentage VA_PERCENTAGE
                        Percentage of time in VA
```

Example:

```bash
> python tax.py --wages 100000 --ny-percentage 0.5 --ct-percentage 0.4 --va-percentage 0.1
CONSTANTS
Year: 2024
Wages: 100000
Tax loss harvesting: 3000
NY percentage: 0.500
CT percentage: 0.400
VA percentage: 0.100

TAXES
Federal: 13181
Social security: 6200
Medicare: 1450
NY state: 3055
CT state: 1740
VA state: 312
NYC local: 1603

SUMMARY
Total taxes: 25802
Federal tax percentage: 0.132
NY state tax percentage: 0.031
CT state tax percentage: 0.017
VA state tax percentage: 0.003
NYC local tax percentage: 0.016
Tax percentage 0.258
Net: 74198
Net percentage 0.742
```