import csv

f = open('files/attendees1.csv')

attendees1 = []

csv_f = csv.reader(f)

for row in csv_f:
  attendees1.append(row[2])


f.close()


f = open('files/attendees2.csv')

attendees2 = []

csv_f = csv.reader(f)

for row in csv_f:
  attendees2.append(row[2])


f.close()

attendees1 = set(attendees1)
attendees2 = set(attendees2)

print(attendees2.difference(attendees1))
