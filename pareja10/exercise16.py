numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
numberName = ""
numbers.update({"eleven":11, "twelve": 12})
for number in range(30, 36):
    numberName = "number", number
    numbers.update(dict(numberName = number))
numbers.update({"two hundred thirty-six": 232, "two hundred and sixty-three negative": -263})

for key, value in numbers.items():
    print("Firs number saved: ", key, ":", value)
    break

for key, value in numbers.items():
    if value < 0: 
        print("Last number saved: ", key, ":", value)
        break

if 7 in numbers: print("Number 7 is in the diccionary.")
if 20 in numbers: print("Number 20 is in the diccionary.")

print("Numbers ammount saved: ", len(numbers))