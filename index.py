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
    if m < 0 or m > 100:
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

def printDetails():
    print("Input grade: "+ str(input_Grade) + "\nGrade/Mark: " + str(mark) + "\nDescription: " + description)

getInput()
solve()
printDetails()