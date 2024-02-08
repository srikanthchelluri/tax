`taxes`

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
```