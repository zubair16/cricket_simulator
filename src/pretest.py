import time
import random


# learn how this works lol :)
class Switch(dict):
    def __getitem__(self, item):
        for key in self.keys():                   # iterate over the intervals
            if item in key:                       # if the argument is part of that interval
                return super().__getitem__(key)   # return its associated value
        raise KeyError(item)

class Batsman:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability


class Bowler:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability


print("Pakistan vs England - Pakistan to bat first")
time.sleep(1)
print("Imam ul-Haq is on strike")
time.sleep(1)
print("Jofra Archer to open the bowling")
time.sleep(1)

imam = Batsman("Imam ul-Haq", 7)
jofra = Bowler("Jofra Archer", 9)

for i in range(1, 7, 1):
    outcome = random.randrange(1, 9) * (jofra.ability - imam.ability)
    outcome_text = Switch({
        range(1, 3): 'Out',
        range(4, 13): 'Dot',
        range(14, 15): 'Single',
        range(16, 17): 'Two',
        range(18): 'Four'
    })
    print(f"Ball {i} of over: {jofra.name} to {imam.name}")
    print(f"Outcome: {outcome_text[outcome]}")
    time.sleep(1)