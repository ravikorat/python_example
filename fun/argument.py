def greet(name, msg="Good morning!"):
    print("Hello", name + ', ' + msg)


greet("Ravi")
greet("Korat", "How do you do?")


def myFunction(*names):
    for name in names:
        print("Hello", name)


myFunction("ravi", "korat", "kishan")