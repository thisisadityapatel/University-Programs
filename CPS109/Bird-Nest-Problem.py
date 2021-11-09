'''
QUESTION 4
'''
import random
def longestFalse(L):
    run = (0, 0)
    max_run = run
    in_run = False
    
    for i, j in enumerate(L):
        if in_run and j:
            run = (run[0], i-1)
            in_run = False

            if run[1] - run[0] > max_run[1] - max_run[0] or run[1] - run[0] == 0:
                max_run = run

        if not in_run and not j:
            run = (i, run[1])
            in_run = True
    
    if in_run:
        run = (run[0], len(L) - 1)
        if run[1] - run[0] > max_run[1] - max_run[0]:
            max_run = run
    
    return(max_run)

print(longestFalse([(True, False)[random.randrange(0, 2)] for i in range(10)]))

def occupy(n):
    L = [False for i in range(n)]
    print(L)
    for i in range(n-1):
        empty = longestFalse(L)
        L[(empty[1] + empty[0])//2] = True
        for i in L:
            if i:
                print("X", end=" ")
            else:
                print("_", end=" ")
        print()

    L[-1] = True
    for i in L:
            if i:
                print("X", end=" ")
            else:
                print("_", end=" ")

occupy(11)
