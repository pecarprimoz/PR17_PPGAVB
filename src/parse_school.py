'''
    README IF USING
    PathFile je pot do datoteke, ki jo spreminjamo
    PathWrite je pot kamor pišemo, če misliš uporabljat spremeni končnico, da si ne brišemo datoteke
    x9e, x9a -> ž, š
    x8e, x8a -> Ž, Š
'''
txtPathFile="../podatki/Osnovne_sole_brez_enot_OSPP.txt"
txtPathWrite="../customdata/osnovne_sole_brez_enot_proper_pp.txt"
f=open(txtPathFile, 'r', encoding = "ISO-8859-1")
w=open(txtPathWrite, 'w')
for vrstica in f:
    magic=(repr(vrstica).replace(" - ","").replace("è","č")
          .replace("x9e", "ž").replace("x9a", "š").replace("x8a", "Š").replace("È", "Č").
           replace("x8e", "Ž"))
    w.write(str(magic).replace("\\","")[0:-2]+"\n")

w.close()
f.close()