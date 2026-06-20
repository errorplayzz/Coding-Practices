d = {} #empty dictionary

s = {1, 5, 32}

e = set() #dont use s = {} as it will create an empty dictionary

ss = {1, 2, 2, 4, 5, 3, 2, 2, 2, 4, 6, 7, 10} #set does not allow duplicate values

print(ss)

# methods of set

sets = {1, 3, 5, 3, 45, 32, 87, "Error"}

print(sets, type(s))

sets.add(566)
print(sets)

sets.remove(3)
print(sets)

# union of sets 

s1 = {1, 2, 3, 4, 5}    
s2 = {3, 4, 5, 6, 7}

print(s1.union(s2))

#intersection of sets

s1 = {1, 2, 3, 4, 5}    
s2 = {3, 4, 5, 6, 7}

print(s1.intersection(s2))

# minus of sets

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

print(s1-s2)
print(s2-s1)

