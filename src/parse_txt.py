txtPathFile="../customdata/Sifrant_txt_pravilno.txt"
f=open(txtPathFile, 'r', encoding = "utf-8")
for i in f:
    print(i)