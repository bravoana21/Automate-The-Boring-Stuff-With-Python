import re

def regex_strip_method(phrase, to_strip = None):
    if to_strip == None:
        to_strip = r'\s'
    else:
        to_strip = re.escape(to_strip)
    
    strip_regex = f'^[{to_strip}]+|[{to_strip}]+$'
    return re.sub(strip_regex, '', phrase)

# Test Cases
print(regex_strip_method('     phrase     '))
print(regex_strip_method('$$$Hello$$$', '$'))  # Output should be 'Hello'
print(regex_strip_method('   Hello, World!   '))  # Output should be 'Hello, World!' (default whitespace)
print(regex_strip_method('\t\t\tHello, World!\n\n\n', '\t\n'))  # Output should be 'Hello, World!'
print(regex_strip_method('###Hello###', '#'))  # Output should be 'Hello'
print(regex_strip_method('***Hello***', '*'))  # Output should be 'Hello'
print(regex_strip_method('---Hello---', '-'))  # Output should be 'Hello'
print(regex_strip_method('   '))  # Output should be '' (default whitespace)
print(regex_strip_method(''))  # Output should be '' (default whitespace)