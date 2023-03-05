import string
import os

# Create a directory to store the files
if not os.path.exists('text_files'):
    os.mkdir('text_files')

# Generate the filenames and create the files
for letter in string.ascii_uppercase:
    filename = os.path.join('text_files', letter + '.txt')
    with open(filename, 'w') as file:
        file.write(letter + '\n')

print("Text files created in 'text_files' directory.")
