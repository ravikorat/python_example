print("select operation :")
print("1.Add")
print("2.Subtract")
print("3.Multiplication")
print("4.Division")

def add(a,b):
    return a + b
    
def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

while True:
    choice= int(input("Enter choice(1,2,3,4):"))
    if choice in (1,2,3,4):
        n1 = float(input("Enter the first number:"))
        n2 = float(input("Enter the second number:"))

        if choice == 1:
            print(n1, '+', n2, '=' , add(n1,n2))
        elif choice == 2:
            print(n1, '-', n2, '=' , subtract(n1,n2))
        elif choice == 3:
            print(n1, '*', n2, '=' , multiply(n1,n2))
        elif choice == 4:
            print(n1, '/', n2, '=' , divide(n1,n2))
        break
    else:
        print("Invalid input")


            
