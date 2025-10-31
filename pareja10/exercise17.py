horm1 = set(['melanina', 'oxitocina', 'dopamina']) 
horm2 = set(['testosterona', 'melanina']) 
horm3 = set(['calcinotna', 'estradiol'])
hormSharing = False
horm1SubSetOfHorm2 = True
# A
for horm in horm1:
    if horm in horm2:
        hormSharing = True
        print("Homr1 share the ", horm ," hormon with horm2.")
        break

if not hormSharing:
    print("horm1 and horm2 don´t share any hormon  with horm2.")

hormSharing = False

for horm in horm1:
    if horm in horm3:
        hormSharing = True
        print("homr1  and horm3 share the ", horm, " hormon with horm3.")

if not hormSharing:
    print("horm1 and horm3 don´t share any hormon with horm3.")

# B
for horm in horm1:
    if horm not in horm2:
        hormSharing = False
        print("horm1 isn´t a subset of horm2.")
        break

if horm1SubSetOfHorm2:
    print("horm1 is a subset of horm2.")

#C
print("Horm1:")
for horm in horm1:
    print(horm)

print("Horm2:")
for horm in horm2:
    print(horm)

print("Horm3:")
for horm in horm3:
    print(horm)