#multiplication recursion

def multiply(a, b):
    if b == 1:
        return a
    return a + multiply(a, b-1)

def main():
    print(multiply(2, 3))

if __name__ == "__main__":
    main()