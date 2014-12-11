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
    print(firstName, lastName, userTitle)
    return firstName, lastName, userTitle


def gettingCustomerAddress():
    houseno = input("Enter your house number: ")
    st = input("Enter your Street name: ")
    st = msg.title(st)
    twn = input("Enter your Town: ")
    twn = msg.capitalise(twn)
    pc = input("Enter your Post Code:")
    pc = msg.upper(pc)
    return houseno, st, twn, pc

def personalisedMsg(userTitle, lastName):
    personalGreeting = print("Hello {0} {1}".format(userTitle, lastName))
    return personalGreeting

#main program
def main():
    msg = personalisedMsg(personalGreeting)
    print("Your site greeting will be:")
    print(msg)
     


