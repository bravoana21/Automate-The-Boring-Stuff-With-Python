import pyinputplus as pyip

total = 0.00
print('Welcome to Ana\'s Loncheria!')

bread_prompt = 'What type of bread would you like for your sandwich?\n'
bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], bread_prompt)
if bread_type == 'wheat':
    total += 0.19
elif bread_type == 'white':
    total += 0.14
else:
    total += 0.21

protein_prompt = 'What type of protein do you prefer?\n'
protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], protein_prompt)
if protein_type == 'chicken':
    total += 0.21
elif protein_type == 'turkey':
    total += 0.18
elif protein_type == 'ham':
    total += 0.16
else:
    total += .16

cheese_approval_prompt = 'Would you like to add cheese?\n'
cheese_decision = pyip.inputYesNo(cheese_approval_prompt)
if cheese_decision == 'yes':
    cheese_prompt = 'In that case, what type of cheese?\n'
    cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], cheese_prompt)
    if cheese_type == 'cheddar':
        total += 0.25
    elif cheese_type == 'Swiss':
        total += 0.23
    else:
        total += 0.31

mayo_prompt = 'Do you want some mayo?\n'
mayo_decision = pyip.inputYesNo(mayo_prompt)
if mayo_decision == 'yes':
    total += 0.08

mustard_prompt = 'Do you want some mustard?\n'
mustard_decision = pyip.inputYesNo(mustard_prompt)
if mustard_decision == 'yes':
    total += 0.03

lettuce_prompt = 'Do you want some lettuce?\n'
lettuce_decision = pyip.inputYesNo(lettuce_prompt)
if lettuce_decision == 'yes':
    total += 0.33

tomato_prompt = 'Do you want some tomatos?\n'
tomato_decision = pyip.inputYesNo(tomato_prompt)
if tomato_decision == 'yes':
    total += 0.04

amount_prompt = 'How many sandwiches do you want?\n'
amount = pyip.inputInt(amount_prompt, min=1)
total *= amount ** 2

service = 0.15 * total
total += service

print('You have a total cost of $' + str(round(total, 2)) + ' for your sandwich(es). Enjoy your day :)')