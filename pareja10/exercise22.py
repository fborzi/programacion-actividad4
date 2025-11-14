cities = {
    "Junin": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

print("a) Population of Pergamino:", cities["Pergamino"])

cities["Lincoln"] = 42036
print("b) Added Lincoln:", cities)

del cities["Junin"]
print("c) After removing Junin:", cities)

cities["Rojas"] += 1000
print("d) After increasing Rojas population by 1,000:", cities)

cities["Pergamino"] = 91399
print("e) After updating Pergamino population:", cities)