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
    event = requests.get("http://www.neswim.com/2016mensivy/"+ event + ".htm").text
    return event

event = get_event("160225F002")
#event2 = event.split("Meet Record:M ")[1]
event3 = event.split("Men - Team Rankings")[0]

print("~"*100)
print("event = ")
print("")
print(event[:500])
