# todo:1 Create a sample class named Employee with two attributes id and name
#       employee :
#           id
#           name
#  object initializes id and name dynamically for every Employee object created.
#   emp = Employee(1, "coder")

# todo:2 Use del property to first delete id attribute and then the entire object


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"id: {self.id}, name: {self.name}")


if __name__ == '__main__':
    emp = Employee(1, 'coder')

    emp.display()

    del emp.id
    try:
        print(emp.id)
    except AttributeError:
        print("id is not defined")

    del emp
    try:
        emp.display()
    except NameError:
        print("emp is not defined")
