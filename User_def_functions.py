#function without parameters
def square():
    """Return the square of a value"""
    new_val = 4 ** 2
    print(new_val)
#calling the function
square()

#function with parameters
def square1(val):
    """Return the square of a value"""
    new_val2 = val ** 2
    print(new_val2)
square1(65)

#we can use return to assign to a new variable 
def square2(val1):
    """Returns cube of a value"""
    new_val3 = val1 ** 3
    return new_val3
#assign to new variable
num = square2(90)
print(num)

#passing multiple parameters
def raise_to_power(value1, value2):
    """Raise value1 to the power of value2"""
    new_val4 = value1 ** value2
    return new_val4
result = raise_to_power(5, 6)
print(result)

#we can also return the value as tuple
#tuples are immutable and denoted with ()
def raise_both(value1, value2):
    """Raise value1 to the power of value2 and vicxeversa"""
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1

    new_tuple = (new_value1, new_value2)
    return new_tuple
result = raise_both(15, 10)
print(result)
#unpacking tuples
num1, num2 = result
print(num1)