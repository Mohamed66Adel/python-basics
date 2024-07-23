from utils import *


print_separator(1)
# todo:1 Create a variable called break and assign it a value 5.\
# See what happens and find out the reason behind the behavior that you see.

# break = 5

print_separator(2)
# todo:2 Create two variables. One to store your birth year and another one to store current year.\
# Now calculate your age using these two variables

birth_year = 2001
current_year = 2024
print("My age is", current_year - birth_year)

print_separator(3)
# todo:3 Store your first, middle and last name in three different variables and then print your full name using these variables

first_name = "Mohamed"
middle_name = "Adel"
last_name = "Mohamed"

print(first_name, middle_name, last_name)
print_separator(4)
# todo:4 Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue
names = ["_nation", "1record", "record1", "record_one", "record-one", "record^one", "continue"]
valid_names = []    # valid names [_nation, record1, record_one]
invalid_names = []  # invalid names [1record, record-one, record^one, continue]

for name in names:
    try:
        exec(f"{name} = 1")
        valid_names.append(name)
    except SyntaxError:
        invalid_names.append(name)

print("Valid names:", valid_names)
print("Invalid names:", invalid_names)
