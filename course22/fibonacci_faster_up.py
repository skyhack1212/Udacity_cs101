#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    before, after = 0, 1
    for i in range(0,n):
        before, after = after, before+after
    return before



print fibonacci(36)
#>>> 14930352
