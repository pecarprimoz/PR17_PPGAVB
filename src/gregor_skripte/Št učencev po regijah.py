import csv
from collections import defaultdict
from csv import DictReader

class Regija:
    def __init__(self, n):
        self.vals = n * [0]
        self.c = 0
    def __iadd__(self, a):
        a = list(map(float, a))
        for i, x in enumerate(a):
            self.vals[i] += x
        self.c += 1
        return self

    def __str__(self):
        return ";".join(list(map(lambda x: str(x).replace(".", ","), [self.c] + self.vals + list(map(lambda x: x/self.c, self.vals)))))+"\n"

reader = DictReader(open("Št učencev po regijah.tab", "rt", encoding="utf-8"), delimiter='\t')
ucenci = defaultdict(lambda: Regija(5))
next(reader)
next(reader)
for row in reader:
    ucenci[row["REGIJA"]] += [row["ST_UC"],row["ST_DEK"],row["ST_ROM"],row["ST_OPB"],row["ST_ODL_USM"]]

header_xs = [
    "število učencev",
    "število deklet",
    "število romov",
    "število učencev v podaljšanem bivanju",
    "število otrok z odločbo o usmeritvi"
]


with open('Regije.csv', 'w') as file:
#     w = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    file.write(";".join(['regija', 'c'] + header_xs + list(map(lambda x: 'povprečno '+x, header_xs)))+"\n")

    for regija ,ucenec in ucenci.items():
        file.write(regija + ";" + str(ucenec))
        # w.writerow([regija] + ucenec.get_list())