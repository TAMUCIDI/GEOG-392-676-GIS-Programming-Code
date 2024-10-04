numOne = int(input("First num: "))
operator = input("Operator: ")
numTwo = int(input("Second num: "))

if operator == '+':
    print("Result = ", (numOne + numTwo))
elif operator == '-':
    print("Result = ", (numOne - numTwo))
elif operator == '*':
    print("Result = ", (numOne * numTwo))
elif operator == '/':
    print("Result = ", (numOne / numTwo))
else:
    print("Invalid operator")

# x = [1, 2, 3, 4, 5]
# total = 0
# for num in x:
#     if num == 3:
#         continue
#     else:
#         total += num

# print(total)