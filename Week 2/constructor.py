class data:
    def __init__(self,name,email,number):
        self.name = name
        self.email = email
        self.number = number

    def display__data(self):
        print(f"Name: {self.name}")
        print(f"Email Id: {self.email}")
        print(f"Number: {self.number}")


name = input("Enter the name of person: ")
email = input("Enter the email of person: ")
number = int(input('Enter the number of person: '))

obj = data(name,email,number)
obj.display__data()
