# class admin and privileges module

from User_class_module import User

class Admin(User):
    
    def __init__(self):
     self.privileges = ['can add post','can delete post','can be user']

    def show_privileges(self):
        print('Priviliges are: ',self.privileges)

class Privileges():

    def __init__(self):
        self.privileges = ['can add users','can remove users','can be a user']

    def show_privileges(self):
        print('Priviliges are: ',self.privileges)
