"""
To access the list index information, so where the list element you're iterating over is located, you can use
enumerate().
"""

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Loop with use of enumerate(). Index +1 to avoid room 0.
for index, area in enumerate(areas):
    print('room '+str(index+1)+': '+str(area))
