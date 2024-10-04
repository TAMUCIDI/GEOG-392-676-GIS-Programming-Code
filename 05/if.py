# i = 5
# k = input("Please provide a number: ")

# if int(k) < i:
#     print("The number you have provided is less than our value.")
# else:
#     # print("The number you have provided is greater than our value.")
#     if int(k) < 10:
#         print("The number you have provided is greater than our value BUT less than 10.")
#     else:
#         print("The number you have provided is greater than our value AND greater than or equal to 10.")

i = 5
k = input("Please provide a number: ")

if int(k) < i:
    print("The number you have provided is less than our value.")
elif int(k) == i:
    print("The number you have provided is equal to our value.")
else:
    print("The number you have provided is greater than our value.")