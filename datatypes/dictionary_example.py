my_dict = {'name': 'Jack', 'age': 26}
print(my_dict['name'])
print(my_dict.get('age'))
print(my_dict.get('address'))#return none key is not found
# print(my_dict['address'])#key error

my_dict['age'] = 27
print(my_dict)

my_dict['address'] = 'Downtown'
print(my_dict)


squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))#16
print(squares)
print(squares.popitem())#(5,25)
print(squares)
# squares.clear()
# del squares
# print(squares)


marks = {}.fromkeys(['Ravi', 'Ashish', 'Megha'], 0)
print(marks)
print(list(sorted(marks.keys())))


dic = {x: x*x for x in range(6)}
print(dic)