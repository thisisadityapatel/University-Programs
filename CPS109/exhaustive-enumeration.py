n = int(input("Enter the number : "))

for i in range(abs(n)):
    if i ** 3 == abs(n):
        break

if i ** 3 == abs(n):
    if n < 0:
        i = -i
    print(i)
    
else:
    print("No perfect cube root exists")
