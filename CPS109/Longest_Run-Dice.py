'''
1. A run is a sequence of adjacent repeated values. Write a program that generates a sequence of 20 random die tosses and then prints the die values, marking the runs by including them in parentheses, like this:
1 2 (5 5) 3 1 2 4 3 (2 2 2 2) 3 6 (5 5) 6 3 1 Use the following pseudocode:
Set a boolean variable inRun to false. For each valid index i in the list
if inRun
    If values[i] is different from the preceding value
        Print ) inRun = false
Else
    if values[i] is the same as the following value
    print (
    inRun = true Print values[i]
If inRun, print )
Recall from lab6, that random.randrange(0, 50) would give a random value from 0 to 49, inclusive. Die values are, of course, from 1 to 6, inclusive.
'''
import random

#creating the list for storing all the rendom numbers
values = []

for i in range(20):
    number = random.randrange(1, 7)
    values.append(number)

#now solving the problem
inRun = False
for i in range(len(values)-1):
        if inRun == True:
            if values[i] != values[i-1]:
                print(")", end="")
                inRun = False
        if inRun == False:
            if values[i] == values[i+1]:
                print("(", end="")
                inRun = True
        print(values[i],end="")

if inRun == True:
    if values[len(values) - 1] != values[len(values)-2]:
        print(")", end="")
        print(values[len(values)-1], end="")
    else:
        print(values[len(values)-1], end="")
        print(")",end="")

else:
    print(values[len(values)-1], end="")

print()



    

