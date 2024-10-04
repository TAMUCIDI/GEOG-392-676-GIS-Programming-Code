# myList = []
# myList.append('a')
# myList.append('b')
# myList.append('c')
# myList.append('d')
# myList.append('a')
# myList.append('1')
# myList.append('2')
# myList.append('3')
# myList.append('4')

# numOfa = myList.count('a') # Returns a value of 2
# isEinList = 'e' in myList # Returns False as e is not in the list
# isBinList = 'b' in myList # Returns True as b is in the list
# indexOfA = myList.index('a') # Returns 0 as 0 is the first index with a
# indexOfOne = myList.index('1')
# print(indexOfOne)

# myTuple = ('a', 'b', 'c', 'a') 
# tuples = myTuple.count('a') # Returns a value of 2
# indexOfB = myTuple.index('b') # Returns a value of 1
# print(myTuple)
# print(tuples)
# print(indexOfB)


# languages = {
#     'Canada' : 'French',
#     'United States' : 'English',
#     'Mexico' : 'Spanish',
#     'Brazil' : 'Portuguese'
# }
# languages['Haiti'] = 'French'
# suriname = "Suriname"
# languages[suriname] = 'Dutch'

# print(languages["Suriname"])
# test = {1, 2}
# print(type(test))
# mySet = set()
# mySet.add(1)
# mySet.add(2)
# print(mySet) # Prints {1, 2}
# mySet.add(1)
# print(mySet) # Still prints {1, 2}
# otherSet = {5, 6, 7}
# mySet.update(otherSet)
# print(mySet)


mySet = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
otherSet = {'z', 'y', 'x', 'w', 'v', 'u', 'b', 'a'}

union = mySet.union(otherSet)
intersection = mySet.intersection(otherSet)
difference = mySet.difference(otherSet)

print(union)
print(intersection)
print(difference)