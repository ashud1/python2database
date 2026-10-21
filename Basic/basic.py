my_stuff={"key1":"value1","key2":"value2"}
print(my_stuff['key1'])

def my_func(param1='default'):
    """
    This is doc string
    """

# lambda expression

# filter 

mylist=[1,2,3,5,6,7,8,9]


# print(even_bool(mylist))

evens=filter(lambda num: num%2 == 0,mylist)

print(list(evens))

# Scoping of variables
x=25
def my_func():
    x=50
    return x
# print(x)
# print(my_func())

my_func()
print(x)

# Local 

lambda x:x**2

# enclosing function locals 

name='This is a global name!'

def greet():
    # name="sammy"

    def hello():
        print ("hello "+name)
    hello()

greet()

