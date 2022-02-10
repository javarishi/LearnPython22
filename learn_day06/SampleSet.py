sampleSet = {"apple", "oranges", "blackberry", "strawberry"}

print(sampleSet)
sampleSet.add("mango")
print(sampleSet)
sampleSet2 = {"potatoes", "carrots", "radish", "blackberry"}
sampleSet.update(sampleSet2)
print(sampleSet)
sampleSet.discard("carrots")
print(sampleSet)
# discard - no errors
sampleSet.discard("onion")
print(sampleSet)