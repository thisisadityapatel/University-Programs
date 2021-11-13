#Herons formula 

number = -1
while number < 0:
    number = int(input("Enter the number : "))

guess = number / 2
epsilon = 0.001
error = abs(number - (guess ** 2))

while error > epsilon:
    guess = (guess + (number / guess)) / 2
    error = abs(number - (guess ** 2))
    
print("Root : ", guess)