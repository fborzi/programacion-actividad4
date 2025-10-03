horm1 = set(['melanina', 'oxitocina', 'dopamina']) 
horm2 = set(['testosterona', 'melanina']) 
horm3 = set(['calcinotna', 'estradiol'])
hormSharing = False
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
if horm2 in horm1:
    print("horm2 is a subset of homr1.")
else:
    print("horm2 isn´t a subset of homr1.")

# C
for horm in horm1:
    print("horm1: ", horm)

print("")

for horm in horm2:
    print("horm2: ", horm)

print("")

for horm in horm3:
    print("horm3: ", horm)