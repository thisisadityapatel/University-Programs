# TASK 3

# Storing all the pairs from the unique_QA_Pairs.txt into a dictionary
import unittest
import json

def file_to_dictionary(filename):
    with open(filename, "r", encoding = "utf-8-sig") as file:
        # Defining the dictionary
        dict = {}
        lines = file.readlines()
        for i in range(1, len(lines), 2):
            key = lines[i].strip()
            value = lines[i-1].strip()
            dict[key] = value #Storing such that questions -> keys and answers -> values.
        return(dict)


# Final Answer Dictionary:
Ans_Dict = file_to_dictionary("unique_QA_Pairs.txt")
with open('QA Dictionary.txt', 'w') as json_file:
    json.dump(Ans_Dict, json_file)

#---------------------------------------------------------
#                         TESTING
#---------------------------------------------------------

class myTests(unittest.TestCase):

 def test1(self):
  self.assertEqual(file_to_dictionary("Task3_Test1.txt"), {"question What male line does Arya exterminate after returning to Westeros?" : "answer Frey", "question Who is the half-brother of Arya's half-brother?" : "answer Jon Snow, King" } )

 def test2(self):
  self.assertEqual(file_to_dictionary("Task3_Test2.txt"), {'question Who has confirmed that Tyrion and Daenerys will meet face to face in The Winds of Winter?': 'answer George R. R. Martin', 'question What taboo did Tyrion loathe Joffrey?': 'answer kinslaying', 'question What have Tyrion and Jaime always been on?': 'answer good terms', 'question What did Jaime bring when Tyrion was small?': 'answer toys, barrel hoops, blocks and a carved wooden lion', "question What was Tyrion's first pony?": 'answer pony', 'question What is Tyrion Lannister pronounced?': 'answer TEER-ee-un LAN-iss-ter', 'question Who is Ser Barristan Selmy?': 'answer Ser Jaime Lannister', 'question What is the name of Lord Mace Tyrell?': 'answer Lord Petyr Baelish', 'question Who is the name of the man?': 'answer Lord Renly Baratheon', 'question What is the name of the seaworth?': 'answer Davos Seaworth'} )

if __name__ == '__main__':
    unittest.main(exit=True)





        