import sys

def userInput():
    searchTerm = sys.argv[1]
    fileName = sys.argv[2]
    return searchTerm, fileName

def find(searchTerm, fileName):
    '''Function to search a string and return line numbers where it is found in the given file
    - Takes input from the cmd line where first argument is the string to be searched 
    and the second is the file to search in
    - This function returns the line numbers where the string is found, if any, in an array.
    - returns false if not found'''
    
    # Variables used
    lineNumber = 0
    foundAtLine = [] #Array to store line numbers where the given search string is found
    
    with open(fileName, 'r') as searchFile:
        for lineRead in searchFile:
            lineNumber += 1 #to match the actual line number rather than the index of iterator.
            if (searchTerm in lineRead):
                foundAtLine.append(lineNumber)

    if not foundAtLine:
        print("The search string does not exist in the given file", sys.argv[2]) 
        return 

    return foundAtLine

searchTerm, fileName = userInput()
findLines = find(searchTerm, fileName)

# n = len(sys.argv)
# print(n)