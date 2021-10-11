#finding suare root of a numbers using the bisectional search method
#the besectional search method is faster that the exhaustive numeration methd and hence the ouput time is much more fast

number = int(input("Enter the number : "))

first = 0
last = number
mid = (first+last)/2
error = abs(number - mid**2)
epsilon = 0.001
while error > epsilon:
    print(mid)
    if mid ** 2 > number:
        last = mid
    else:
        first = mid
    mid = (first + last) / 2
    error = abs(number - mid ** 2)
    print(mid)
    










