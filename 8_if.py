from utils import *

print_separator(1)
# todo:1 Using following list of cities per country,
#  india = ["mumbai", "banglore", "chennai", "delhi"]
#  pakistan = ["lahore","karachi","islamabad"]
#  bangladesh = ["dhaka", "khulna", "rangpur"]
#  i. Write a program that asks user to enter a city name and it should tell which country the city belongs to
#  ii. Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
#  For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter a city name: ").lower()
country = None
if city in india:
    country = "India"
elif city in pakistan:
    country = "Pakistan"
elif city in bangladesh:
    country = "Bangladesh"
else:
    print("City not found")
    exit()

print(f"{city} belongs to {country}")

city1 = input("Enter first city name: ").lower()
city2 = input("Enter second city name: ").lower()

if (city1 in india) and (city2 in india):
    print("Both cities are in India")
elif (city1 in pakistan) and (city2 in pakistan):
    print("Both cities are in Pakistan")
elif (city1 in bangladesh) and (city2 in bangladesh):
    print("Both cities are in Bangladesh")
else:
    print("They don't belong to the same country")

print_separator(2)
# todo:2 Write a python program that can tell you if your sugar is normal or not.
#  Normal fasting level sugar range is 80 to 100.
#  i. Ask user to enter his fasting sugar level
#  ii. If it is below 80 to 100 range then print that sugar is low
#  iii. If it is above 100 then print that it is high otherwise print that it is normal

sugar_level = float(input("Enter your fasting sugar level: "))
if sugar_level < 80:
    print("Sugar is low")
elif sugar_level > 100:
    print("Sugar is high")
else:
    print("Sugar is normal")
