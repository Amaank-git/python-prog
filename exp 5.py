L=[24,56,78,99]
print(L)
L.append(100)
print(L)
N=[1,2,3,4]
print(N)
N.extend(L)
print(N)
print(N.insert(2,4))

print(N.remove(4))

print(N.index(100))

print(N.count(2))
N.sort()
print(N)
N.clear()
print(N)


