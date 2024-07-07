# Question 20

import re

def findNumberWithCommas(number):
    numberRegex = re.compile(r'^\d{1,3}(,\d{3})*$')
    true_number = numberRegex.search(number)
    if true_number:
        return true_number.group()
    else:
        return 'No match'
    
# test cases
print(findNumberWithCommas('42'))
print(findNumberWithCommas('12,34,567'))
print(findNumberWithCommas('1,234'))
print(findNumberWithCommas('1234'))
print(findNumberWithCommas('6,368,745'))