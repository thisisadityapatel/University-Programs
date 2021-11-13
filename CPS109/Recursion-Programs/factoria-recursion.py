#Factorial recursion program
def factorial(x):
    if x == 1:
        return 1
    product = x * factorial(x - 1)
    return product

def main():
    print("factorial of 10 : ", factorial(10))
    print("factorial of 5 : ", factorial(5))

if __name__ == "__main__":
    main()
    


