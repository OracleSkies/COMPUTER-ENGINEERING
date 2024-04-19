f = open("demo.txt", "r")

#reads the file
print(f.read())
"""output:
Hello! Welcome to Demo File!
This file is for testing
Good Luck and Dangal Greetings"""

print(f.readline())
"""output:
Hello! Welcome to Demo File!"""

print(f.readlines())
"""output:
['Hello! Welcome to Demo File!\n', 'This file is for testing\n', 'Good Luck and Dangal Greetings ']"""

#closes the file
f.close()