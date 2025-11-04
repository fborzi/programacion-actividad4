def getCity(people, dni):
    """
    It´s a function that returns a person´s city name if dni matches
    with the person´s dni. If not, it returns "City not found" prhase.
    Eparams - people: list - people list, dni: int - person´s dni
    @return - str
    """
    for person in people:
        if dni in person:
            return person[2]
        
    return "City not found."

def getState(people, cities, dni):
    """
    It´s a function that returns a person´s state name if dni matches
    with the person´s dni. If not, it returns "State not found" prhase.
    Eparams - people: list - people list, cities: list - cities list, dni: int - person´s dni
    @return - str
    """
    city = getCity(people, dni)

    for personState in cities:
        if city in personState:
            return personState[1]
        
    return "State not found."

def getPeopleInStateAmmount(people, cities, state):
    """
    It´s a function that returns the people ammount that live in a State.   
    Eparams - people: list - people list, cities: list - cities list, state: str - state to check
    @return - int
    """

    peopleAmmount = 0
    personState = ""
    personDni = 0

    for person in people:
        personDni = person[1]
        personState = getState(people, cities, personDni)

        if personState == state:
            peopleAmmount += 1

    return peopleAmmount

def reapeatedDigits(n):
    """
    It´s a funtion that returns a list that contains reapeted digits in 'n' parameter
    Eparamas - n: int - number to check
    @return - list
    """

    repeatedDigits = []
    nString = str(n)

    for digit in nString:
        if nString.count(digit) > 1 and not digit in repeatedDigits:
            repeatedDigits.append(int(digit))

    return repeatedDigits

def repeatedLetters(word):
    """
    It´s a function that returns a set that contains the repeated leeter in the "word" argument
    Eparams - word: str - string to check
    return - set 
    """
    word = word.lower()
    letters = [c for c in word if c.isalpha()]
    repeated = set([c for c in letters if letters.count(c) > 1])
    return repeated

def removeAccents(text):
    """
    It´sa function that replaces accented vowels with their non-accented equivalents.
    Eparams - text: str - text to check
    return - str
    """
    accents = {
        'á': 'a', 'à': 'a', 'ä': 'a', 'â': 'a',
        'é': 'e', 'è': 'e', 'ë': 'e', 'ê': 'e',
        'í': 'i', 'ì': 'i', 'ï': 'i', 'î': 'i',
        'ó': 'o', 'ò': 'o', 'ö': 'o', 'ô': 'o',
        'ú': 'u', 'ù': 'u', 'ü': 'u', 'û': 'u'
    }
    for accented, normal in accents.items():
        text = text.replace(accented, normal)
    return text

def hasThreeDifferentVowels(word):
    """
    It´s a function that checks if a word has at least 3 different vowels.
    Eparamas - word: str
    return - bool
    """
    word = word.lower()
    word = removeAccents(word)
    vowels = ['a', 'e', 'i', 'o', 'u']
    found = []
    for letter in word:
        if letter in vowels and letter not in found:
            found.append(letter)
    return len(found) >= 3

def characterFrequency(text):
    """
    It´s a functio that returns the ammount of times that a character appears in the text.
    Eparams - text: str - text to chek
    return - dicc
    """
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def versionA():
    """
    It´s a functios that only keeps a count of how many cities were entered and how many belong to each country.
    Eparams - 
    return - 
    """
    cityCount = 0
    countryCount = {}

    while True:
        city = input("Enter a city (or 'zz' to stop): ")
        if city.lower() == "zz":
            break

        country = input("Enter the country this city belongs to: ")
        cityCount += 1

        if country in countryCount:
            countryCount[country] += 1
        else:
            countryCount[country] = 1

    print("\n--- Results ---")
    print("Total number of cities entered:", cityCount)
    print("Number of cities per country:")
    for country, count in countryCount.items():
        print(f"{country}: {count}")


def versionB():
    """
    It´s a functios that stores each [city, country] pair in a list, and then process that list to count the cities per country.
    Eparams -
    return - 
    """
    cities = []

    while True:
        city = input("Enter a city (or 'zz' to stop): ")
        if city.lower() == "zz":
            break

        country = input("Enter the country this city belongs to: ")
        cities.append([city, country])

    # Process list to count how many cities per country
    countryCount = {}
    for city, country in cities:
        if country in countryCount:
            countryCount[country] += 1
        else:
            countryCount[country] = 1

    print("\n--- Results ---")
    print("Total number of cities entered:", len(cities))
    print("Number of cities per country:")
    for country, count in countryCount.items():
        print(f"{country}: {count}")