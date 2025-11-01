digitAddition = 0
repeatedDigitsAmmount = 0
numbersTypedAmmount = 0
digitsRepeated = set()
numbersHigherThan470Ammount = 0
percentageNumbersHigherThan470 = 0
procecedNumbersAverage = 0
allNumbersAddition = 0
hasRepeatedNumbers = False
numberToCheck = int(input("Enter a integer number: "))
stringNumber = str(numberToCheck)

numbersTypedAmmount += 1
allNumbersAddition += numberToCheck

if numberToCheck > 470:
    numbersHigherThan470Ammount +=1

for number in stringNumber:
    if stringNumber.count(number) > 1:
        hasRepeatedNumbers = True

while hasRepeatedNumbers:
    for number in stringNumber:
        if stringNumber.count(number) > 1 and number not in digitsRepeated:
            digitsRepeated.add(number)
            repeatedDigitsAmmount += 1
            digitAddition = int(number) * stringNumber.count(number)
            #A
            print("Digit ", number, "its addition is ", digitAddition)
    #B
    print(repeatedDigitsAmmount, " digits are repeated in ", numberToCheck)

    hasRepeatedNumbers = False
    repeatedDigitsAmmount = 0
    hasRepeatedNumbers = False

    numberToCheck = int(input("Enter a integer number: "))
    stringNumber = str(numberToCheck)

    numbersTypedAmmount += 1
    allNumbersAddition += numberToCheck

    if numberToCheck > 470:
        numbersHigherThan470Ammount +=1

    for number in stringNumber:
        if stringNumber.count(number) > 1:
            hasRepeatedNumbers = True


percentageNumbersHigherThan470 = (numbersTypedAmmount * numbersHigherThan470Ammount) / 100
procecedNumbersAverage = allNumbersAddition / numbersTypedAmmount

#C
print("Percentage Numbers Higher Than 470 (C): ", percentageNumbersHigherThan470)
#D
print("Proceced Numbers Average (D): ", procecedNumbersAverage)