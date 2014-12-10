print("This program will calculate your weekly earnings ")
print("")

#Calculate pay
def calculate_pay():
    hours, rate = Getting_the_things()
    total = calculate_total_pay(hours, rate)
    return total

#Number of hours worked in a week and hourly rate

def Getting_the_things():
     hours = int(input("Hours Worked: "))
     rate = int(input("Hourly Rate: £"))
     print()
     return hours, rate


#Calculate basic pay

def calculate_basic_pay(hours,rate):
     total = hours * rate
     return total


#Calculate total pay

def calculate_total_pay(hours,rate):
      if hours <= 40:
           total = calculate_basic_pay(hours,rate)
      else:
            total = calculate_overtime_pay(hours,rate)
      return total


#Overtime pay for anything over 40 hours 

def calculate_overtime_pay(hours,rate):
     basic_pay = 40 * rate
     total = rate * hours * 1.5
     return total

#Main Program
    
def main():
    total = calculate_pay()
    print("You Should Be Making:")
    print("£",total,"Per Week")
