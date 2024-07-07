import re

def findNumberWithCommas(number):
    matches = []
    numberRegex = re.compile(r'(\d{1,3}|,\d{3}|)')
    for slice in numberRegex.findall(number):
        matches.append(slice)
    if len(matches) > 0:
        return ''.join(matches)
    else:
        return False

# test cases
print(findNumberWithCommas('42'))
print(findNumberWithCommas('12,34,567'))
print(findNumberWithCommas('1,234'))
print(findNumberWithCommas('1234'))
print(findNumberWithCommas('6,368,745'))