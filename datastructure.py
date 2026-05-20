#1
t = (3,6,7,2,8)

#2
print("the third element is:",t[2])

#3
a,b,c,d,e = t
print("The 5 unpacked elements are ",a,b,c,d,e)

#4
s = {"banana","mango","kiwi","watermelon","apple"}

#5
s.add("orange")

#6
s.remove("mango")

#7
b={"kiwi","grape","muskmelon"}
print("the union of set:",s|b)

#8
print("the intersection of set:",s&b)

#9
print("check is b is subset of s",b.issubset(s))

#10
l= [14,18,19,20,12,14,19,18]
s = set(l)
print("after removing duplicate values:",s)


#11
d = {"riyan":50,"yug":42,"neil":39}

#12
d.update({"name":21})

#13
d.pop("riyan")

#14
h = {"hello":18,"maseiah":41}
d.update(h)

#15
print(h.get("hello"))

#16
text = "apple banana apple orange banana apple"
frequency = {}


for word in text.split():
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)


#17
print("Max key is:",max(d,key=d.get))

#18
reverse ={}
for k,b in d.items():
    reverse[b] = k
print("Reversed dict:",reverse)

#19
d["yug"]=90
print("The updated dictionary:",d)

#20
t = [('apple', 1), ('banana', 2), ('orange', 3)]
d = dict(t)
print("The conversion of list of tuple into dict:",d)

#OUTPUT
"""
the third element is: 7
The 5 unpacked elements are  3 6 7 2 8
the union of set: {'orange', 'muskmelon', 'watermelon', 'grape', 'kiwi', 'banana', 'apple'}
the intersection of set: {'kiwi'}
check is b is subset of s False
after removing duplicate values: {12, 14, 18, 19, 20}
18
{'apple': 3, 'banana': 2, 'orange': 1}
Max key is: yug
Reversed dict: {42: 'yug', 39: 'neil', 21: 'name', 18: 'hello', 41: 'maseiah'}
The updated dictionary: {'yug': 90, 'neil': 39, 'name': 21, 'hello': 18, 'maseiah': 41}
The conversion of list of tuple into dict: {'apple': 1, 'banana': 2, 'orange': 3}
"""