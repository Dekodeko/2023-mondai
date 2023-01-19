from dataclasses import dataclass

@dataclass
class User:
    name:str
    age:int

class tab_ctrl:
    coltbl: int[2]

def tc(user):
    print("tc user ",user )
    print("tc age = ", user.age)
    print("tc name = ",user.name)

user = User('tadokoro',24)

print( "user ",user )
print("age = ", user.age)
print("name = ",user.name)

tc(user)

