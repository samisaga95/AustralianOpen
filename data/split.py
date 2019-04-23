import csv
from itertools import groupby

for key, rows in groupby(csv.reader(open("10yearAUSOpenMatches.csv")),
                         lambda row: row[3]):
    with open("%s.csv" % key, "w") as output:
        for row in rows:
            output.write(",".join(row) + "\n")
