# bounce.py
"""
A rubber ball is dropped from a height of 100 meters and each 
time it hits the ground, it bounces back up to 3/5 the height
 it fell. Write a program bounce.py that prints a table showing
  the height of the first 10 bounces.
"""
# Exercise 1.5

bounceHeight = 0
bounceNum = 0

droppingHeight = 100
bounceRatio = 3 / 5 

while bounceNum < 10:
    bounceNum = bounceNum + 1
    bounceHeight = round(droppingHeight * bounceRatio, 4)
    print(f'{bounceNum} {bounceHeight}')
    droppingHeight = bounceHeight

print('Thank You!')
