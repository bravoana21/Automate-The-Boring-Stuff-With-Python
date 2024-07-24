import re

def strongPassword(password):
    lengthRegex = re.compile(r'.{8,}')
    uppercaseRegex = re.compile(r'[A-Z]')
    lowercaseRegex = re.compile(r'[a-z]')
    digitRegex = re.compile(r'\d')
    if lengthRegex.search(password) and uppercaseRegex.search(password) and lowercaseRegex.search(password) and digitRegex.search(password):
        return password
    return 'No match'

# Test cases
print(strongPassword('Password123'))  
print(strongPassword('password123'))  
print(strongPassword('PASSWORD123'))  
print(strongPassword('Password'))     
print(strongPassword('Pass12'))