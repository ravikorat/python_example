num=int(input("Enter the number:"))
s = 0

temp = num
while temp > 0:
   d = temp % 10
   s += d ** 3
   temp //= 10

# display the result
if num == s:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")