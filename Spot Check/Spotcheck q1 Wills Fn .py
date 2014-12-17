# Password checker
def password_checker():
    validPassword = False
    while validPassword != True:
        passwordlength = get_password()
        validPassword = password_ok(passwordlength,validPassword)
    display_answer()

# get Password
def get_password():
    password = input("Please enter a valid Password between 8 to 16 characters: ")
    passwordlength = len(password)
    return passwordlength

# Is Password ok
def password_ok(passwordlength,validPassword):
    if 8 <= passwordlength <= 16:
        validPassword = password_accepted(validPassword)
    else:
        password_length(passwordlength)
    return validPassword

# Display
def display_answer():
    print("Password accepted")

# Password accepted
def password_accepted(validPassword):
    validPassword = True
    return validPassword
    
# Password long or short
def password_length(passwordlength):
    if passwordlength < 8:
        password_short()
    else:
        password_long()

# Password to long
def password_long():
    print("Password too long")

# Password to short
def password_short():
    print("Password too short")

# Main Program
password_checker()
