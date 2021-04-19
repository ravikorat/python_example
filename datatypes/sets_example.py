my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

print(type(my_set))

my_set.add(10)
print(my_set)

my_set.update([12, 13, 4])
print(my_set)

my_set.discard(6)
print(my_set)


# my_set.remove(6)#raise an error
# print(my_set)




my_sets = set("HelloWorld")
print(my_sets)

my_sets.pop()
print(my_sets)
my_sets.clear()
print(my_sets)


#set operation
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# Union
print(A|B)
print(A.union(B))
print(B.union(A))

# Intersection
print(A &B)
print(A.intersection(B))
print(B.intersection(A))

# Difference
print(A - B)
print(A.difference(B))
print(B.difference(A))

# Symmetric Difference element is A and B but not both
print(A ^ B)
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))




for letter in set("apple"):
    print(letter)