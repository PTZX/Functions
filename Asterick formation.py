a1 = "*"

n = int(input("Enter an odd number  "))
repeat = int(input("Enter the Number or Repetitions  "))

for each in range(repeat):
    each = each+1
    print(each)
    if n % 2 != 0:
        
        print("{0:^15}".format(a1))
        a = a1 * 2
        print("{0:^20}".format(a))
        a = a1 * 3
        print("{0:^20}".format(a))
        a = a1 * 5
        print("{0:^20}".format(a))
        a = a1 * 3
        print("{0:^20}".format(a))
        a = a1 * 2
        print("{0:^20}".format(a))
        a = a1
        print("{0:^15}".format(a1))
    
