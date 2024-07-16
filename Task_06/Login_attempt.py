# The program prints number of login attempts
# and resets the value of login attemps

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

    def login_attempt(self):
        