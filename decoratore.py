def repeater(old_function):
    def new_function(*args, **kwds): # See learnpython.org/en/Multiple%20Function%20Arguments for how *args and **kwds works
        old_function(*args, **kwds) # we run the old function
        old_function(*args, **kwds) # we do it twice

    return new_function # we have to return the new_function, or it wouldn't reassign it to the value

@repeater
def multiply(num1, num2):
    print(num1 * num2)

#multiply(2, 3)

def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds) # modify the return value
    return new_function

@double_out
def multiply2(num1, num2):
    return num1 * num2

multiply2(2, 3)