'''
Let s be a string that contains a sequence of decimal numbers
separated by commans, e.g., s = '1.23,2.4,43.323'.  Write a program 
that prints the sum of the numbers in s.
'''

sentence = input("Enter the string : ")

#using method 1

lst = []

lst = sentence.split(",")

sum = 0
for n in lst:
    sum = sum + float(n)

print(sum)

#using method 2

sum = 0
new = ""
for i in sentence:
    if i != ",":
        new = new + i.strip()
    else:
        sum = sum + float(new)
        new = ""
sum = sum + float(new)
print(sum)