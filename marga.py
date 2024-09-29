# Given arrays
#print negative, print positive
age = [12, 13, -14, 15, -16]
username = ["Marga", "Miko", "Margarette", "Cutie", "Margaux"]


for num in age:
    if num < 0:
        print(f"Negative 0 : {num}")
    elif num > 1:
        print(f"Positive 1: {num}")


for name in username:
    if name == "Marga":
        print("Marga is cute")
        break
else:
    print("Marga is none")
