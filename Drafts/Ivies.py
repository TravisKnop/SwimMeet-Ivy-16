import datetime
import requests
import json
import re
import pandas as pd

Harvard = []
Princeton = []
Penn = []
Cornell = []
Columbia = []
Dartmouth = []
Brown = []
Yale = []

list_of_events = [
    "160225F001", "160225F002", "160225F003", "160225F004", "160225F005", "160225F006",
    "160225F007", "160225F008", "160225F009", "160225F010", "160225F011", "160225F012", "160225F013", "160225F014",
    "160225F015", "160225F016", "160225F017", "160225F018", "160225F019", "160225F020", "160225F021"
]

def get_event(event):
    return requests.get("http://www.neswim.com/2016mensivy/"+ event + ".htm").text

def get_score(string):
    score = string.split("Team Rankings")[1]
    first = score.split("1. ")[1].split("2. ")[0]
    second = score.split("2. ")[1].split("3. ")[0]
    third = score.split("3. ")[1].split("4. ")[0]
    fourth = score.split("4. ")[1].split("5. ")[0]
    fifth = score.split("5. ")[1].split("6. ")[0]
    sixth = score.split("6. ")[1].split("7. ")[0]
    seventh = score.split("7. ")[1].split("8. ")[0]
    eighth = score.split("8. ")[1]
    places = [first, second, third, fourth, fifth, sixth, seventh, eighth]
    for place in places:
        if "Harvard" in place:
            for t in place.split():
                try:
                    Harvard.append(float(t))
                except ValueError:
                    pass
        elif "Princeton" in place:
            for t in place.split():
                try:
                    Princeton.append(float(t))
                except ValueError:
                    pass
        elif "Yale" in place:
            for t in place.split():
                try:
                    Yale.append(float(t))
                except ValueError:
                    pass
        elif "Penn" in place:
            for t in place.split():
                try:
                    Penn.append(float(t))
                except ValueError:
                    pass
        elif "Brown" in place:
            for t in place.split():
                try:
                    Brown.append(float(t))
                except ValueError:
                    pass
        elif "Cornell" in place:
            for t in place.split():
                try:
                    Cornell.append(float(t))
                except ValueError:
                    pass
        elif "Columbia" in place:
            for t in place.split():
                try:
                    Columbia.append(float(t))
                except ValueError:
                    pass
        elif "Dartmouth" in place:
            for t in place.split():
                try:
                    Dartmouth.append(float(t))
                except ValueError:
                    pass
                

    

for event in list_of_events:
    name = get_event(event)
    get_score(name)

def save(DataFrame):
    Timestamp = '{:%Y-%m-%d %H:%M}'.format(datetime.datetime.now()))
    DataFrame.to_csv("IvyTeamScores" + Timestamp + ".csv")

scores = pd.DataFrame({"Harvard": Harvard, "Princeton": Princeton, "Penn": Penn, "Columbia": Columbia, "Cornell": Cornell, "Dartmouth": Dartmouth, "Yale": Yale, "Brown": Brown})
save(scores)
newscores = pd.read_csv("IvyTeamScores.csv")
newscores

