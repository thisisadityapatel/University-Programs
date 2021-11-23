# TASK 1
# Counting the number of Question and Answer Pairs.
import unittest

# Counting the number of QA Pairs 
def count_QA_pairs(filename):
    a = 0
    q = 0
    with open(filename, "r", encoding = "utf-8-sig") as file:
        lines = file.readlines()
        for line in lines:
            lst = line.split(" ")
            if lst[0].upper() == "ANSWER":
                a += 1
            elif lst[0].upper() == "QUESTION":
                q+= 1
        #returning the number of QA pairs
        return min(a, q)

print()
print("Q-A Pairs in QA_Pairs.txt :" + str(count_QA_pairs("QA_Pairs.txt")))

#---------------------------------------------------------
#                         TESTING
#---------------------------------------------------------

# Task_Test1.txt and Task1_Test2.txt are the smaller version of the QA_Pairs.txt, created from my end for the sake of testing.
# Task_Test1.txt contains 4 pairs of question answers, while Task_Test2.txt contains 11 pairs of it.
# These are temperary files just for the sake of testing the t1.py program.

class myTests(unittest.TestCase):

 def test1(self):
  self.assertEqual(count_QA_pairs("Task1_Test1.txt"), 9)

 def test2(self):
  self.assertEqual(count_QA_pairs("Task1_Test2.txt"), 7)


if __name__ == '__main__':
 unittest.main(exit=True)