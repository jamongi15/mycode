#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'Your points translated to '

# wrap connection in a float() to accept decimals as numbers
points = int(input("Input your grade percentage points "))

# if input value was higher or equal to 25
#if points in range (90,101):
if (90 <= points <=100):
    message = message + ' A '
elif points in range (80,90):
    message = message + ' B '
#elif points in range (70,80):
elif (69<= points <=80):
    message = message + ' C '
elif points in range (60,70):
    message = message + ' D '
elif points in range (0,60):
    message = message + ' F '
else:
    message = message + ' an out of range percentage points '
print(message)

