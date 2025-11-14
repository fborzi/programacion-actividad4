from functions import versionA
from functions import versionB

print("Choose a version to run:")
print("a) Without storing cities")
print("b) Storing cities in a list")
choice = input("Enter your choice (a/b): ").lower()

if choice == "a":
    versionA()
elif choice == "b":
    versionB()
else:
    print("Invalid choice.")