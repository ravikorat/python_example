x = "global "

def myFun():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

myFun()

#2
x = 5
def myFunction():
    x = 10
    print("local x:", x)
myFunction()
print("global x:", x)

#3
c = 0
def add():
    global c
    c = c + 2 
    print("Inside add():", c)

add()
print("In main:", c)