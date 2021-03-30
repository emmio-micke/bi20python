def myfunc(n):
    return lambda a: a * n


my_doubler = myfunc(2)

print(my_doubler(5))
print(my_doubler(10))
print(my_doubler(2))

my_tripler = myfunc(3)

print(my_tripler(3))
print(my_tripler(5))
print(my_tripler(7))
