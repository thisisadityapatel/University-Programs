x = int(input("Enter x : "))
y = int(input("Enter y : "))
z = int(input("Enter z : "))

if x %2 != 0:
    if y %2 != 0:
        if z %2 !=  0:
            print(max(x,y,z))
        print(max(x,y))
    elif z % 2 != 0:
        print(max(x,z))
    else:
        print(x)

elif y %2 != 0:
    if z %2 !=  0:
        print(max(y,z))
    print(y)

elif z % 2 != 0:
    print(z)

else:
    print("None")
    
     