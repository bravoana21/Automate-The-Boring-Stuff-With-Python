def listWithComma(list):
    listStr = ''
    for i in list:
        if list[len(list) - 1] == i:
            listStr += ' and ' + i
            return listStr
        listStr += i + ', '


spam = ['apples', 'bananas', 'tofu', 'cats']
print(listWithComma(spam))
print(listWithComma([]))