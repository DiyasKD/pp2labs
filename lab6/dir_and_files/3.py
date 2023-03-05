import os

path = input("Enter a path to test: ")

if os.path.exists(path):
    print("Path exists")
    dirname, filename = os.path.split(path)
    print("Directory name:", dirname)
    print("File name:", filename)
else:
    print("Path does not exist")
