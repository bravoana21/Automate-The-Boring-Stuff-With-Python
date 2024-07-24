import re

def validDate(day, month, year):
    day = int(day)
    month = int(month)
    year = int(year)
    if year < 1000 or year > 2999 or month < 1 or month >12 or day < 1:
        return False
    elif month in [4, 6, 9, 11] and day <= 30:
        return True
    elif month == 2:
        if day <= 28:
            return True
        elif day == 29:
            if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
                return True
            else:
                return False
        else:
            return False
    elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
        return True
    else:
        return False

def detectDate(date):
    dateRegex = re.compile(r'^(\d{2})/(\d{2})/(\d{4})$')
    match = dateRegex.search(date)
    if match:
        day = match.group(1)
        month = match.group(2)
        year = match.group(3)
        if validDate(day, month, year) == True:
            return day+'/'+month+'/'+year
        else:
            return 'No match'
    else: 
        return 'No match'
 
   
# Valid Test Cases
print(detectDate('29/02/2020'))
print(detectDate('28/02/2019'))
print(detectDate('01/01/2000'))
print(detectDate('31/12/2999'))
print(detectDate('15/07/1500'))
print(detectDate('01/04/1000'))

# Invalid Test Cases
print(detectDate('32/01/2000'))
print(detectDate('15/13/2000'))
print(detectDate('29/02/2019'))
print(detectDate('15/07/0999'))
print(detectDate('15/07/3000'))
print(detectDate('00/01/2000'))
print(detectDate('15/00/2000'))
print(detectDate('31/04/2000'))

# Edge Cases
print(detectDate('01/01/1000'))
print(detectDate('31/12/2999'))
print(detectDate('29/02/2400'))
print(detectDate('29/02/2100'))

# Format Check Test Cases
print(detectDate('15-07-2000'))
print(detectDate('2000/07/15'))
print(detectDate('/07/2000'))
print(detectDate('15//2000'))
print(detectDate('15/07/'))