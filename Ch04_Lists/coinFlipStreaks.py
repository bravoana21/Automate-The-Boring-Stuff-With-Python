import random

numberOfStreaks = 0
numberOfExperiments = 10000

for experimentNumber in range(numberOfExperiments):
    # Code that creates a list of 100 'heads' or 'tails' values.
    headsAndTails = []
    for j in range(100):
        if random.randint(0, 1)  == 0:
            headsAndTails.append('H')
        else:
            headsAndTails.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    timesRepeated = 0
    for i in range(1, 100):
        if headsAndTails[i] == headsAndTails[i - 1]:
            timesRepeated += 1
            if timesRepeated == 5:
                numberOfStreaks += 1
                break
        else:
            timesRepeated = 0

print('Chance of streak: %s%%' % (numberOfStreaks / numberOfExperiments * 100))