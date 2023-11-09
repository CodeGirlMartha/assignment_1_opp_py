#create a user class with properties like name , age, location.
#create a new instance of the user class(a new object).
#access the user name and age
#create  a function for the user class then print a users location
#print the users location using this function

# A user class with properties ie name, age, location
class user:
    name = "MARTHA"
    age = 21
    location = 'KISAASI'
# the new insatnce(object)
user_info =user() 
print(user_info.name)
print(user_info.age)

# create a function for the user class that prints a user's location
# using the _init_ function to print the user's location

class user:
    def __init__(user001, location):
        user001.location = location 
user_info = user("KISAASI")
print(user_info.location)