# Creates empty set:
s = set()

# Add elements to set - does not add repeated values
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

print(s)

s.remove(2)

print(s)

# len returns number of elements in sets, lists...
print(len(s))
