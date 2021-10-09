# 2.3 Branching Programs : largest odd problem

# Write a program that examines variables x, y, z
# and prints the largest odd number among them.
# If none are odd, then print None
#----------------------------------
largest = None
x = int(input("Enter x : "))
y = int(input("Enter y : "))
z = int(input("Enter z : "))

if x % 2 != 0:
    if y % 2 != 0:
        if z % 2 != 0:
            largest = max(x, y, z)
        largest = max(x ,y)
    largest = x

if  y % 2 != 0:
    if z % 2 != 0:
        largest = max(y, z)
    largest = y

if z % 2 != 0:
    largest = z

if largest == None:
    print("No odd numbers present")

elif largest != None:
    print(largest)