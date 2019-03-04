#comment 1
import csv
import pprint
from datetime import datetime


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

# print(flights)
# pprint.pprint(flights)

# flights2 = {}
# for k, v in flights.items():
#     flights2[convert2ampm(k)] = v.title()
# pprint.pprint(flights2)

fts = {convert2ampm(k): v.title() for k, v in flights.items()}
# pprint.pprint(fts)

# print(set(fts.values()))

# when = {}
# for dest in set(fts.values()):
#     when[dest] = [k for k, v in fts.items() if v == dest]

when = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}

print(when)
