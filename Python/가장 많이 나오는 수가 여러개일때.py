from collections import Counter

a=[1, 2, 3, 4, 5, 6, 6, 7, 7,7,4, 4,3, 2, 1, 1]
b=['allice', 'bar', 'caca', 'dada', 'mm', 'caca', 'ddddd', 'dada']


k=Counter(a)

print(k)


for key, values in k.items():
    if values==max(k.values()):
        print(key)

#print(max(k.values()))


l=Counter(b)
print(l)

for key, values in l.items():
    if values==max(l.values()):
        print(key)
