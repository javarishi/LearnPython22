sampleDictionary = {
    "model" : "Camry",
    "company" : "Toyota",
    "Year" : 2020,
    "color" : "Shiny White",
}

print(sampleDictionary)
sampleDictionary["origin"] = "Japan"
print(sampleDictionary)
# getting an element
print(sampleDictionary.get("model"))
print(sampleDictionary["origin"])
sampleDictionary["color"] = "Shiney Red"
print(sampleDictionary)

if "model" in sampleDictionary:
    print("Exists")

if "Camry" in sampleDictionary.values():
    print("Value Exists")

for eachKey in sampleDictionary:
    print(eachKey, sampleDictionary.get(eachKey))

for eachKey, eachValue in sampleDictionary.items():
    print(eachKey, eachValue)

for eachValue in sampleDictionary.values():
    print(eachValue)

# pop(key)
sampleDictionary.pop("origin")
print(sampleDictionary)
sampleDictionary.popitem()
print(sampleDictionary)
