# Fibonacci Series using recursion function

def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

def main():
    print(fib(4))

if __name__ == "__main__":
    main()