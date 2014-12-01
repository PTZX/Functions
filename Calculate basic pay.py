print("This program will calculate your wages, salary, untaxed income, occupational payout, earnings:")

#Calculate pay
def calculate_pay(hours,rate):
      hours = Getting_the_things(hours)
      rate = Getting_the_things(rate)


#Get rate and hours
def Getting_the_things(hours,rate):
      hours = int(input("Your Hours: "))
      rate = int(input("Hourly Rate: "))
      return hours, rate


#Calculate total pay

def calculate_total_pay(hours,rate):
      if hours <= 40:
           total = calculate_basic_pay(hours,rate)
      else:
            total = calculate_overtime_pay(hours,rate)
      return total


#Calculate basic pay

def calculate_basic_pay(hours,rate):
      total = hours * rate
      return total


#Overtime pay

def calculate_overtime_pay(hours,rate):
      overtime_hours = hours - 40
      basic_pay = 40 * rate
      total = rate * overtime_hours * 1.5
      return total, hours, rate

      
total  = hours * rate
#main program - display total pay
def display_total_pay(total):
      print("£{0}".format(total))
