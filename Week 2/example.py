'''
Write a program to create a class called Emp , having an instance members called name , age and sal . 
Also declare a class variable called raise_amount to store the increment percentage of sal and set 
it the value given by the user

Now provide following methods in your class
__init___() : This method should initialize instance members  with the parameter passed

increase_sal(): This method should calculate the increment in sal and add it to the instance member sal

display(): This method should display name , age and sal of the employee

Finally , in the main script , create 2 Emp objects , initialize them and increase their salary . Finally display the data

'''
class emp:
    raise_amount = 25
    def __init__(self,name,age,sal):
        self.name = name    
        self.age = age
        self.sal = sal

    def increament_sal(self):
        self.sal += self.sal*(emp.raise_amount/100)
    
    def display(self):
        print(f"Name of employee is: {self.name}")
        print(f"Age of Employee is: {self.age}")
        print(f"Salary of Employee is {self.sal}")


    
name = input("Enter the Name of Employee: ")
age = int(input("Enter the age of employee: "))
salary = int(input("Enter the salary of Employee: "))

obj = emp(name,age,salary)
obj.increase_sal()
obj.display()



