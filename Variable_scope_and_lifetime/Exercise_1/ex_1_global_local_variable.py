def my_function(a):     # a is local variable
    b = a -2    # b is local variable
    return b

c = 3   #c  is global variable

if c > 2:
    d = my_function(5)  # d is global variable
    print(d)