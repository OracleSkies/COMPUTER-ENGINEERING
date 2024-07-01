#PUBLIC MEMBER
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show(self):
        print("Name:", self.name,"Salary:",self.salary)

#main
emp = Employee("Kyla Dalisay",30000)
print("Name:", emp.name,"Salary:",emp.salary)
emp.show()

