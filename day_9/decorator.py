"""Write a decorator called @log_function that prints the name of the 
function being called and its arguments before executing it.
"""

def log_function(func):

    def call_func_name(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        if args or kwargs:
            print(f"Arguments: {args if args else ''} {kwargs if kwargs else ''}")
        return func(*args, **kwargs)
    return call_func_name


@log_function
def greet(name):
    print(f"Hello, {name}!. How are you?")

greet("Alice") 

# Output: 
# Calling function: greet 
# Arguments: 'Alice'
# Hello, Alice. How are you today?


# Write a decorator @double_result that doubles the result returned by any function.

# Example:

def double_result(func):

    def double(*args,**kwargs):
        if args or kwargs in func:
            result = func(*args, **kwargs)
        return result * 2
    return double

@double_result
def add(x, y):
    return x + y

print("\nThe doubled result is: ", add(3, 4))  # Output: 14