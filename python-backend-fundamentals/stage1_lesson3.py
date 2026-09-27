# Q1

# What is the output?

# try:
#     x = 10 / 0
#     print("A")
# except ZeroDivisionError:
#     print("B")

# print("C")
# answer  b and c because When the try block is being executed in the first line, an error happened, so it went to accept. Accept runs, then goes to the main execution line, and c printed

# Q2

# What is the output?

# try:
#     x = int("hello")
# except ValueError:
#     print("Invalid")

# else:
#     print("Success")

# finally:
#     print("Done")

# answer Success, then done, because if `try` blocks run successfully, then `else` will be printed, and `finally` will be printed eventually until it's not fixed. Even if `try` is running and `except` is running, `finally` will run eventually. 

# Q3

# What happens here?

# def create_user(name):
#     if not name:
#         raise ValueError("Name is required")

#     return {"name": name}

# print(create_user(""))

# Does it print a dictionary, None, or something else?

# And why?

# asnwer It will raise the error "name is required" because we are passing the empty string, and an empty string is a false value. Not false is true, so the raise ValueError will run, and it will return `name` and `None`. 

# Q4 — important

# What's the difference between:

# import math

# and:

# from math import sqrt

# In `import math`, we will get all the functions and methods from `math`, so we can use `math.pow`, `math.sqrt`, `math.add`. From `from math import sqrt`, we are only importing a single method, that is, `sqrt`, so we can directly use `sqrt` and write it. 

# Q6 — Flask architecture

# Suppose we have:

# backend/
# ├── routes/
# │   └── tasks.py
# └── services/
#     └── supabase.py

# Why would we put Supabase database logic inside:

# services/supabase.py

# instead of writing all the database code directly inside:

# routes/tasks.py

# This one is less about Python syntax and more about backend architecture, so think carefully.

# answer We have to write the backend Supabase database logic inside Supabase .env because this is Modular approach: writing the routes, task route code in tasks.py, and Supabase database-related code in supabase.py. At the time of debugging, we should find the bugs very easily. Thinking in this approach is helping us. 

# Q7 — interview question

# What's the difference between:

# raise ValueError("Invalid")

# and:

# print("Invalid")

# Don't just say "one throws error." Explain what happens to program execution.\';[p]
# In `raise ValueError`, Python is generating an error that the user has set to throw an error: `invalid`, but in `print invalid`, it is printing an error. There is no reason behind it. 