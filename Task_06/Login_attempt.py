# The program prints number of login attempts
# and resets the value of login attemps

class User():
    # initial method
    def __init__(self, first_name, last_name, age, sex, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = login_attempts 

    # defining class method
    def describe_user(self):
        print(self.first_name.title() +' ' +  self.last_name.title())
        print('Age: '+ str(self.age))
        print('Sex: ' + self.sex.title())

    def greet_user(self):
        print('Your are welcome here!')
        print('.'*30)

    def increment_login_attempt(self):
        # increments logins attempts
        
        self.login_attempts = self.login_attempts + 1
        print('Number of login attempts: ',self.login_attempts)
       

    def reset_login_attempt(self):
        # reseting value to zero
        self.login_attempts = 0
        print(f"NUmber of login attempts are: {self.login_attempts}")

# class instance
user = User("ali","khan",33,"male",0)
user.increment_login_attempt()
user.increment_login_attempt()
user.increment_login_attempt()
user.reset_login_attempt()