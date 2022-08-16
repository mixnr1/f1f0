# f1f0
FIFO calculator

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
