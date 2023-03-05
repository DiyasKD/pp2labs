filename = input("Enter a filename: ")
list_to_write = ['apple', 'banana', 'cherry', 'date']

with open(filename, 'w') as file:
    for item in list_to_write:
        file.write("%s\n" % item)

print("List written to file:", filename)
