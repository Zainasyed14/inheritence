class Person:

    def __init__(self, name , idnumber):

        self.name = name
        self.idnumber = idnumber
    def PrintInfo(self):
        print(self.name , self.idnumber)

class Employee(Person):
    def __init__(self , name , idnumber , salary , post):
        self.salary = salary
        self.post = post
        super().__init__(name , idnumber)

    def Printinfo2(self):
        print(self.salary , self.post)

employee = Employee("Emily" , 331267 , "$600" , "Assistant")
employee.PrintInfo()
employee.Printinfo2()