import os
import re

folder_path = input("Enter the folder path: ")
user_regex = input("Enter the regular expression to search for: ")
regex = re.compile(user_regex)

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        file = open(file_path, 'r')
        lines = file.readlines()
        file.close()
        for line in lines:
            if re.search(user_regex, line):
                print(f"Match found in {filename}: {line.strip()}")

print("\nSearch completed.")