#intersection of tuples

def intersection(t1, t2):
    result = ()
    for i in t1:
        if i in t2 and i not in result:
            result = result + (i, )
    return tuple(sorted(result))

def main():
    tuple1 = (2, 3, 4, 5)
    tuple2 = (-2, 3, 5, -9)
    print(intersection(tuple1, tuple2))

if __name__ == "__main__":
    main()
