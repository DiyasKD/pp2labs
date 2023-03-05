source_filename = input("Enter the source filename: ")
dest_filename = input("Enter the destination filename: ")

with open(source_filename, 'r') as source_file, open(dest_filename, 'w') as dest_file:
    dest_file.write(source_file.read())

print("File contents copied from", source_filename, "to", dest_filename)
