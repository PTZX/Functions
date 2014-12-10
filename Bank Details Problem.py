#Bank Details Problem

###A program to collect information from
#its customers when they register on its website.

###When firsts registering, the program should collect the users:
#first name, last name, title (Mr, Mrs, Ms etc).0
#house number/name and street name, town and post code.

def customerDetails():
    userTitle, firstName, lastName = gettingCustomerName()


#The getting of users identity
def gettingCustomerName():
    firstName = input("Enter your First Name: ")
    firstName = title(firstName)
    lastName = input("Enter your Surname: ")
    lastName = title(lastName)
    userTitle = input("Your Title: ")
    userTitle = capitalise(title)
    return firstName, lastName, userTitle


def customerAddress():
    houseno = input("Enter your house number: ")
    st = input("Enter your Street name: ")
    twn = input("Enter your Town: ")
    twn = capitalise(twn)
    pc = input(Enter)
    return hn, st, twn

def personalisedMsg(firstName, lastName):
    personalGreeting = ("Hello {0} {1}".format(userTitle, lastName))
    return personalGreeting

def main():
    
    msg = personalisedMsg(personalGreeting)
    print(msg)
    


