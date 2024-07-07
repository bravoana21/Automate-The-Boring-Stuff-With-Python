# Question 22

import re

def catchWords(sentence):
    sentenceRegex = re.compile(r'^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$', re.I)
    real_sentence = sentenceRegex.search(sentence)
    if real_sentence:
        return real_sentence.group()
    else:
        return 'No match'
    
# test cases
print(catchWords('RoboCop eats apples.'))       # No match
print(catchWords('Alice eats apples.'))
print(catchWords('Bob pets cats.'))
print(catchWords('ALICE THROWS FOOTBALLS.'))    # No match
print(catchWords('Carol throws baseballs.'))
print(catchWords('Alice throws Apples.'))
print(catchWords('Carol eats 7 cats.'))         # No match
print(catchWords('BOB EATS CATS.'))