numberOfWords= 0
numberOfDigits=0
numberOfLetters=0
text=input("Enter a text number :")
for x in text :
    x=x.lower()
    if x>='a' and x<='z' :
        numberOfLetters = numberOfLetters + 1
    elif x>='0' and x<='9' :
        numberOfDigits =numberOfDigits+1
    elif x==" " :
        numberOfWords =numberOfWords+1
print("number of letters",numberOfLetters)
print("number of digit ",numberOfDigits)
print("number of numberOfWords",numberOfWords+1)

