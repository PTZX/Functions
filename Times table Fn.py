##

print("Times-table tester")
print()

#

def times_table():
    timesTable = input("Which times-table do you want to be tested on? ")
    timesTable = int(timesTable)
    return timesTable

def questions(timesTable):
    import random
    
    for q in range(1,16):
        num1 = timesTable
        num2 = random.randrange(2,13)
        answer = num1 * num2
        userAnswer = input(str(num1) + 'x' + str(num2) + " = ? ")
    return answer, userAnswer

def verdict(userAnswer, answer):
    if UserAnswer == answer:
        print('Well done, you got the correct answer!')
        print()
    else:
        print('Sorry, you got the answer wrong. The correct answer is',Ans)
        print()
    
