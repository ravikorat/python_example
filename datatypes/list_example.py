myList=['p','r','o','g','r','a','m','i','z']

print(myList[0])
print(myList[-1])

print(myList[2:5])
print(myList[-5:-1])



odd = [2, 4, 6, 8]  
odd[0] = 1            
print(odd)

odd[1:4] = [3, 5, 7]  
print(odd)

odd.append(9)
print(odd)

odd.extend([10,11,89])          
print(odd)

odd.insert(1,100)
print(odd)

# del odd[2]
# print(odd)

# del odd
# print(odd)

odd.remove(1)#element
print(odd)

odd.pop(1)#position
print(odd)

odd.pop()
print(odd)

# odd.clear()
# print(odd)

odd.sort()
print(odd)


pow2 = [2 ** x for x in range(10)]
print(pow2)


for fruit in ['apple','banana','mango']:
    print("I like",fruit)