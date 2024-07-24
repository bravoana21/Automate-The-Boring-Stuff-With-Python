def collatz(number):
    try:
        number = int(number)
        if number % 2 == 0:
            evenResult = number // 2
            print(evenResult)
            return evenResult
        else:
            oddResult = 3 * number + 1
            print(oddResult)
            return oddResult
    except ValueError:
        print('The value you entered is not valid. It must be an integer.')
    
while True:
    print('Type an integer:')
    intUser = input()
    if collatz(intUser) == 1:
        break
