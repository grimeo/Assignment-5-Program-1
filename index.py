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
    if float(m) < 0 or float(m) > 100:
        mark = m

def setDescription(d):
    global description
    description = d




getInput()