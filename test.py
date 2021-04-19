# def tri_recursion(n):
#     if n>0:
#         res = n+ tri_recursion(n-1)
#         print(res)
#     else:
#         res= 0
#     return res

# print("Tri recursion is")
# num=6
# tri_recursion(num)

# double= lambda a,b:a+b
# print(double(5,10))

# my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# print(new_list)

# my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# new_list = list(map(lambda x: (x*2 ) , my_list))

# print(new_list)

# x = 20

# def foo():
#     x=x * 2
#     print(x)
   

# foo()

# def outer():
#     x = "local"

#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)

#     inner()
#     print("outer:", x)


# outer()
# c = 5 # global variable

# def add():
#     global c
#     c = c + 2 # increment by 2
#     print("Inside add():", c)

# add()
# print("In main:", c)

# import math
# x=2.55
# print(math.ceil(x))
# nested list
# my_list = ["mouse", [8, 4, 6], ['a']]
# print(my_list[2][0])
# Appending and Extending lists in Python
# odd = [1, 3, 5]

# odd.insert(3,3)

# print(odd)

# odd.extend([9, 11, 13])

# print(odd)

# Dictionary Methods
# marks = {}.fromkeys(['Math', 'English', 'Science'], 0)

# # Output: {'English': 0, 'Math': 0, 'Science': 0}
# print(marks)

# for item in marks.items():
#     print(item)

# # Output: ['English', 'Math', 'Science']
# print(list(sorted(marks.keys())))

# # Dictionary Comprehension
# squares = {x: x+x for x in range(6)}

# print(squares)

# f=open("test.txt",'w')
# f.write("hello world\n")
# f.write("Hii how are you\n")
# f.write("My name is ravi")
# f.close()

# f=open("test.txt",'a')
# f.write("hgfhghdzf")

# f=open("test.txt",'r')
# f.tell() 
# print(f.readable())
# f.close()

# f=open("myfile.txt",'w')
# f.write("hfdhfhd\n")
# f.write("hfueiei")
# f.close()

# f=open("myfile.txt",'r',encoding='utf-8')
# print(f.read())

# f=open("test.txt",'w')
# f.write("hhjhfhd")
# import module sys to get the type of exception
import sys

randomList = [4, 4, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)