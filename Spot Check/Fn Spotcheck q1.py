##Password between 8-16 characters long
print("Enter a password of 8 to 16 characters")

##def passwordCheck():
##    validPassword = false

def getPassword():
    password = input("Enter a password: ")
    return password
                
def Length(password):
    valid = False
    length = len(password)
    if 8<= length <= 16:
        print("Password Accepted")
        valid = True
    elif len(password) < 8:
        print("Too Short")
    else:
        print("Too Long")
    return valid

def passwordcheck():
    valid = False
    while valid == False:
        password = getPassword()
        valid = Length(password)

passwordcheck()
