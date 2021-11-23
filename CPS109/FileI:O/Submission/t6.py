# TASK 6
# Counting the frequency of words in the unique_QA_Pairs.txt file and writing it in the Frequency.txt file

import unittest
def frequency_of_words(filename1, filename2):
    fre_dict = {}
    with open(filename1, "r", encoding = "utf-8-sig") as f1, open(filename2, "w") as f2:
        lines = f1.readlines()
        
        for line in lines:
            lst = line.split(" ")
            for word in lst:
                word = word.upper().strip()
                if word not in fre_dict:
                    fre_dict[word] = 0
                fre_dict[word] += 1

        for i in fre_dict:
            f2.writelines(i + ", " + str(fre_dict[i]) + "\n")
        
        return(fre_dict)

print(frequency_of_words("unique_QA_Pairs.txt", "Frequency.txt"))

#-----------------------------------------------------------------
#                       TESTING
#-----------------------------------------------------------------
class myTests(unittest.TestCase):

 def test1(self):
  self.assertEqual(frequency_of_words("Task6_Test1.txt", "Frequency_Task6_Test1.txt"), {'ANSWER': 2, 'LADY': 1, 'CATELYN': 1, 'STARK': 1, 'QUESTION': 2, 'WHO': 2, 'IS': 1, 'ARYA': 1, "STARK'S": 1, 'WIFE?': 1, 'HOUSE': 2, 'LANNISTER': 1, 'ESCAPED': 1, 'THE': 1, 'PERSECUTION': 1, 'OF': 1, 'STARK?': 1})

 def test2(self):
  self.assertEqual(frequency_of_words("Task6_Test2.txt", "Frequency_Task6_Test2.txt"), {'ANSWER': 6, 'THE': 4, 'BATTLE': 1, 'OF': 2, 'WINTERFELL': 1, 'QUESTION': 6, 'WHEN': 1, 'DID': 1, 'ARYA': 4, 'KILL': 1, 'NIGHT': 1, 'KING?': 1, 'SANDOR': 2, 'CLEGANE': 1, 'WHO': 4, 'KILLED': 1, 'CERSEI': 1, 'LANNISTER?': 1, 'DAENERYS': 1, 'TARGARYEN': 1, 'DESTROYS': 1, "KING'S": 1, 'LANDING?': 1, 'CONVINCES': 1, 'TO': 5, 'ABANDON': 1, 'HER': 2, 'QUEST': 1, 'FOR': 1, 'VENGEANCE?': 1, "ARYA'S": 1, 'YOUNGER': 1, 'BROTHER': 1, 'BRAN': 1, 'IS': 1, 'CHOSEN': 1, 'AS': 1, 'KING': 1, 'IN': 1, 'WESTEROS?': 1, 'DECIDES': 1, 'LEAVE': 2, 'WESTEROS': 2, 'AND': 1, 'SAIL': 1, 'WEST': 1, 'DISCOVER': 1, 'WHAT': 2, 'LIES': 1, 'BEYOND': 1, 'WHERE': 1, 'MAPS': 1, 'KNOWN': 1, 'WORLD': 1, 'END.': 1, 'DOES': 1, 'DECIDE': 1, 'AFTER': 1, 'BIDDING': 1, 'FAREWELL': 1, 'SIBLINGS?': 1})


if __name__ == '__main__':
 unittest.main(exit=True)




    