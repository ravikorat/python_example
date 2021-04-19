import sys

randomList = ['a',0, 2]

# for i in randomList:
#     try:
#         print("The entry is", i)
#         r = 1/int(i)
#         print("The reciprocal of",i, "is", r)
#         break
#     except:
#         print("Oops!", sys.exc_info(), "occurred.")
#         print("Next entry.")
#         print()


try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)