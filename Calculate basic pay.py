print("This program will calculate your weekly earnings ")
print("Salary, untaxed income, occupational payout or earnings")

#Calculate pay
def calculate_pay():
    hours, rate = Getting_the_things()
    total = calculate_total_pay(hours, rate)
    return total

#Input the number of hours worked in a week and hourly rate
      
def Getting_the_things():
     hours = int(input("Your Hours: "))
     rate = int(input("Hourly Rate: "))
     return hours, rate

#Calculate basic pay

def calculate_basic_pay(hours,rate):
     total = hours * rate
     return total

      
#Overtime pay for anything over 40 hours 

def calculate_overtime_pay(hours,rate):
     print(hours)
     print(rate)
     overtime_hours = hours - 40
     basic_pay = 40 * rate
     total = rate * overtime_hours * 1.5
     return total
    

#Calculate total pay

def calculate_total_pay(hours,rate):
      if hours <= 40:
           total = calculate_basic_pay(hours,rate)
      else:
            total = calculate_overtime_pay(hours,rate)
      return total


      
#display total pay
def calculate_pay(total):
    
