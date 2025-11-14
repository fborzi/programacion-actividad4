members = {}

print("Enter member information (enter DNI '0' to finish):")

while True:
    dni = input("\nEnter DNI: ")
    if dni == "0":
        break

    name = input("Enter name: ")
    lastName = input("Enter last name: ")
    age = int(input("Enter age: "))
    feeStatus = input("Is the membership fee up to date? (yes/no): ").lower() == "yes"

    members[dni] = {
        "name": name,
        "lastName": lastName,
        "age": age,
        "feeUpToDate": feeStatus
    }

    # a) Number of members
print("\na) Total number of members:", len(members))

    # b) Number of members with unpaid fees
unpaidMembers = [m for m in members.values() if not m["feeUpToDate"]]
print("b) Number of members with unpaid fees:", len(unpaidMembers))

    # c) Show name and last name of member with DNI 25.123.555
targetDni = "25123555"
print("\nc) Searching for member with DNI 25.123.555:")
if targetDni in members:
    member = members[targetDni]
    print(f"Member found: {member['name']} {member['lastName']}")
else:
    print("No member found with that DNI.")

    # d) Add a new member
members["40151724"] = {
    "name": "Esteban",
    "lastName": "Quito",
    "age": 17,
    "feeUpToDate": True
}
print("\nd) New member added: Esteban Quito (DNI 40.151.724)")

    # e) Member with the highest age
if members:
    oldestDni = max(members, key=lambda d: members[d]["age"])
    print(f"\ne) The oldest member's DNI is: {oldestDni}")
else:
    print("\ne) No members registered.")

    # f) Remove member with DNI 15.188.125 only if they exist and fee is up to date
removeDni = "15188125"
print("\nf) Removing member with DNI 15.188.125...")
if removeDni in members:
    if members[removeDni]["feeUpToDate"]:
        del members[removeDni]
        print("Member successfully removed.")
    else:
        print("Cannot remove member: fee is not up to date.")
else:
       print("No member found with that DNI.")

    # g) Register that member with DNI 28.731.431 paid their fee
updateDni = "28731431"
print("\ng) Updating payment for member with DNI 28.731.431...")
if updateDni in members:
    members[updateDni]["feeUpToDate"] = True
    print("Payment updated successfully.")
else:
    print("No member found with that DNI.")

    # Optional: show final list of members
print("\n--- Final member list ---")
for dni, data in members.items():
    print("DNI:", dni, "|", data["name"], data["lastName"], "| Age:", data["age"], "| Fee up to date:", "Yes" if data["feeUpToDate"] else "No")