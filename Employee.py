from Person import Person


class Employee(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)  # Call the superclass constructor to set name and age
        self.company = company       # Additional property for the employee's company
        self.salary = salary         # Additional property for the employee's salary

    def display(self):
        # First, call the display method of the superclass to print name and age
        super().display()
        # Then, print the additional details specific to the Employee class
        print(f"Company: {self.company}, Salary: ${self.salary}")
