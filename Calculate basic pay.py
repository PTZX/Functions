<<<<<<< HEAD

#Get rate and hours
def Getting_the_things():
         hours = int(input("Your Hours: "))
         rate = int(input("Hourly Rate: "))


#Calculate total pay

def calculate_total_pay(hours,rate):
         if hours <= 40:
                 total = calculate_basic_pay(hours,rate)
         else:
                  total = calculate_overtime_pay(hours,rate)
         return total


#overtime pay

def calculate_overtime_pay(hours,rate):
         overtime_hours = hours - 40
         basic_pay = 40 * rate
         total = rate * overtime_hours * 1.5
         return total


#calculate basic pay

def calculate_basic_pay(hours,rate):
         total = hours * rate
         return total



#main program

total_pay = calculate_basic_pay(hours,rate)
print("£{0} a week".format(total_pay))
total_pay = calculate_overtime_pay(41,5)
print("£{0} a week".format(total_pay))
=======
#calculate_basic_pay

def calculate_basic_pay(hours,rate):
    total = hours * rate
    return total


#overtime_pay

def calculate_overtime_pay(hours,rate):
    overtime_hours = hours - 40
    overtime = overtime_rate * hours * 1.5
    total = overtime + total_pay
    return total

def calculate_total_pay(hours,rate):
    if hours <= 40:
        total = calculate
        return total



#main program
total_pay = calculate_basic_pay(12,2)
print(total_pay)

total_pay = calculate_ovetime_pay(41,1)
print(total_pay)
>>>>>>> branch 'master' of https://github.com/PTZX/Functions.git

