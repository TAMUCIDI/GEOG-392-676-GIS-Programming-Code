import re

# address = "123 Fake Street"

# match = re.search("(?i)street$", address)

# print(match)

# import re
# result = re.search("i", "abcdefghijklmnopqrstuvwxyz")
# print(result) # Prints <_sre.SRE_Match object; span=(8, 9), match='i'>

# s = '100 NORTH BROAD ROAD'
# s[:-4] + s[-4:].replace('ROAD', 'RD.')
# s = s[:-4] + s[-4:].replace('ROAD', 'RD.')
# print(s)

# import re
# result = re.match("cat", "c")
# print(result) # Prints <_sre.SRE_Match object; span=(0, 1), match='c'>
# result = re.match("a", "cat") # Prints None since "a" is not at the beginning of our string
# print(result)


# import re
# s = '100 NORTH BROAD ROAD'
# result = re.sub('ROAD$', 'RD.', s)
# print(result) # Prints

x = "6 geese a-layin 51 golden rings 4 calling birds 33 French hens 2 turtle doves 91 partridge in a pear tree"
result = re.findall(r"\d+", x)
print(result)