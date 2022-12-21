matrix = [
        [1,2,3],
        [2,3,4],
]
for row in matrix :
    for col in row :
        print(col)

#dictionary
studentid ={
    "101" : "ela",
    "102" : "Ambia",
    "103" : "khatun",
}
print(studentid["103"])

#Tuples vaeiable not change
tuple
students =(
    ("Ambia",107,109,103),
    "Ela",
    "Khatun",
)
print(students[0 :])#(:sob print)

#set
set
num1 ={1,2,3,4}
num2 =set([4,5,6])
num2.add(7)
num2.remove(4)
print(4 not in num2)
print(num1 | num2)#union(|)
print(num1 & num2)#intersect &
print(num1 - num2)#difference -

#push &pop
books = []
books.append("learn c")
books.append("learn c++")
books.append("learn data structure")
print(books)
books.pop()
print(books)