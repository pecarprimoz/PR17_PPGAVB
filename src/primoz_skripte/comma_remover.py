
import re
strn = "765,'Osnovna šola Cirkulane - Zavrč, Podružnica Zavrč','Srečanja s kulturami in načini življenja /i/',1537,3803,1,0,7,1,1"

p = re.compile(r'(?<=[a-zA-Z]),(?=[a-zA-Z\s])')
result = p.sub("", strn)
nf= open("../txts/sifrat_txt_new.txt",'w')
with open("../txts/Sifrant_txt.txt", encoding="utf-8") as file:
    for i in file:
        if "Zavrč," in i:
            i=i.replace('Osnovna šola Cirkulane - Zavrč, Podružnica Zavrč','Osnovna šola Cirkulane - Zavrč Podružnica Zavrč')
        nf.write(p.sub("",i))

nf.close()
file.close()