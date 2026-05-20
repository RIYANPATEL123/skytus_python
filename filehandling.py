import csv
#1
file = open("xyz.txt",'r')
content = file.read()
print(content)
file.close()

#2
file = open("xyz.txt",'r')
lines = file.readlines()
c = len(lines)
print("Total lines:",c)


#3
count ={}
for line in file:
    for word in line:
        word = word.lower()
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

for i in count:
    print("The word count:",count)
file.close()

#4
file = open("xyz.txt",'w')
for i in range(5):
    a = input("Enter the sentence which is to be added to file: ")
    file.write(a)
file.close()

#5
file = open("xyz.txt",'a')
l = ["this","hello","world"]
for i in l:
    file.write(i)
file.close()

#6
file = open("xyz.txt",'r')
a = "this"
lines = file.readlines()
for i in lines:
    if a in i:
        print(i)
    else:
        print("The word in not in that line")

file.close()

#7
file = open("xyz.txt",'r')
f = file.read()
file.close()
rep = f.replace("this","hello")
file = open("xyz.text",'w')
file.write(rep)
file.close

#8
file = open("xyz.txt",'r')
f1 = file.read()
file.close()

file = open("hello.txt",'r')
f2 = file.read()
file.close()
f3 = f1+f2
file = open("mer.txt",'w')
file.write(f3)
file.close()

#9
with open('your_file.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print("\t".join(row))


#10
file = open("xyz.txt",'r')
f = file.read()
file.close()

file = open("hello.txt",'w')
file.write(f)
file.close()

#OUTPUT
"""
I drink coffee every morning.
She likes to read books in the evening.
The train leaves at exactly 8:00 AM.
We played football in the park yesterday.
Total lines: 4
Enter the sentence which is to be added to fileThere are many days 
Enter the sentence which is to be added to filethere are 5 dyas
Enter the sentence which is to be added to filethere is not a single thing
Enter the sentence which is to be added to fileeveryt hitng is necesaaary
Enter the sentence which is to be added to filemany thigns canont happen once
There are many days there are 5 dyasthere is not a single thingeveryt hitng is necesaaarymany thigns canont happen oncethishelloworld
"""
