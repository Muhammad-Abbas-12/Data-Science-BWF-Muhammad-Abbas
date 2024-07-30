# this module combines class Amin , User and Privileges

# Class User

class User():
    # initial method
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    # defining class method
    def describe_user(self):
        print(self.first_name.title() +' ' +  self.last_name.title())
        print('Age: '+ str(self.age))
        print('Sex: ' + self.gender)

    def greet_user(self):
        print('Your are welcome here!')
        print('.'*30)


# class Privileges

class Privileges():

    def __init__(self):
        self.privileges = ['can add users','can remove users','can be a user']

    def show_privileges(self):
        print('Priviliges are: ',self.privileges)

# child Admin class inherited from Parent class User

class Admin(User):
    
    def __init__(self):
        self.privileges = ['can add post','can delete post','can be user']

        self.privileges = Privileges()

