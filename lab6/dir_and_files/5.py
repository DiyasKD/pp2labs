filename = input("Enter a filename: ")
s = str(input())
list_to_write = s.split()

with open(filename, 'w') as file:
    for item in list_to_write:
        file.write("%s\n" % item)

print("List written to file:", filename)
