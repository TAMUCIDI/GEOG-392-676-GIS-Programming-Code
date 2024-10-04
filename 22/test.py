from functools import reduce

def lambdaTest():
    isEven = lambda num: num % 2
    print(isEven(5))

def mapTest():
    x = [2, 3, 4, 5, 6, 7, 8]
    squareEm = lambda num: num ** 2
    y = list(map(squareEm, x))
    z = map(squareEm, x)
    print(z)

def filterTest():
    x = [2, 3, 4, 5, 6, 7, 8]
    y = list(filter(lambda num: num % 2 == 0, x))
    z = list(filter(lambda num: num % 2, x))
    print(y)
    print(z)

def reduceTest():
    x = [2, 3, 4, 5, 6, 7, 8]
    add = lambda total, num: total + num
    summation = reduce(add, x)
    print(summation)

def fib(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

def generatorTest():
    for x in fib(6):
        print(x)



# lambdaTest()
# mapTest()
# filterTest()
# reduceTest()
generatorTest()