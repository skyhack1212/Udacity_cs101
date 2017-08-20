#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = b = 1
    i = 2
    result = 0
    while i < n:
        result = a + b
        a, b = b, result
        i += 1
    return result



print fibonacci(36)
#>>> 14930352
