# Define a class to represent companies. Companies will have a name (given at creation), a list of all sales for the year (string of a product), and a dictionary of products (strings, keys) and their prices (float like, values), as well as a list of employees. Define a function to add a new product. The function will take the name of the product and the price. Define a function to add an employee, given an employee. Define an employee class. Employees will have a name as a string, and a company, both given at creation. They will also have a role given at creation. A role is represented by a number, with 1 being a new hire, and 10 the ceo. Make the role value optional, with the default set to 1.

class Company:
    def __init__(self, name):
        self.name = name
        self.sales = []
        self.products = {}
        self.employees = []

    def add_product(self, name, price):
        self.products[name] = price

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee:
    def __init__(self, name, company, role=1):
        self.name = name
        self.company = company
        self.role = role
