import os
path = input("Enter a path: ")
option = input("Enter 'd' to list directories, 'f' to list files, or 'a' to list all: ")

if option == 'd':
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)
elif option == 'f':
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)
elif option == 'a':
    for item in os.listdir(path):
        print(item)
else:
    print("Invalid option")
