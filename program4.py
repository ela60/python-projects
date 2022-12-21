index=0
num=list(range(10))
print(num)
while index<5 :
    print(num[index])
    index=index+1
print("""""")
num=[10,20,30,21]
for x in num :
    print(x)

#1+2+....+n
n= int (input("Enter the last number"))
sum=0
for x in range(1,n+1,1) :
    sum=sum+x
    sum=sum*x
    print(x)
    print(x)


#n=5
#for i in range(n+1):
    # print(i*"*")


