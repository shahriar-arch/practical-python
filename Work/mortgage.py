# mortgage.py
#
# Exercise 1.7

"""
Dave has decided to take out a 30-year fixed rate mortgage
of $500,000 with Guido’s Mortgage, Stock Investment, and 
Bitcoin trading corporation. The interest rate is 5% and 
the monthly payment is $2684.11.
"""

"""
principle = 500000
rate = 0.05
monthly_payment = 2684.11
month = 0
total_payment = 0.0
total_year = 0

while principle > 0:
    principle = round(principle * (1 + (rate / 12)) - monthly_payment, 2)
    total_payment = round(total_payment + monthly_payment, 2)
    month = month + 1
    if month == 12:
        total_year = total_year + 1
        month = 0
        print(f'Total payment after {total_year} year: {total_payment}')
        print(f'Principle after {total_year} year: {principle}')
        

print('---------------------------------------------------')
if month % 12 != 0:
    print(f'Total payment in {total_year} years and {month} months = {total_payment}')
else:
    print(f'Total payment in {total_year} years: {total_payment}')
print('')
print('')
print('Thank You')
"""

"""
Suppose Dave pays an extra $1000/month for the first 
12 months of the mortgage?
Modify the program to incorporate this extra payment and have 
it print the total amount paid along with the number of months 
required.
"""

principle = 500000
rate = 5
monthly_payment = 2684.11
month = 0
total_payment = 0.0
total_year = 0
"""
extra_payment = float(input('Extra Payment: '))
extra_payment_start_month = float(input('Extra Payment Start Month: '))
extra_payment_end_month = float(input('Extra Payment End Month: '))
"""

while principle > 0:
    month = month + 1
    """
    if month == extra_payment_start_month:
        monthly_payment = monthly_payment + extra_payment
    if month == extra_payment_end_month + 1:
        monthly_payment = monthly_payment - extra_payment
    """
    principle = round(principle * (1 + ((rate /100) / 12)), 2)
    
    if principle < monthly_payment:
        monthly_payment = round(principle, 2)
    
    principle = round(principle - monthly_payment, 2)
    total_payment = round(total_payment + monthly_payment,2)
    
    print('-----------------------------------------------')
    print(f'Monts:                    {month}')
    print(f'Monthly Payment           {monthly_payment}')
    print(f'Total Payment:            {total_payment}')
    print(f'Remaining Principle:      {principle}')
    print('-----------------------------------------------')

print('')
print('')
print(f"Dave's total payment is {total_payment}, over {month} months.")