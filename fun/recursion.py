def tri_recursion(n):
    if n>0:
        res = n+ tri_recursion(n-1)
        print(res)
    else:
        res= 0
    return res

print("Tri recursion is")
num=6
tri_recursion(num)