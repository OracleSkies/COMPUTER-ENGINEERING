#PRIVATE MEMBER
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def show(self):
        print("Name:", self.name,"Salary:",self.__salary)

class Programmer(Employee):
    def __init__(self, name, salary):
        self.name = name
        Employee.__salary = salary

    def show(self):
        print("Name:", self.name,"Salary:",self.__salary)

#main
emp = Employee("Kyla Dalisay",30000)
#print("Name:", emp.name,"Salary:",emp.salary) #cannot call emp.salary kasi private member sya
emp.show() #pero gagana dito ung __salary kasi tinatawag siya inside the method of the class

