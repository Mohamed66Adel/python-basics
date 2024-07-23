# todo:1 You have a football field that is 92 meter long and 48.8 meter wide.\
#  Find out total area using python and print it.

length = 92.0
width = 48.8

print(f"The total area of the football field is {round(length * width, 2)} m2", )

# todo:2 You bought 9 packets of potato chips from a store.\
#  Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.\
#  Find out using python, how many dollars is the shopkeeper going to give you back?
packet_cost = 1.49
packets = 9
total_cost = packet_cost * packets
money_given = 20
print(f"the shopkeeper will give back {round(money_given - total_cost, 2)} dollars")

# todo:3 You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.\
#  If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.\
#  Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
area = 5.5 ** 2
cost_per_square_feet = 500
total_cost = area * cost_per_square_feet
print(f"The total cost to replace all tiles is {round(total_cost, 2)} rs")

# todo:4 Print binary representation of number 17
number = 17
binary_representation = f'{number:b}'
print(f"The binary representation of {number} is {binary_representation}")
