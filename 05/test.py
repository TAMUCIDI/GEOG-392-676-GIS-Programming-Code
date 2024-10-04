# x = 1
# y = 2

# print(x > y and x == y) # False, since both expressions are false
# print(x < y and x == y) # False, since only one expression is true
# print(x < y and x != y) # True, since both expressions are true

# print(x > y or x == y)  # False, since both expressions are false
# print(x > y or x != y)  # True, since one expression is true
# print(x < y or x == y)  # True, since one expression is true
# print(x < y and x != y) # True, since both expressions are true

# print(not(x != y))      # False, (x != y) resolves to true then we flip it to false

# languages = ["C", "C++", "Python", "Delphi", "Perl", "Erlang", "Javascript", "Java", "Pascal", "BASIC", "Assembly", "F#", "C#", "Swift", "Objective-C", "Kotlin", "R", "Scala", "Ruby", "PHP"]
# for language in languages:
#     print(language)

# magicNumber = "16"
# userInput = input("Guess the magic number: ")

# while userInput != magicNumber:
#     userInput = input("Guess the magic number: ")

# while 2 > 1:
#     print("True")

count = 9
count %=4
print(count)