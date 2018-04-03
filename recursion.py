# RECURSION

def recursion_factorial(n):
   if n == 1:
       return n
   else:
       return n*recursion_factorial(n-1)

print(recursion_factorial(3))
print(recursion_factorial(7))


def while_loop_factorial(n):
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
    return factorial

print(while_loop_factorial(3))
print(while_loop_factorial(7))
