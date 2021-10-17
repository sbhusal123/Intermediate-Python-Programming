import traceback

"""
- Contains the function calls made in your code at a specific point.
- Also known as stack trace, stack traceback, backtrace
"""

def a():
    raise Exception("Some exception occured")

def b():
    a()

def c():
    b()

# Call order: c -> b -> a -> Exception
try:
    c()
except:
    print(traceback.format_exc())

"""
Output:

Traceback (most recent call last):
  File "traceback.py", line 19, in <module>
    c()
  File "traceback.py", line 15, in c
    b()
  File "traceback.py", line 12, in b
    a()
  File "traceback.py", line 9, in a
    raise Exception("Some exception occured")
Exception: Some exception occured
"""