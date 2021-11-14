#using the yield function for finding the fibonacci series

def fib():
    yield 1
    yield 1
    a, b = 1, 1
    while True:
        a, b = b, a+b
        yield b

def main():
    x = int(input("Enter the index at which the fibonacci series is to be found : "))
    for i in fib():
        if i >= x:
            break
    print(i)

if __name__ == "__main__":
    main()