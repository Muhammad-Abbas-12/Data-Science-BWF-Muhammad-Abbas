# this file show that how we use a module to call a method 

from Admin_user_privileges_module import Admin, User, Privileges

# privileges instance 

admin = Admin()
admin.privileges.show_privileges()
