numbers = [10, 23, 45, 66, 78, 91]
names = ["michael", "sara", "tom", "lucas", "emma"]

for number in numbers:
    if number % 2 == 0:
        print(f"Even: {number}")\

else:
    print(f"Odd: {number}")

for name in names:
    if name == "sara":
        print("sara is present")
        break

else:
    print("sara non")