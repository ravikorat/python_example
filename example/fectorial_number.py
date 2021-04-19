# num=int(input("Enter the number :"))

# factorial=1

# if num==0:
#     print("The fectorial 0 is 1")
# elif num<0:
#     print("Fectorial does not exist for negative numbers")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("The fectorial of",num,"is:",factorial)


#2
num=int(input("Enter the number :"))
def fact(num):
    if num==1:
        return num
    else:
        return num* fact(num-1)

print(fact(num))