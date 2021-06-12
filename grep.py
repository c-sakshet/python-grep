import sys, re, os

def getListOfFiles(dir_name):
    '''
    This function recursively parses all files and directories in the given directory\
    and returns a list of pathnames to all the files in the directory.
    '''
    # paths_of_files_parsed = []
    ''' 
    code for traversing to be added
    '''
    # return paths_of_files_parsed

    pass

def getUserInput():
    search_term = sys.argv[1] #key word entered by user to search for in the file/s
    regex = "(" + search_term + ")"
    keyword = re.compile(regex, flags = re.IGNORECASE)

    list_of_files = []
    if not(os.path.isdir(sys.argv[2])):
        if (os.path.isfile(sys.argv[2])):
            list_of_files.append(sys.argv[2]) #file entered by user
        else:
            return 0, 0
    else:
        list_of_files = getListOfFiles(sys.argv[2])
    return keyword, list_of_files


def findKeyword(search_term, list_of_files):
    '''Function to search a string and return line numbers where it is found in the given file
    - Takes input from the cmd line where first argument is the string to be searched
    and the second is the file to search in
    - This function returns the line numbers where the string is found, if any, in an array.
    - returns false if not found'''

    # Variables used
    line_number = 0
    found_at_line = []  # Array to store line numbers where the given search string is found

    try:
        for file in list_of_files:
            with open(file, 'r') as search_file:
                for line_read in search_file:
                    line_number += 1  # to match the actual line number rather than the index of iterator.
                    if search_term.findall(line_read):
                        found_at_line.append((line_number, line_read.strip('\n'))) # strip new line char at end of line
                        # To Strip right spaces use the following code instead of the above line
                        # found_at_line.append((line_number, line_read.rstrip()))

    except:
        print("Exception", sys.exc_info()[0], "occurred. ")
        exit()
    
    finally:
        return found_at_line
        search_file.close()

def main():
    if len(sys.argv) < 3:
        print("An unexpected error occurred. Please follow the usage: \n\
        Linux: python3 ./find.py <search keyword> <file name> \n\
        Windows: py ./find.py <search keyword> <file name>\n\
        \
        \nNote: If searching for special characters like [!,@,#,$,%,^,&] or similar,\
        \nplease use quotes to denote the string.\n\
        E.g.: py ./find.py \"python project\" <file name>\
            ")
        exit(0)

        '''
        To Do:
        Support CLI special character input.
        '''

    
    search_term, list_of_files_obtained = getUserInput()
    if (search_term != 0):
        keyword_lines = findKeyword(search_term, list_of_files_obtained)
    else:
        return

    if not keyword_lines:
        print("The search string does not exist in the given file", sys.argv[2])
        return
        
    for entry in keyword_lines:
        print("Line Number: ", entry[0], ", Line Content: ", entry[1])
        # n = len(sys.argv)
        # print(n)

main()
