l1=[10,100,66,15]
l2=['m','n','a','a']
l1.sort()
print(l1)
l2.sort()
print(l2)

l1.reverse()
print(l1)

print(sorted(l1))
print(sorted(l1,reverse=True))

print(max(l1))
print(min(l2))

print(sum(l1))

print(l2.count("a"))

l1.extend(l2)
print(l1)

l1.append("c++")
print(l1)

l1.remove("a")
print(l1)

l1.pop(1)
print(l1)

pl=l1.index("c++")
print(pl)