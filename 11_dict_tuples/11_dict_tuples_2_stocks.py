# todo: You are given following list of stocks and their prices in last 3 days,
#       Stock	Prices
#       info	[600,630,620]
#       ril	    [1430,1490,1567]
#       mtl 	[234,180,160]
#  Write a program that asks user for operation. Value of operations could be,
#   i. print: When user enters print it should print following,
#       info ==> [600, 630, 620] ==> avg:  616.67
#       ril ==> [1430, 1490, 1567] ==> avg:  1495.67
#       mtl ==> [234, 180, 160] ==> avg:  191.33
#   ii.add: When user enters 'add', it asks for stock ticker and price.
#   If stock already exist in your list (like info, ril etc) then it will append the price to the list.
#   Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

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
        self.receiver.print_stocks()


class AddCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.add_stock()


# [2] Receiver Class
class StockManager:
    def __init__(self):
        self.stocks = {"info": [600, 630, 620],
                       "ril": [1430, 1490, 1567],
                       "mtl": [234, 180, 160]}

    def print_stocks(self):
        for stock, prices in self.stocks.items():
            print(stock, prices, f"avg:  {sum(prices) / len(prices): .2f}", sep=' ==> ')

    def add_stock(self):
        ticker = input("Enter stock ticker: ").lower()
        price = float(input("Enter stock price: "))
        if ticker in self.stocks:
            self.stocks[ticker].append(price)
        else:
            self.stocks[ticker] = [price]
        self.print_stocks()


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
    receiver = StockManager()
    invoker = CommandInvoker()

    invoker.register_command('print', PrintCommand(receiver))
    invoker.register_command('add', AddCommand(receiver))

    command = input("Enter command (print, add): ").strip().lower()
    invoker.execute_command(command)

