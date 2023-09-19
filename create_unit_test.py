# create a function that takes a file as input and adds unit tests to that file by calling create_unit_test

from chat_gpt import create_unit_test

def add_unit_tests_to_file(file_name):
    # read the content of the file
    with open(file_name, 'r') as f:
        content = f.read()
       # call the function create_unit_test with the content of the file
        unit_test = create_unit_test(content)
        # append the unit test at the end of the file
        with open(file_name, 'a') as f:
            f.write(unit_test)

   
# call the function
add_unit_tests_to_file('functions.py')