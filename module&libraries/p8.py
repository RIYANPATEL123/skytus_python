import random as r

l = [1,2,3,4,5,6]
print(f"Original list {l}")
for i in range(int(len(l)/2)):
    a = r.randint(0,len(l)-1)
    b = r.randint(0,len(l)-1)
    c = l[a]
    l[a] = l[b]
    l[b] = c 
print(f"Random Shuffled list {l}")
