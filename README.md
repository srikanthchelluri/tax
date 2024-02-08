# `taxes`

Usage:

```bash
> python tax.py --help                                                  
usage: tax.py [-h] [--year YEAR] [--wages WAGES] [--tax-loss-harvesting TAX_LOSS_HARVESTING]
              [--ny-percentage NY_PERCENTAGE] [--va-percentage VA_PERCENTAGE]

options:
  -h, --help            show this help message and exit
  --year YEAR           Year for tax calculation
  --wages WAGES         Total wages
  --tax-loss-harvesting TAX_LOSS_HARVESTING
                        Tax loss harvesting amount
  --ny-percentage NY_PERCENTAGE
                        Percentage of time in NY
  --va-percentage VA_PERCENTAGE
                        Percentage of time in VA
```

Example:

```bash
> python tax.py --wages 100000 --ny-percentage 0.5 --va-percentage 0.5
CONSTANTS
Year: 2023
Wages: 100000
Tax loss harvesting: 3000
NY percentage: 0.500
VA percentage: 0.500

TAXES
Federal: 14042
Social security: 6200
Medicare: 1450
NY state: 2485
VA state: 2287
NYC local: 1687

SUMMARY
Total taxes: 28151
Tax percentage 0.282
Net: 71849
Net percentage 0.718
```