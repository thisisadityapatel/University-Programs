# Define a fucntion which upon entering the idex od the element gives the value of the element in the fibonacci series

def fib(n):
    if n == 0:
        return None
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    if n > 2:
        for i in range(3, n+1):
            a, b = b, a+b
        return b

def main():
    print(fib(7))

if __name__ == "__main__":
    main()

