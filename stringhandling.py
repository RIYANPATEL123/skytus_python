#1 
a =input("Give a string to print its length: ")
print("The length of the string is:",len(a))

#2
b = input("Enter your sentence to convert into lowercase")
print("The lowercase of the string is: ",b.lower())

#3
a = "Hello world"
a.replace(" ","_")


#4
print("The first character of a string",a[0])
print("The last character of a string",a[-1])

#5
for i in range(1,len(a)+1):
    print(a[-i],end="")

#6
b = "l"
c = 0
for i in a:
    if(b==i):
        c = c+1
print("The letter",b,"appears",c,"times in the string")

#7
b = "This is a sentence"
c = "sentence"
if c in b:
    print("The word is there in the sentence")
else:
    print("The word is not there in the sentence")

#8

a = input("Enter your name")
b = int(input("Enter your age"))
print(f"Your name is {a}")
print(f"Your age is {b}")

#9
a = "    Sentence    "
print("After removeing extra spaces",a.strip())

#10
l = ["hello","this","is","a"]
for i in l:
    print(i,end="-")

#11
l =["terminator","dark knight","Hello","Driver","pushpa"]

#12
l.append("spiderman")
print(l)

#13
l.pop(0)

#14
l = [15,13,2,72,35,4,5,6]
l.sort(reverse=False)

#15
l.reverse()

#16
a = 0
for i in range(len(l)):
    if l[i]>a:
        a = l[i]
    
print("The largest number in a list:",a)

#17
k = [91,13,42]
for i in range(len(k)):
    l.append(k[i])

#18
for i in k:
    a = i
print("The last element of a list is:",a)

#19
l = [13,15,1,3,[14,54,76]]
print("The specific inner element is:",l[4][1])

#20
c = 0
a = 91
k.append(a)
for i in k:
    if i==a:
        c+=1
print("the number of times an element appears in a list:",c)


#OUTPUT

"""
Give a string to print its length: HEllow
The length of the string is: 6
Enter your sentence to convert into lowercaseTHIs is a UppcAse Sentecne
The lowercase of the string is:  this is a uppcase sentecne
The first character of a string H
The last character of a string d
dlrow olleHThe letter l appears 3 times in the string
The word is there in the sentence
Enter your nameriyan
Enter your age19
Your name is riyan
Your age is 19
After removeing extra spaces Sentence
hello-this-is-a-['terminator', 'dark knight', 'Hello', 'Driver', 'pushpa', 'spiderman']
The largest number in a list: 72
The last element of a list is: 42
The specific inner element is: 54
the number of times an element appears in a list: 2
"""


