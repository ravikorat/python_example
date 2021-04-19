my_string="Hello "
str2 = "Ravi"
print(my_string)


print(my_string[0])
print(my_string[-1])
print("5th character is : ",my_string[5])
print(my_string[2:7])

# my_string[4]='a'
# print(my_string)

print(my_string+str2)
print(str2*3)


count = 0
for letter in 'Hello World':
    if(letter == 'o'):
        count += 1
print(count,'letters found')


keyword_order = "{s}, {b} and {j} you are brilliant".format(j='rk',b='Korat',s='Ravi')
print(keyword_order)



print("Binary representation of {0} is {0:b}".format(12))

# formatting floats
print("Exponent representation: {0:e}".format(254.36985))


 # round off
print("One third is: {0:.4f} {1:.3f}".format(1/3,1/5))


 # string alignment
print("|{:<10}|{:^10}|{:>10}|".format('ravi','korat','rk'))
