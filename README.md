# f1f0
FIFO calculator

One of the taxation regimes in the field of cryptocurrency is the taxation of income from capital gains. Capital gains is understood as income (profits) from the sale of cryptocurrency. The sale of cryptocurrency is regarded as a swap transaction resulting in obtaining an official currency (fiat currency) or other services. If a transaction occurs at a loss, the transaction itself shall not be taxed. Losses can be used to recover the overpaid tax.

**IMPORTANT:** The laws governing the application of taxes may vary depending on the country in which you are located. Note that tax regulation may change over time.

## How is capital gains calculated?
**asset sales value** – **original asset acquisition value**

**IMPORTANT:** The sale/buy price of a cryptocurrency is considered to be the payment received in official currency (fiat currency). If it is not possible to determine the initial acquisition value of the capital asset, the acquisition value shall be considered to be 0.
FIFO or the weighted average method may be used to calculate the acquisition value. The method chosen shall be used for at least 10 years. The acquisition value may include expenses (commissions, government fees) related to obtaining cryptocurrency.

## How do I use f1f0.py script to calculate taxes from capital gains?

To prepare an virtual environment with all required script dependencies, follow these steps:
```
$git clone https://github.com/mixnr1/f1f0.git
$python3 -m venv f1f0/
$cd f1f0/
$source bin/activate
$pip install -r requirement.txt
```
Use the following command to display the calculation of script on the screen:
```
$python3 f1f0.py -f /path/to/input/xlsx_file
```
Use the following command to save the calculation of script in csv file:
```
$python3 f1f0.py -f /path/to/input/xlsx_file -o /path/to/output/csv_file 
```
Use the following command to apply the column names of the xlsx file (default values are 'Datums', 'EUR', 'EUR/BTC', 'BTC')
```
$python3 f1f0.py -f /path/to/input/xlsx_file -c Date EUR EUR/BTC BTC
$python3 f1f0.py -f /path/to/input/xlsx_file -c 'Date' 'EUR' 'EUR/BTC' 'BTC'
```
Use the following command to change the tax rate (the default tax rate is 20% (0.2))
```
$python3 f1f0.py -f /path/to/input/xlsx_file -t 0.21 
$python3 f1f0.py -f /path/to/input/xlsx_file -o /path/to/output/csv_file -t 0.21
```
