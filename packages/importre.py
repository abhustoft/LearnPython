import re

# print an alphabetically sorted list of all functions in the re module, which contain the word find
#print(dir(re))

# Not good:
# print an alphabetically sorted list of all functions in the re module, which contain the word find

#Not good:
# find the word "find" in the list


# find the word "find" in list, print matches
for i in sorted(dir(re)):
    if "find" in i:
        print(i)


