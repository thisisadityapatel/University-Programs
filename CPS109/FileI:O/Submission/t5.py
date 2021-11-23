# TASK 5
# Copying all the answers into an Answers.txt file
import unittest

# Importing the Transfering_QA function from t4.py file
from t3 import file_to_dictionary
from t4 import Transfering_QA 

#Answer Showing the list That has been written into the .txt file
print()
print("Showing the list of Answer : ")
print("------------------------------ ")
print(Transfering_QA("unique_QA_Pairs.txt", "Answers.txt", "Answer"))

#---------------------------------------------------------------------
#                       TESTING
#---------------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(Transfering_QA("Task5_Test1.txt", "Answers_Task5_Test1.txt", "Answer"), ['answer archery', 'answer out-shooting him', 'answer laughs at their antics', 'answer scolded', 'answer Queen Cersei', "answer her mother's patience", 'answer Hand of the King', 'answer Nymeria', 'answer a sword', 'answer Needle', 'answer Mycah', 'answer Sansa and Joffrey', 'answer Joffrey', 'answer rocks', 'answer Crossroads Inn'])
    def test2(self):
        self.assertEqual(Transfering_QA("Task5_Test2.txt", "Answers_Task5_Test2.txt", "Answer"), ['answer Littlefinger', 'answer dragon skulls', 'answer Khal Drogo', 'answer Arya finds a passage out of the castle', 'answer angry', 'answer the wolf and the lion', 'answer Yoren', 'answer a boy'] )

if __name__ == '__main__':
    unittest.main(exit=True)
