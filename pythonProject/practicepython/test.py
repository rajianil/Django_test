import os
print(os.getcwd())

def func1():
    var = [i*i for i in range(5)]
    return var

a=func1()
print(a)
check_num = lambda x: 'Num greater than 5' if x > 5 else 'Num not greater than 5'

num = [lambda x ,i=i : x*i for i in range(1,10)]
print(type(num))
for i in num:
    print(i(2))
num = [lambda x: x*i for i in range(1,10)]
#print(type(num(8)))

string="helrojwei"
print(string[1:8:2])
print(__file__)
