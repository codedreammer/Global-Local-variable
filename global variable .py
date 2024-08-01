x = 10
print(x)

def hello():
    x = 5
    print(f"the local x is {x}")
    print("Hello akshay")

def my_function():
    global x 
    x = 4
    y = 5 
    print(y)

print(f"The local global x is {x}")
hello()
x= 5
print(f"the global x is {x}")


my_function()
print(x)
