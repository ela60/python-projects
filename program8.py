from collections import deque
bank = deque(["ela","ambia","khatun"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()
if not bank :
    print("No person left")
def add(x,y):
    sum=x+y
    print(sum)
add(10,40)
add(20,50)

def sub(x,y):
    sub=x-y
    print(sub)
sub(30,20)

def large(a,b):
    if a>b:
        return a
    else:
        return b
result=large(20,30)
print("Result= ",result)


a=(lambda x :x*x*x)(2)
print(a)

roll=101,102,103,104,105,106,107,108,109,110
name=["ela","Ambia","shila","nela","khatun","ammu","abbu","tutum","tuntuni","tompy"]
print(list(zip(roll,name)))

