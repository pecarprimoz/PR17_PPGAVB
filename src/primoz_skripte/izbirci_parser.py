'''
    README IF USING
    prebere vsebino izbircov in naredi slovar kjer je ključ šola, vrednost pa array izbirnih predmetov
'''

txtPathFile="../txts/correcttxt_new.txt"
f=open(txtPathFile, 'r', encoding = "UTF-8")
new=[]
for ind,line in enumerate(f):
    vsebina=line.split(',')
    new.append(list())
    for val in vsebina:
        new[ind].append(val.strip('\'').strip('"').replace("/i/","").replace('\n',''))
from collections import defaultdict
sole_in_izbirci=defaultdict(list)
for vsebina in new:
    if vsebina not in sole_in_izbirci[vsebina[1]]:
        sole_in_izbirci[vsebina[1]].append(vsebina[2])

#print(sole_in_izbirci["Osnovna šola Ledina"])