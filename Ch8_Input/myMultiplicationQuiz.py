import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    
    tries = 0
    start = time.time()
    
    while (time.time() - start) < 8 and tries < 3:
        answer = input('#%s: %s x %s = ' % (questionNumber, num1, num2))
        if (time.time() - start) >= 8:
            break
        try:
            if int(answer) == (num1 * num2):
                print('Correct!')
                correctAnswers += 1
                break
            else:
                print('Incorrect!')
                tries += 1

        except:
            print('Incorrect!')
            tries += 1
        
    if tries == 3:
        print('Out of tries!')
    
    elif (time.time() - start) >= 8:
        print('Out of time!')
        
    time.sleep(1) # Brief pause to let user see the result.

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))