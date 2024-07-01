#PROTECTED MEMBER

class Company:
    def __init__(self):
        self._project = "LMS" #as a programmer, we should respect that
                              #_project is a protected member
                              #this is more of a concept th an a functionality
                              #wala talaga tong restriction. Sa private lang meron

class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name:",self.name)
        print("Working on project:", self._project)

#main
dalisay = Employee("Kyla Dalisay")
dalisay.show()
dalisay._project = "HRIS" 
print("Project:",dalisay._project)
    