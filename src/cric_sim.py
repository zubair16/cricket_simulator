import time
import random


class Match:
    def __init__(self, innings, over, ball, runs, wickets):
        self.innings = innings
        self.over = over
        self.ball = ball
        self.runs = runs
        self.wickets = wickets


class Batsman:
    def __init__(self, name, hand, rating, momentum):
        self.name = name
        self.hand = hand
        self.ability = rating
        self.momentum = momentum


class Bowler:
    def __init__(self, name, hand, style, rating, momentum):
        self.name = name
        self.hand = hand
        self.style = style
        self.rating = rating
        self.momentum = momentum


class Conditions:
    def __init__(self, pitch, weather):
        self.pitch = pitch
        self.weather = weather
        print(f"Today the weather is quite {self.weather} and the pitch is looking quite {self.pitch}")


def generate_conditions():
    weather_val = random.randrange(0, 2)

    if weather_val == 0:
        weather_type = "overcast"
        pitch_type = "green"
    else:
        weather_type = "sunny"
        sunny_pitch_val = random.randrange(0, 2)
        if sunny_pitch_val == 0:
            pitch_type = "dusty"
        else:
            pitch_type = "dead"

    day_condition = Conditions(pitch_type, weather_type)
    return day_condition


def simulate_delivery(cricket_match):
    cricket_match.ball = 0
    for ball in range(0, 6, 1):
        print(f"{cricket_match.over}.{cricket_match.ball}")
        cricket_match.ball += 1
        # time.sleep(1)


def main():
    cricket_match = Match(1, 0, 0, 0, 0)
    generate_conditions()

    for over in range(0, 50, 1):
        simulate_delivery(cricket_match)
        cricket_match.over += 1
        # time.sleep(1)


if __name__ == '__main__':
    main()
