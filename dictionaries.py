# New dict:
houses = {
    "Harry": "Gr",
    "Draco": "Sl"
}
print(houses)

houses["Ginny"] = "Gr"

print(houses)

print(houses["Harry"])

if "Augusto" in houses.keys():
    print(houses["Augusto"])
else:
    print("Augusto not a key")
