import sys


def getUserInput():
    search_term = sys.argv[1]
    file_name = sys.argv[2]
    return search_term, file_name


def findKeyword(search_term, file_name):
    '''Function to search a string and return line numbers where it is found in the given file
    - Takes input from the cmd line where first argument is the string to be searched
    and the second is the file to search in
    - This function returns the line numbers where the string is found, if any, in an array.
    - returns false if not found'''

    # Variables used
    line_number = 0
    found_at_line = []  # Array to store line numbers where the given search string is found

    with open(file_name, 'r') as searchFile:
        for line_read in searchFile:
            line_number += 1  # to match the actual line number rather than the index of iterator.
            if search_term in line_read:
                found_at_line.append((line_number, line_read.strip('\n'))) # strip new line char at end of line
                # To Strip right spaces use the following code instead of the above line
                # found_at_line.append((line_number, line_read.rstrip()))
    return found_at_line


def main():
    if len(sys.argv) < 3:
        print("Please follow usage: python3 ./find.py <search keyword> <file name>")
        return
    search_term, file_name = getUserInput()
    keyword_lines = findKeyword(search_term, file_name)
    if not keyword_lines:
        print("The search string does not exist in the given file", sys.argv[2])
        return
    for entry in keyword_lines:
        print("Line Number: ", entry[0], ", Line Content: ", entry[1])
        # n = len(sys.argv)
        # print(n)

main()
