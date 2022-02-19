# How To Use *args and **kwargs to call a function
# Usage of *args. *args is used to send a non-keyworded variable length argument list to the function.
# **kwargs allows you to pass keyworded variable length of arguments to a function. You should use **kwargs if you want to handle named arguments in a function. Here is an example to get you going with it:

# So here we will see how to call a function using *args and **kwargs. Just consider that you have this little function:

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# Now you can use *args or **kwargs to pass arguments to this little function. Here’s how to do it:

# first with *args
args = ("two", 3, 5)
test_args_kwargs(*args)
# arg1: two
# arg2: 3
# arg3: 5

# now with **kwargs:
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)
# arg1: 5
# arg2: two
# arg3: 3

# Order of using *args **kwargs and formal args
some_func(fargs, *args, **kwargs)

# When to use them?
# It really depends on what your requirements are. The most common use case is when making function decorators (discussed in another chapter). Moreover it can be used in monkey patching as well. Monkey patching means modifying some code at runtime. Consider that you have a class with a function called get_info which calls an API and returns the response data. If we want to test it we can replace the API call with some test data. For instance:

# import someclass

# def get_info(self, *args):
#     return "Test data"

# someclass.get_info = get_info
