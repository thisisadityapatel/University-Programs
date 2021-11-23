# TASK 2

'''
Are these pairs unique? For example: (q1, a1) (q1, a1) are identical and overlapping; (q1, a1) (q1, a2) are overlapping,
and (q1, a1) (q2, a1) are overlapping as well. If not unique, find the overlapping pairs, 
and generate a unique_QA_Pairs.txt file and an Overlapping.txt file. 
The format of unique_QA_Pairs.txt and Overlapping.txt are the same as QA_Pairs.txt.
For (q1, a1) (q1, a1), keep (q1, a1) once; put (q1, a1) in Overlapping.txt.
For (q1, a1) (q1, a2) and (q1, a1) (q2, a1) , keep (q1, a1) (i.e., 
the first occurrence of a pair with q1) and delete the others; put (q1, a1), (q1, a2) and (q2, a1) in Overlapping.txt.
'''
import unittest

#Question 2 Temp Trial
def saperating_unique_overlapping(filename1, filename2, filename3):
    with open(filename1, "r", encoding = "utf-8-sig") as f1, open(filename2, "w", encoding = "utf-8-sig") as f2, open(filename3, "w", encoding = "utf-8-sig") as f3:
        lines = f1.readlines()
    
        #appending all the questions and their answers into individual lists and assigning them the number
        qlst = []
        qflag = []
        alst = []
        aflag = []

        #Writing all the combinations of the  questions and answers into respective lists alongside their flags
        for i in range(1, len(lines), 2):
            if lines[i] in qlst:
                qlst.append(lines[i])
                qflag.append(1)
            else:
                qlst.append(lines[i])
                qflag.append(0)
            if lines[i-1] in alst:
                alst.append(lines[i-1])
                aflag.append(1)
            else:
                alst.append(lines[i-1])
                aflag.append(0)

        #Now writing the pairs into the respective files.
        for i in range(len(qlst)):
            #Checking for unique conditions
            if qflag[i] == 0 and aflag[i] == 0:
                f2.writelines(alst[i])
                f2.writelines(qlst[i])
        
            #Rest of the conditions
            elif qflag[i] == 1 or aflag[i] == 1 :
                f3.writelines(alst[i])
                f3.writelines(qlst[i])
        return([qflag, aflag])

#Getting the Flag list of the two outputs
ouput_answer = saperating_unique_overlapping("QA_Pairs.txt", "unique_QA_Pairs.txt", "Overlapping.txt") 


#-----------------------------------------------------------------------------------------------------------
#                                       TESTING
#-----------------------------------------------------------------------------------------------------------
# Test cases: Here the functions returns us a list conatining two list, that are the flags of questions and answers.
# If the flag value is one, it means that the question / answer ahs been repeated and hence consequently be transfered into the 
# overlapping.txt file while the ones with 0 flag would be transfered into the unique_QA_Pairs.txt file.

class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(saperating_unique_overlapping("Task2_Test1.txt", "unique_QA_Pairs_Test1.txt", "Overlapping_Test1.txt"), [[0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1]])

    def test2(self):
        self.assertEqual(saperating_unique_overlapping("Task2_Test2.txt", "unique_QA_Pairs_Test2.txt", "Overlapping_Test2.txt"), [[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]])

if __name__ == '__main__': 
 unittest.main(exit=True)






        
        

        



            
                
                

