# this file show that how we use a module to call a method 

from Imported_Admin import Admin, User, Privileges

# privileges instance 

admin = Admin()
admin.privileges.show_privileges()
