filename = input("Enter a filename: ")

with open(filename, 'r') as file:
    lines = file.readlines()
    num_lines = len(lines)
    print("Number of lines:", num_lines)
