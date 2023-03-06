import string
import os

# Create a directory to store the files
if not os.path.exists('text_files'):
    os.mkdir('text_files')
os.chdir(r'C:\Users\Дияс\Desktop\Python\text_files')
# Generate the filenames and create the files
for letter in string.ascii_uppercase:
    file = open(letter + ".txt", 'x')
    

print("Text files created in 'text_files' directory.")
