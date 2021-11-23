# TASK 4 
# Writing all the data from the unique_QA_Pairs dictionary into the Questions.txt file

import unittest
from t3 import file_to_dictionary

def Transfering_QA(filename1, filename2, transfer):
    dictionary = file_to_dictionary(filename1)
    with open(filename2, "w", encoding = "utf-8-sig") as file:
        if transfer.upper() == "QUESTION":
            lst = list(dictionary.keys())
            for element in lst:
                file.writelines(element + "\n")
            return(lst)
        elif transfer.upper() == "ANSWER":
            lst = list(dictionary.values())
            for element in lst:
                file.writelines(element + "\n")
            return(lst)


#Answer Showing the list That has been written into the .txt file
print("Showing the list of Question : ")
print("------------------------------ ")
print(Transfering_QA("unique_QA_Pairs.txt", "Questions.txt", "Question"))

#---------------------------------------------------------------------
#                       TESTING
#---------------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(Transfering_QA("Task4_Test1.txt", "Questions_Task4_Test1.txt", "Question"), ["question Who is the half-brother of Arya's half-brother?", 'question Where did Arya return to?', "question Who manipulated Arya's half-brother?", 'question When did Arya kill the Night King?', 'question Who killed Cersei Lannister?', "question Who destroys King's Landing?"])
    def test2(self):
        self.assertEqual(Transfering_QA("Task4_Test2.txt", "Questions_Task4_Test2.txt", "Question"), ['question What bodyguard murdered Mycah?', 'question Who does Arya and Sansa meet?', 'question What do Arya see in the Red Keep?', 'question Who brought his army across the Narrow Sea with the Targaryen exiles?', 'question What happens to Arya after he overhears Varys and Illyrio Mopatis?', "question Who is Arya's father?", 'question What are the Starks and Lannisters?', "question Who is the recruiter for the Night's Watch?", 'question What is Arya mistaken for?', 'question What happened to Arya while fighting Jaime?'] )

if __name__ == '__main__':
    unittest.main(exit=True)






        
            





