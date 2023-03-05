import os

filename = input("Enter the filename to delete: ")

if not os.path.exists(filename):
    print(filename, "does not exist")
elif not os.access(filename, os.W_OK):
    print(filename, "is not writable")
else:
    os.remove(filename)
    print("File", filename, "has been deleted")
