patients = {
    14972142: [45, "F", True],
    6409217: [70, "M", False],
    25600123: [55, "M", True],
    38765432: [82, "F", False],
    45987654: [60, "M", True]
}

print("a) Total registered patients:", len(patients))

print("\nb) Patient list:")
for dni, data in patients.items():
        age, sex, diabetic = data
        print(f"DNI: {dni} | Age: {age} | Sex: {sex} | Diabetic: {'Yes' if diabetic else 'No'}")

try:
    dni_input = int(input("\nc) Enter a DNI to increase their age by 1: "))
    if dni_input in patients:
        patients[dni_input][0] += 1
        print(f"Updated age for patient {dni_input}: {patients[dni_input][0]} years")
    else:
        print("DNI not found.")
except ValueError:
    print("Invalid input. Please enter a numeric DNI.")

    # d) Check if DNIs 14.972.142 and 6.409.217 have diabetes
print("\nd) Diabetes check:")
for dni in [14972142, 6409217]:
    if dni in patients:
        print(f"Patient {dni} has diabetes: {'Yes' if patients[dni][2] else 'No'}")
    else:
        print(f"Patient {dni} not found.")

diabetic_ages = [data[0] for data in patients.values() if data[2]]
if len(diabetic_ages) > 0:
    avg_age = sum(diabetic_ages) / len(diabetic_ages)
    print(f"\ne) Average age of diabetic patients: {avg_age:.2f}")
else:
    print("\ne) No diabetic patients registered.")

has_old_non_diabetic = any(data[0] > 80 and not data[2] for data in patients.values())
print("\nf) Is there any patient older than 80 without diabetes?",
        "Yes" if has_old_non_diabetic else "No")