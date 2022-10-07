p = 500000          #principle 
r = 0.05 / 12       #monthly interest 
n = 12 * 30         #Total monts
c = 0.0             #monthly payment

c = ((r * p) * ((1 + r) ** n)) / (((1 + r) ** n) - 1)

print(f'Monthly payment of the mortgage: {c}')
