"""
One morning, you go out and place a dollar bill on the sidewalk by the
Sears tower in Chicago. Each day thereafter, you go out double the number 
of bills. How long does it take for the stack of bills to exceed the height 
of the tower?
bill thickness = 0.11mm
tower height = 442 meters
"""

bill_thickness = 0.11 * (1 / 1000) # 1 meter = 1000 mm 
tower_height = 442
num_bills = 1
num_days = 1

while bill_thickness * num_bills <= tower_height:
    print(f'Days: {num_days}, No of bills: {num_bills}, Stack Height: {num_bills * bill_thickness}')
    num_days = num_days + 1
    num_bills = num_bills * 2

print("")
print("--------------------------------------------------")
print(f'Number of Days:     {num_days}')
print(f'Number of Bills:    {num_bills}')
print(f'Final Height:       {num_bills*bill_thickness}')
print("---------------------------------------------------")