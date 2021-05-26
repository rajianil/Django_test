def max_of_two(x,y):
    if x>y:
        return x
    else:
        return y

def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))

print(max_of_two(2,6))
print(max(6,4,1))

def sum_list(numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum
print(sum_list([1,2,3,9]))

def mult_list(numbers):
    mult=1
    for i in numbers:
        mult*=i
    return mult

print(mult_list((1,2,3,2)))

def reverse_string(stringval):
    return stringval[::-1]
print(reverse_string("hello13"))
def rev_str(stringval):
    index=len(stringval)
    revval=''
    while index>0:
        revval+=stringval[index-1]
        index=index-1
    return revval

print(rev_str("hellore123"))

def factorial(n):
    fact=1
    while n>0:
        print(n)
        fact=n*fact
        n=n-1
    return fact

print(factorial(5))

def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"
print(hello())
## returns "<b><i><u>hello world</u></i></b>"
