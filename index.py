# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

# encapsulate field for filtering inputs
def getInput():
    global input_Grade
    input_Grade = float(input("Enter your grade:"))

def setMark(m):
    global mark
    if input_Grade < 0 or input_Grade > 100:
        print("Out of Bounds")
        exit()
    else:
        mark = m

def setDescription(d):
    global description
    description = d

def solve():
    if input_Grade >= 97 and input_Grade <= 100:
        setMark(1.00)
        setDescription("Excellent")
    elif input_Grade >= 94 and input_Grade < 97:
        setMark(1.25)
        setDescription("Excellent")
    elif input_Grade >= 91 and input_Grade < 94:
        setMark(1.50)
        setDescription("Very Good")
    elif input_Grade >= 88 and input_Grade < 91:
        setMark(1.75)
        setDescription("Very Good")
    elif input_Grade >= 85 and input_Grade < 88:
        setMark(2.0)
        setDescription("Good")
    elif input_Grade >= 82 and input_Grade < 85:
        setMark(2.25)
        setDescription("Good")
    elif input_Grade >= 79 and input_Grade < 82:
        setMark(2.50)
        setDescription("Satisfactory")
    elif input_Grade >= 76 and input_Grade < 79:
        setMark(2.75)
        setDescription("Satisfactory")
    elif input_Grade == 75:
        setMark(3.00)
        setDescription("Passing")
    elif input_Grade >= 65 and input_Grade < 75:
        setMark(5.00)
        setDescription("Failure")
    else :
        setMark("")
        setDescription("W/D/Inc.")


def printDetails():
    print("Input grade: "+ str(input_Grade) + "\nGrade/Mark: " + str(mark) + "\nDescription: " + description)

getInput()
solve()
printDetails()