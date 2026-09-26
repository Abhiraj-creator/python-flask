 # question 1
# x = 10
# y = x

# y = 20

# print(x)
# print(y)
#my answer is  20 20

# question 2

# tasks = []

# if not tasks:
#     print("No tasks")
# else:
#     print("Tasks exist")
# answer no tasks
# question 3

# def create_task(title,desc,assign_to):
#     return {
#         "title":title,
#         "description":desc,
#         "assign_to":assign_to
#     }
    
# result =create_task('flask','learning flask backend', 'abhiraj')
# print(result)

# question 4 
# differnece between data["email"] and data.get("email") is first one returns error is there is no email filed but second one will give none if there is no feild 

# question 5
#What does **kwargs do?

# **kwargs accepts an dictonary as parameter of an function and then does opertion of dict 
#like

# def dictonary(**kwargs):
#     return kwargs

# dictonary({
#     "name":"abhiraj"
# })

# Question 6 — Backend-relevant

# Suppose Next.js sends:

# {
#     "title": "Learn Flask",
#     "assigned_to": "abc123"
# }

# What Python data structure would Flask typically work with after parsing this JSON?

# And how would you retrieve title and assigned_to?

# i would use dict because json is similar to dict 

# data = get_data()
# title =data['title']
# assigned_to =data['assined_to']
# something like it 

# Question 7 — Interview level

# Explain the difference between:

# mutable
# immutable

# and give 2 examples of each.

# mutable is changeable andimmuatble iis not chnagable like mutable list dict set imutable tuple int float str 


# Question 8 — Practical

# Explain what this command does:

# python -m venv .venv

# and why we need it.

# this command will create an sepaeate enviroment where we can install our dependices not installing in global space to get rid of many problems like with global python packages 