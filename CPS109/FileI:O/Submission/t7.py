# TASK 7
# Sorting the data from the Frequency.txt file and then writing it into Decreasing_Frequency.txt
import unittest

def sorting_count(filename1, filename2):
    sort_dict = {}
    with open(filename1, "r") as file:
        lines = file.readlines()
        for line in lines:
            lst = line.split(", ")

            if len(lst) < 1:
                continue

            word = lst[0].strip()
            count = lst[1].strip()

            if word not in sort_dict:
                sort_dict[word] = 0
            sort_dict[word] = int(count)

    with open(filename2, "w") as file:
        a = sorted(sort_dict.items(), key=lambda x: x[1], reverse = True)
        for i in range(len(a)):
            file.writelines(a[i][0] + ", " + str(a[i][1]) + "\n")
    return(a)

        
output_final_answer = sorting_count("Frequency.txt", "Decreasing_Frequency.txt")
print(" Final Answer in Decreasing order.")
print()
print(output_final_answer)

#---------------------------------------------------------------------------------
#                           Testing
#---------------------------------------------------------------------------------

# The Test Cases here compare the list of the dictionary returned in decreasing order
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(sorting_count("Task7_Test1.txt", "Decreasing_Frequency_Test1.txt"), [('THE', 2178), ('WHAT', 1757), ('OF', 968), ('LANNISTER', 57), ('HOUSE', 37), ('MAN', 24), ('STARK?', 14), ('FACELESS', 7), ('ESCAPED', 2), ('PERSECUTION', 1)])

    def test2(self):
        self.assertEqual(sorting_count("Task7_Test2.txt", "Decreasing_Frequency_Test2.txt"), [('TO', 1329), ('JON', 328), ('KING', 67), ('AFTER', 62), ("ARYA'S", 46), ('WINTERFELL', 34), ('WESTEROS?', 12), ('RETURNING', 4), ('HALF-BROTHER', 4), ('HALF-BROTHER?', 4), ('EXTERMINATE', 1), ('SNOW,', 1)])

if __name__ == '__main__':
 unittest.main(exit=True)