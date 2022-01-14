#!/usr/bin/env python3
"""A program that counts the number of comic books a publisher has made in a year."""
import csv

marvel = 0
dc = 0
other_pub = 0

with open('brett_comics.txt', 'r') as file:
    reader = csv.reader(file, delimiter = ';')
    for row in reader:
        if row[3] == "Marvel Comics":
            marvel += 1
        elif row[3] == "DC Comics":
            dc += 1
        else:
            other_pub += 1

print(f"""Marvel Comics published {marvel} comic books.\nDC published {dc} comic books.\nOther publishers published {other_pub} comic books.""")
