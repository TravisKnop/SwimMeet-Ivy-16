import requests
import json
import re
import pandas as pd

list_of_events = [
    "160225F001", "160225F002", "160225F003", "160225F004", "160225F005", "160225F006",
    "160225F007", "160225F008", "160225F009", "160225F010", "160225F011", "160225F012", "160225F013", "160225F014",
    "160225F015", "160225F016", "160225F017", "160225F018", "160225F019", "160225F020", "160225F021"
]

def get_event(event):
    event = requests.get("http://www.neswim.com/2016mensivy/"+ event + ".htm").text
    return event

event = get_event("160225F002")
event = event.replace("<span></span>", "")
event2 = event.split("\n")

def cutsplits(string):
    prog = re.compile('\ \d+\ +[A-Z]')
    result = prog.search(string)
#    alphabet = 'aeiou'
 #   for character in string:
 #       if character in alphabet:
    if result:
        return string


print("")
print("")
print("")
print("")
print("")
print("START PROGRAM HERE")
print("")
print("")
print("")
print("")

all = []
for line in event2:
    text = cutsplits(line)
    if text:
        all.append(text)

for item in all:
    print(item)
