
import re
strn = "281,'Center za usposabljanje, vzgojo in izobraževanje Janeza Levca Ljubljana','Računalništvo (v OŠPP) /i/',1877,3813,1,1,13,2,3"

p = re.compile(r'(?<=[a-zA-Z]),(?=[a-zA-Z\s])')
result = p.sub("", strn)
nf= open("../txts/correcttxt.txt",'w')
with open("../podatki/Izbircitxt.txt", encoding="utf-8") as file:
    for i in file:
        nf.write(p.sub("",i))

nf.close()
file.close()