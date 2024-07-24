# Question 21

import re

def lastNameWatanabe(name):
    watanabeRegex = re.compile(r'^[A-Z][a-zA-Z]+\s(Watanabe)$')
    real_watanabe = watanabeRegex.search(name)
    if real_watanabe:
        return real_watanabe.group()
    else:
        return 'No match'
    
# test cases
print(lastNameWatanabe('Haruto Watanabe'))
print(lastNameWatanabe('haruto Watanabe'))
print(lastNameWatanabe('Alice Watanabe'))
print(lastNameWatanabe('Mr. Watanabe'))
print(lastNameWatanabe('RoboCop Watanabe'))
print(lastNameWatanabe('Watanabe'))
print(lastNameWatanabe('Haruto watanabe'))