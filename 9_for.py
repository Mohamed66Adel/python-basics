from utils import print_separator

print_separator(1)
# todo:1 After flipping a coin 10 times you got this result,
#  result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
#  Using for loop figure out how many times you got heads

result = ["heads", "tails", "tails", "heads", "tails", "heads", "heads", "tails", "tails", "tails"]

count = 0
for r in result:
    if r == "heads":
        count += 1

print(count)

print_separator(2)
# todo:2 Print square of all numbers between 1 to 10 except even numbers
for i in range(1, 10):
    if i % 2 != 0:
        print(f"{i} squared is {i ** 2}")

print_separator(3)
# todo:3 Your monthly expense list (from Jan to May)
#  expense_list = [2340, 2500, 2100, 3100, 2980]
#  Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
#  If expense is not found then it should print that as well.

expense_list = [2340, 2500, 2100, 3100, 2980]
expense_dict = {"jan": 2340, "feb": 2500, "mar": 2100, "apr": 3100, "may": 2980}
inp = int(input("Enter an expense amount: "))

month = None
for m, expense in expense_dict.items():
    if inp == expense:
        month = m
        break
print(f"Expense of {inp} {f'occurred in {month}' if month else 'not found in any month'}")

print_separator(4)
# todo:4 Lets say you are running a 5 km race.
#  Write a program that, Upon completing each 1 km asks you "are you tired?"
#  If you reply "yes" then it should break and print "you didn't finish the race"
#  If you reply "no" then it should continue and ask "are you tired" on every km
#  If you finish all 5 km then it should print congratulations message

race = 5
done = True
for i in range(race):
    ans = input("Are you tired? ").lower()
    if ans == "yes":
        print("You didn't finish the race")
        done = False
        break
if done:
    print(f"Congratulations you've finished the {race}km race")

print_separator(5)
# todo:5 Write a program that prints following shape
#  *
#  **
#  ***
#  ****
#  *****

depth = 5
for i in range(1, depth + 1):
    print("*" * i)