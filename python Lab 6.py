print "How many numbers do you want to add together?"

total = 0

for x in range(3):
    userInput = int(raw_input())
    total = total + userInput
    
print total

totalList = []
for x in range(3):
    userInput = int(raw_input())
    totalList.append(userInput)

print sum(totalList)

print 'What number do you want the factorial of?'
userInput = raw_input()
total = 1
for i in range(1, int(userInput)+ 1,1):
    total = total * i
    
print int(total)

print 'What number do you want the factors of?'
userInput = raw_input()
for i in range(1, int(userInput)+ 1,1):
    if int(userInput) % i == 0:
        print i
