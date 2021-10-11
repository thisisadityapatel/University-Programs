# Write a program that asks the use for an integer and prints
# two integers, root and power, such that 1 < power < 6
# and root ** power is equal to the integer entered by the user.
# If no such pair of integers exists, it should print a message
# to that effect.

number = int(input("Enter the number : "))

ans = None

for power in range(2, 6):
    for root in range(number):
        if root ** power == number:
            ans = (root, power)
        if root ** power > number:
            break

if ans == None:
    print("No Combination exists")
else:
    print(ans)

