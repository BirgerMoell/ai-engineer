# create a function that takes a file as input and adds unit tests to that file by calling create_unit_test
import sys
from chat_gpt import create_unit_test, code_review

def add_unit_tests_to_file(file_name):
    # read the content of the file
    with open(file_name, 'r') as f:
        content = f.read()
       # call the function create_unit_test with the content of the file
        unit_test = create_unit_test(content)
        # append the unit test at the end of the file
        with open(file_name, 'a') as f:
            f.write(unit_test)

   
# code review
def code_review_file(filename):
    # read the file
    with open(filename, 'r') as f:
        content = f.read()
        print("the content of the file is", content)
        
        # call the open AI api
        response = code_review(content)
        # create a new file named filename + _review with the comment
        with open(filename + '_review', 'w') as f:
            f.write(response)
        print(response)
        return response
# call the function
#add_unit_tests_to_file('functions.py')
# code_review_file('functions.py')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        code_review_file(file_name)
    else:
        print("Please provide a file name as an argument.")