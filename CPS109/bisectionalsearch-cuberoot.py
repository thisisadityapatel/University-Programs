#using the binary search method to find the cube root of the given number
#yeals faster output that the primitive exhaustive numeration method

number = int(input("Enter the number : "))

first = 0
last = number
mid = (first + last) / 2
error = abs(number - mid ** 3)

while error > 0.001:
    if mid ** 3 > number:
        last = mid
    else:
        first = mid
    mid = ( first + last )/2
    error = abs(number - mid ** 3)
    print(mid)

