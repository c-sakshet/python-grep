import sys, re, os

def get_user_input():
    search_term = sys.argv[1] #key word entered by user to search for in the file/s
    input_file = sys.argv[2]
    return search_term, input_file

def create_re_keyword(keyword):
    regex = "(" + keyword + ")"
    re_keyword = re.compile(regex, flags = re.IGNORECASE)
    return re_keyword

def get_parsed_files(dir_name):
    '''
    This function recursively parses all files and directories in the given directory\
    and returns a list of pathnames to all the files in the directory.
    '''
    # print("Inside get parsed files")
    parsed_files = list()
    ''' 
    code for traversing to be added
    '''
    return parsed_files.append(dir_name)

def check_file_type(dir_name):
    ''' This function checks if input is a file or directory'''
    flag = 0    #Toggle for file type: 0 - file, 1 - directory

    if not(os.path.isdir(dir_name)):
        if (os.path.isfile(dir_name)):
            flag = 0            
        else:
            raise Exception("No such file or directory.")
    else:
        flag = 1       

    return flag

def get_list_of_files(dir_name):
    '''
    This function returns
    '''
    paths_of_files = list()
    flag = check_file_type(dir_name)

    if(flag == 0): #input is a file
        paths_of_files.append(dir_name)    #file entered by user
    else:
        paths_of_files = get_parsed_files(dir_name)

    return paths_of_files

def find_keyword(search_term, input_file):
    '''Function to search a string and return line numbers where it is found in the given file
    - Takes input from the cmd line where first argument is the string to be searched
    and the second is the file to search in
    - This function returns the line numbers where the string is found, if any, in an array.
    - returns false if not found'''

    # Variables used
    line_number = 1
    found_at_line = list() # Array to store line numbers where the given search string is found

    #Check for all files if input is a directory:
    list_of_files = get_list_of_files(input_file)
    
    #Create a keyword pattern object
    re_keyword = create_re_keyword(search_term)
    
    try:
        for current_file in list_of_files:
            with open(current_file, 'r') as search_file:
                for line_read in search_file:
                    line_number += 1  # First iterator to match the actual line number rather than the index of iterator.
                    if re_keyword.findall(line_read):
                        found_at_line.append((current_file, line_number, line_read.strip('\n'))) # strip new line char at end of line
                            # To Strip right spaces use the following code instead of the above line
                            # found_at_line.append((line_number, line_read.rstrip()))
    except FileNotFoundError as file_not_found:
        raise Exception("Exception", sys.exc_info()[1],"orrurred.")
    except:
        raise Exception("Exception", sys.exc_info()[1],"orrurred.")
    finally:
        return found_at_line

def print_output(keyword_lines):
    print ("File\t\tLine\tContent\t")
    for entry in keyword_lines:
        print("{}\t\t[{}]\t{}" .format(entry[0], entry[1], entry[2]))

def main():
    if len(sys.argv) < 3:
        # print(sys.argv[1:])
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
    - Support CLI special character input - & without quotes.
    - Handle error caused by user input consisting of special characters like &, $.
    '''

    search_term, list_of_files_obtained = get_user_input()    #get cli arguments from user

    keyword_lines = find_keyword(search_term, list_of_files_obtained) #execute python-grep function
    if not keyword_lines:
        print("The search string does not exist in the given file or directory.")
        return

    print_output(keyword_lines)    
    # for entry in keyword_lines:
    #     print("{} - Line Number: {} ::  {}" .format(entry[0], entry[1], entry[2]))

    # '''
    # syntax for color highlight - print("\033[38;5;196m{} \033[0;0m\n".format(<text to highlight>))
    # '''
    # n = len(sys.argv)
    # print(n)

main()
