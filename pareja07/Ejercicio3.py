a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

print(a[0])
print(a[-1])

a.pop(0)

del a[-3:]

a.insert(0, 9)

a[a.index('ix')] = 4

a.append(5)

print(a[:3])

a.extend(a)

print('dos' in a)
print(3.0 in a)

print(a.count(1))
print(a.count(4))

for elemento in a:
    print(elemento)

for elemento in reversed(a):
    print(elemento)
