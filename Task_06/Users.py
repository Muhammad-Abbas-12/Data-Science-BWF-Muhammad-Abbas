# Making a class user that descrive usrs information

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


# class instance
user_1 = User('Ali','Khan','23','Male')
user_1.describe_user()
user_1.greet_user()

# class instance
user_2 = User('Sajid','Ahmad','45','Male')
user_2.describe_user()
user_2.greet_user()

# class instance 
user_3 = User("Shabana",'Gul','51','Female')
user_3.describe_user()
user_3.greet_user()