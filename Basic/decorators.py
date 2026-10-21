# global() --> to print all the global variables
# local() --> to print all the variables
s='GLOBAL VARIABLE !'
def func():
    mylocal=10
    print(locals())
    print(s)

print(func())
print(s)

print(locals())


def hello(name="jose"):
    return "Helo"+name

print(hello())

# assign a fuction to variable

a=hello

print(a())

print("=========1===========")

def hello(name="jose"):
    print("The hellow() function has been run!")

    def greet():
        return "This stging is inside greet()"

    def welcome():
        return "This string is inside welcome !"
    # print(greet())
    # print(welcome())
    # print("End of hello()")

    if name=="jose":
        return greet
    else:
        return welcome

x=hello()

print(x())

print("=======2=============")

def hello():
    return "Hi JOSE !"

def other(func):
    print("hello")
    print(func())

other(hello)


print("========3=============")

def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("func() has been called")
    return wrap_func

def func_needs_decorator():
    print("this function needs decorator!")

a=new_decorator(func_needs_decorator)
a()

print("========4=============")

@new_decorator
def func_needs_decorator():
    print("this function needs decorator!")

func_needs_decorator()