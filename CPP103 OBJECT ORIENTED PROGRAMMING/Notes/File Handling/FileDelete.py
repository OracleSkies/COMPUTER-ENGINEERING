import os

if os.path.exists("demo.txt"): # error handler that checks if file exists
    os.remove("demo.txt")
else:
    print("The file does not exist")