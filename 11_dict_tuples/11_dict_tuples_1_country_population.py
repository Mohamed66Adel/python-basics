# todo: We have following information on countries and their population (population is in crores),
#  |Country	 | Population|
#  |China	 | 143       |
#  |India	 | 136       |
#  |USA	     | 32        |
#  |Pakistan | 21        |
#  i. Using above create a dictionary of countries and its population
#  ii.Write a program that asks user for three type of inputs,
#    a. print: if user enter print then it should print all countries with their population in this format,
#       china==>143
#       india==>136
#       usa==>32
#       pakistan==>21
#    b. add: if user input add then it should further ask for a country name to add.
#       If country already exist in our dataset then it should print that it exist and do nothing.
#       If it doesn't then it asks for population and add that new country/population in our dictionary and print it
#    c. remove: when user inputs remove it should ask for a country to remove.
#       If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
#    d. query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.

# Using Command Design Pattern
from abc import ABC, abstractmethod


# [1] Commands classes
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class PrintCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.print_population()


class AddCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.add_country()


class RemoveCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.remove_country()


class QueryCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.print_pop()


# [2] Receiver Class
class PopulationManager:
    def __init__(self):
        self.population = {"China": 143, "India": 136, "USA": 32, "Pakistan": 21}

    def print_population(self):
        for country, pop in self.population.items():
            print(country, pop, sep='==>')

    def add_country(self):
        country = input("Enter country name: ").capitalize()
        if country in self.population:
            print(f'{country} already exists!')
        else:
            pop = int(input("Enter population: "))
            self.population[country] = pop
            self.print_population()

    def remove_country(self):
        country = input("Enter country name: ").capitalize()
        if country in self.population:
            del self.population[country]
            self.print_population()
        else:
            print(f"{country} doesn't exist!")

    def print_pop(self):
        country = input("Enter country: ").capitalize()
        if country in self.population:
            print(self.population[country])
        else:
            print(f"{country} doesn't exist")


# [3] Invoker Class
class CommandInvoker:
    def __init__(self):
        self.commands = {str: Command}

    def register_command(self, command_name, command):
        self.commands[command_name] = command

    def execute_command(self, command_name):
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print("Invalid command!")


if __name__ == '__main__':
    receiver = PopulationManager()
    invoker = CommandInvoker()

    invoker.register_command('print', PrintCommand(receiver))
    invoker.register_command('add', AddCommand(receiver))
    invoker.register_command('remove', RemoveCommand(receiver))
    invoker.register_command('query', QueryCommand(receiver))

    command = input("Enter command (print, add, remove, query): ").strip().lower()
    invoker.execute_command(command)
