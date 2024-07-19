# inheritance of user class 

# user class

class User():
    # initial method
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    # defining class method
    def describe_user(self):
        print(self.first_name.title() +' ' +  self.last_name.title())
        print('Age: '+ str(self.age))
        print('Sex: ' + self.sex)

    def greet_user(self):
        print('Your are welcome here!')
        print('.'*30)

# child class inherited from Parent class User

class Admin(User):
    
    def __init__(self):
     self.privileges = ['can add post','can delete post','can be user']

    def show_privileges(self):
        print('Priviliges are: ',self.privileges)

# child class instance
admin = Admin()
admin.show_privileges()
