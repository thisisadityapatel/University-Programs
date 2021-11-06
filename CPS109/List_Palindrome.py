'''
5. Write a function isPal(L), where L is a list of integers, and the function returns True if the list is a palindrome, 
False otherwise. For example [5, 2, 9, 9, 2 5] is a palindrome. Use the reverse() method of list and check if the reversed 
list is the same as the original list.
'''

def isPal(L):
    #Using the reverse function:
    L1 = list(L)
    L.reverse()
    if L1 == L:
        return True
    else:
        return False

def main():
    list1 = [5, 2, 9, 9, 2, 5]
    print(f"{list1}, palindrome: {isPal(list1)}")
    
    list2 = [2, 3, 4, 5, 4, 3, 2, 1]
    print(f"{list2}, palindrome: {isPal(list2)}")
    
    list3 = [2, 3, 4, 4, 3, 2]
    print(f"{list3}, palindrome: {isPal(list3)}")

if __name__ == "__main__":
    main()