def add_one(x):
    # No return statement at all
    result = x + 1
    return result
value = add_one(5)
print(value)


def divide_three(x):
    result = x / 3
    return result
value = divide_three(30)
print(value)


def greatest_twonumbers(x1,x2):
    result = x1 > x2
    return result
value=greatest_twonumbers(10,35)
print(value)  


def simple_interest(p,t,r):
    result = p*t*r
    return result
si=simple_interest(200,8,10)
print(si) 


def odd_even(n):
    result=n%2==0
    return result
number=odd_even(28)
print(number)

