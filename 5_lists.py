from utils import *

print_separator(1)
# todo:1 Let us say your expense for every month are listed below,
#  January - 2200
#  February - 2350
#  March - 2600
#  April - 2130
#  May - 2190
#  Create a list to store these monthly expenses and using that find out,
#  1. In Feb, how many dollars you spent extra compare to January?
#  2. Find out your total expense in first quarter (first three months) of the year.
#  3. Find out if you spent exactly 2000 dollars in any month
#  4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#  5. You returned an item that you bought in a month of April and got a refund of 200$.
#     Make a correction to your monthly expense list based on this

expenses = [2200, 2350, 2600, 2130, 2190]
print(f"1. In Feb, I spent {expenses[1] - expenses[0]} dollars extra compared to January")
print(f"2. My total expense in the first quarter is {sum(expenses[:3])} dollars")
print(f"3. I spent exactly 2000 dollars in {sum([1 if v == 2000 else 0 for v in expenses])} months")
expenses.append(1980)
expenses[3] -= 200

print_separator(2)
# todo:2 You have a list of your favourite marvel super heros.
#  heros = ['spider man','thor','hulk','iron man','captain america']
#  Using this find out,
#  1. Length of the list
#  2. Add 'black panther' at the end of this list
#  3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
#  4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
#  5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print(f"1. The length of the list is {len(heros)}")
heros.append("black panther")
print(f"2. The list after adding 'black panther' at the end is \n{heros}")
heros.pop()
heros.insert(3, "black panther")
print(f"3. The list after adding 'black panther' after 'hulk' is \n{heros}")
heros[1:3] = ["doctor strange"]
print(f"4. The list after replacing 'thor' and 'hulk' with 'doctor strange' is \n{heros}")

# print(help(heros.sort))
heros.sort()
print(f"5. The list after sorting in alphabetical order is \n{heros}")
