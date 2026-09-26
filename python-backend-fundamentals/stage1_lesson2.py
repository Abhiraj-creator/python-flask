# Q1 — Scope

# What does this print?

# name = "Global"

# def outer():
#     name = "Outer"

#     def inner():
#         print(name)

#     inner()

# outer()
# answer is outer because according to legb rule it will look local no local then goes to enclosed and it finds the the variable 

# Q2 — Function objects

# What does this print?

# def greet():
#     print("Hello")

# x = greet

# x()

# And explain why.
# answer Hello because an function is an object in python greet is func and we are saving function body in variable x and calling x() so its same as greet() 


# Q3 — Function vs function call

# What's the difference between:

# execute(greet)

# and:

# execute(greet())

#  in execute(greet) execte func will be called and greet func body has benn passed as argument wihle in  execute(greet()) both execute anfd greet function are called immdeate 


# Q4 — Closure

# What does this print?

# def multiplier(x):

#     def multiply(number):
#         return number * x

#     return multiply


# double = multiplier(2)

# print(double(10))

# More importantly, explain why multiply() still knows that x is 2 after multiplier() has finished
# because of clouser even after the multiplier ecection is completed in memory it will rememeber that x is 2 and later in inner function it will use 2 and 10 and get 20 answer 


# Q5 — Decorator

# Without running it, tell me the output:

# def logger(function):

#     def wrapper():
#         print("Before")
#         function()
#         print("After")

#     return wrapper


# @logger
# def hello():
#     print("Hello")


# hello()

# so this means # @logger
# def hello():
#     print("Hello")

#  logger is called with an argument that is funtion named  hello in hello = wrapper wil be returned and before then our parameter function that is hello will be printed and then after 

# Q6 — Flask connection

# Explain in your own words what you think this means:

# @app.route("/tasks")
# def get_tasks():
#     return {"tasks": []}

# Don't just say "it creates an API." Explain what the decorator is doing to get_tasks

# app.routes here is an decorater with an argument /tasks= get_tasks and then returns the return body of get_tasks

# Q7 — *args / **kwargs

# What will this print?

# def test(*args, **kwargs):
#     print(args)
#     print(kwargs)

# test(10, 20, name="Abhiraj", age=21)

# args will be 10 and 20 becuase they are postional args whereas kwargs will print name:abhiraj and age:21 because htey are keyword args

# Q8 — Backend thinking

# Why would a Flask authentication decorator use:

# def wrapper(*args, **kwargs):

# instead of simply:

# def wrapper():
#  because from  fronted there can be data such as no unlabbeled data like 10 20 and aslo labeled data like name= abhiraj so to use it in backend we will use this *args and **kwargs

 