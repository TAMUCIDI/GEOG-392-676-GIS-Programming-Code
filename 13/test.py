numbers = [1, 2, 3, 4, 5, 6]
raisedNums = [x ** 3 for x in numbers if x % 2 == 0]
print(raisedNums) # Prints [1, 8, 27, 64, 125, 216]