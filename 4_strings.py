from utils import *


print_separator(1)
# todo:1 Create 3 variables to store street, city and country, now create address variable to store entire address.\
#  Use two ways of creating this variable, one using + operator and the other using f-string.
#  Now Print the address in such a way that the street, city and country prints in a separate line
street = "Sea-street"
city = "basyoun"
country = "Egypt"

address1 = street + "\n" + city + "\n" + country
address2 = f"{street}\n{city}\n{country}"

print(address1, address2, sep="\n\n")

print_separator(2)
# todo:2 Create a variable to store the string "Earth revolves around the sun"
#  Print "revolves" using slice operator
#  Print "sun" using negative index
sentence = "Earth revolves around the sun"
print(sentence[6:14])
print(sentence[-3:])

print_separator(3)
# todo:3 Create two variables to store how many fruits and vegetables you eat in a day.
#  Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
#  Use python f string for this.
fruits_n = 2
vegetables_n = 3

print(f"I eat {vegetables_n} veggies and {fruits_n} fruits daily")

print_separator(4)
# todo:4 I have a string variable called s='maine 200 banana khaye'.
#  This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
#  Replace incorrect words in original string with new ones and print the new string.
#  Also try to do this in one line.
s = 'maine 200 banana khaye'
s = s.replace("200 banana", "10 samosa")
print(s)
