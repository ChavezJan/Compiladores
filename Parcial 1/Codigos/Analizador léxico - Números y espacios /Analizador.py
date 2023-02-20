"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""
import os
from sys import exit

def main() -> None:
    numberList =[]
    newText, numberList, numberOfLines= fileReader()
    fileCreate()
    fileWrite(newText)

    printList(numberList)
    print("Lines: " + str(numberOfLines))


def printList(list) -> None:
    for i in list:
        print(i)

"""
    Create the new File.
"""
def fileCreate() -> None:
    if os.path.exists("newTest.txt"):
        print("The file does exist.")
        print("Deleting...")
        os.remove("newTest.txt")
        fileCreate()
    else:
        print("The file does not exist.")
        print("Creating...")
        newFile = open("newTest.txt","x")

"""
    input controller for the path
"""
def enterPath() -> str:
    path = ""
    print("\nEnter the path of the file:\n")
    path = input()
    return path
"""
    Menu controller: This function is used to choose an example file
    /Users/chavez/Documents/UP/Semestre 11/Compiladores/Parcial 1/Codigos/Analizador léxico - Números y espacios /Code/test.txt

"""

def menuController() -> str:
    print("what file do you want to read?\na) python\nb) c++ \nc) choose your code\nd) End Code")
    fileName = ""
    e = inputController(input().lower(), ["a","b","c","d"])

    if(e == "a"):
        return "test.py"
    elif(e == "b"):
        return "test.cpp"
    elif(e == "c"):
        return enterPath()
    elif(e == "d"):
        exit()


def inputController(e, expected) -> str:
    if(e in expected):
        return e
    else:
        print("Choose one of the oprions")
        return menuController()
"""
    Reads the original Code.
"""
def fileReader() -> str:

    fileName = menuController()
    fileR = ""
    numberOfLines = 1
    try:
        fileR = open(fileName,"r")
        fileR = str(fileR.read()) 

        isNumber = False
        number = ""
        numberList = []
        newFile = ""

        for i in fileR:
            if(i == "\n"):
                numberOfLines += 1
            if(i != " " ):
                isNumber = checkNumber(i, isNumber)


                if(isNumber == True ):
                    number += i
                newFile += i
            
            else:
                if(number != ""):
                    numberList.append(number)
                number = ""
        return newFile, numberList, numberOfLines    
    except:
        print("Error reading the file\n")
        exit()
    


"""
    Check if the send value is a number Digit for Digit
"""
def checkNumber(i, lastWasNumber) -> bool:
    numbers = [0,1,2,3,4,5,6,7,8,9]
    decimal = "."
    try:
        i = int(i)
        if(i in numbers):
            return True
    except:
        if(lastWasNumber and i == decimal):
            return True
        else:
            return False

    
"""
    Write the new text without Space's
"""
def fileWrite(text) -> None:
    file = open("newTest.txt","a")
    file.write(text)
    file.close()


if __name__ == '__main__':
    main()