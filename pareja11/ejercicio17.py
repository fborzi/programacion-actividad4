horm1 = set(["melanina", "oxitocina", "dopamina"])
horm2 = set(["testosterona", "melanina"])
horm3 = set(["calcitocina", "oxitocina"])

# a)
print("horm1 y horm2 comparten:", horm1 & horm2)
print("horm1 y horm3 comparten:", horm1 & horm3)

# b)
print("horm2 es subconjunto de horm1?", horm2.issubset(horm1))

# c)
todas = horm1 | horm2 | horm3
print("todas las hormonas:", todas)