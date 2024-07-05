import random
import zombiedice
'''
class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
'''
class RandomDecisionZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        if diceRollResults is not None and random.choice([True, False]):
                diceRollResults = zombiedice.roll()

class TwoBrainsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains >= 2:
                break
            diceRollResults = zombiedice.roll()

class TwoShotgunsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns >= 2:
                break
            diceRollResults = zombiedice.roll()

class RollUpToFourTimesZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        rolls = random. randint(1, 4)
        shotguns = 0
        for r in range(rolls):
            diceRollResults = zombiedice.roll()
            if diceRollResults is None:
                break
            shotguns += diceRollResults['shotgun']
            if shotguns >= 2:
                break

class MoreShotgunsThanBrainsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        shotguns = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun'] 
            if shotguns > brains:
                break
            diceRollResults = zombiedice.roll()

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    # MyZombie(name='My Zombie Bot'),
    RandomDecisionZombie(name='Random Decision'),
    TwoBrainsZombie(name='Two Brains'),
    TwoShotgunsZombie(name='Two Shotguns'),
    RollUpToFourTimesZombie(name='Roll Up to Four Times'),
    MoreShotgunsThanBrainsZombie(name='More Shotguns Than Brains'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)