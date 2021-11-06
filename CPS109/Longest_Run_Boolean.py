'''
3. Assume that L is a list of Boolean values, True and False. Write a function longestFalse(L) which returns a tuple (start, end) 
representing the start and end indices of the longest run of False values in L. If there is a tie, then return the first such run. 
For example, if L is
False False True False False False False True True False False 
0       1     2     3   4       5   6      7    8   9       10
then the function would return (3, 6), since the longest run of False is from 3 to 6.
'''
import random
def longestFalse(L):
    run = (0, 0)
    inRun = False
    longest_run = (0, 0)

    for i, j in enumerate(L):
        if inRun and j:
            run = (run[0], i - 1)
            inRun = False

            if run[1] - run[0] > longest_run[1] - longest_run[0]:
                longest_run = run
        if not inRun and not j:
            run = (i, run[1])
            inRun = True

    return(longest_run)

def main():
    l = random.choices([True, False], k=10)
    print(l)
    print(longestFalse(l))

if __name__ == "__main__":
    main()