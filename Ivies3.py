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
    event = event.split("Event ")
    print(event[1])
    event = event[1].replace("<span></span>", "")
    event2 = event.split("\n")
    list_of_lines = []
    for line in event2:
        if cutsplits(line):
            list_of_lines.append(line)
    return list_of_lines

def cutsplits(string):
    prog = re.compile('\ \d+\ +[A-Z]')
    result = prog.search(string)
    if "Meet Record" in string:
        result=False
    if "Pool Record" in string:
        result=False
    if result:
        return string

def extract_place(line):
    return int(line[:3])
    
def extract_name(line):
    return line[4:20]

def extract_class(line):
    return line[21:23]

def extract_school(line):
    return line[24:40]
    
def extract_prelim_time(line):
    return line[42:50]

def extract_final_time(line):
    return line[53:60]
    
def extract_points(line):
    try:
        return float(line[69:])
    except ValueError:
        return 0

def dictify_line(event, line):
    dict1 = {}
    rank = extract_place(line)
    name = extract_name(line)
    year = extract_class(line)
    school = extract_school(line)
    prelim = extract_prelim_time(line)
    final = extract_final_time(line)
    points = extract_points(line)
    dict1.update({'Event': event, 'Rank': rank, 'Name': name, 'Year': year, 'School': school, 'Prelims': prelim, 'Finals':final, 'Points':points}) 
    return dict1

rows_list = []

for event in list_of_events[1]:
    line_list = get_event(event)
    event_num = line_list[0][:3]
    for line in line_list[1:]:
        dict2 = dictify_line(event_num, line)
        rows_list.append(dict)   

print(type(rows_list[1]))
df
