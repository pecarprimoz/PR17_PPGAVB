#### Opis podatkov

Pri izdelavi seminarske naloge uporabljamo podatke o osnovnih šolah. Podatke smo dobili na Ministerstvu za izobraževanje, znanost in šport. Imamo štiri pomembnejše tabele in sicer tabele z podatki o šolah, oddelkih, izbirnih predmetih in izobraževanju na domu.

#### Popravil podatke
S podatki, ki smo jih dobili v originalnem stanju, smo imeli težave s šumniki (kodirano v windows-1250 namesto v utf-8) tako, da sem napisal parser za to. Kasneje smo ugotovili, da je potrebno v Excelu shraniti v pravilnem kodiranju.

Vse datoteke so imele "," za delimiter. Problem je bil to, da podatki sami v sebi uporabljajo vejice v npr. imenah šole. Spisal sem skripto, ki reši ta problem.

```python
p = re.compile(r'(?<=[a-zA-Z]),(?=[a-zA-Z\s])')
```

In še zadnja stvar, podatki niso popolni, nekaj jih je izpolnjenih čisto nesmiselno, kdorkoli je dodajal v bazo je enkrat uporabljal ID-je, ki se navezujejo na določen podatek, enkrat pa je vnesel kar normalno (v oddelkih so šifre za leta, nekaj tisoč vrednosti je imelo namesto IDja kar z besedami napisano 12-> 1. razred, kar se je poznalo v analizi). Take podatke sem, če se je le dalo, ročno popravil.

#### Izdelal skripte za analizo
Naredil sem nekaj preprostih skript za parsanje datotek, npr. za oddelke pobere le vrednosti o letu, oddelku, učencih, učenkah in romih, tako sem zbil iz 2.852.050 na 428.820 celic, posledično hitrejše izvajanje skript in nasploh delovanje v Orange3. Izdelal sem skripte, za izdelavo novih Excel datotek z podatki, ki so me zanimali.

##### Število otrok na šolo za 10 let
Pobral vse možne šole in seštel koliko otrok hodi na določeno šolo. Tako sem dobil porazdelitev za število otrok vseh slovenskih šol. V primeru, da ne uporabimo histograma, dobimo normalno porazdelitev.
![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/hist_otroci.png?raw=true "Porazdelitev otrok v histogramu.")

##### Gručenje po predmetih
Naredil sem hierarhično gručenje po vseh predmetih. Rezultati niso preveč dobri, sicer je v isti cluster dal izbirne športe.
![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/clustering_predmeti.png?raw=true "Hierarhično gručenje na predmetih.")

##### Porazdelitev otrok glede na razred
Pobral sem podatke za vse otroke, jih razdelil v 3 skupine in pogledal porazdelitve za sledeče 3 skupine.
![alt text](https://raw.githubusercontent.com/pecarprimoz/PR17_PPGAVB/master/slikice/ucenci_na_leto.png "Porazdelitev učencov, glede na leto.")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/ucenke_na_leto.png?raw=true "Porazdelitev učenk glede na leto.")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/romi_na_leto.png?raw=true "Porazdelitev romov glede na leto.")

##### Število otrok na oddelek
Vzel sem vse informacije o oddelkih, o letih in številu otrok na oddelek, to pa sem predstavil v škatli z brki.
![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/oddelki_ucenci.png?raw=true "Št. otrok, na oddelek, na leto.")

##### Scatter ploti
Izdelal sem še dva scatter plota, kako so učenci in učenke zastopani glede na letnik, tukaj, kot pričakovano smo imeli neko veliko gručo, katere so bile obe zastopane enako, kar pa je zanimivo pa je scatter plot med učenci in romi, v tem scatter plottu pa so romi veliko manj zastopani, ko se bolj nagibamo višjim razredom (št. romov pada od 1. razreda do 9. po ~1000 na razred)

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/scatter_ucenkeXucenci_po_razredih.png?raw=true "Scatter plot, učenci in učenke")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/scatter_ucenciXromi_po_razredih.png?raw=true "Scatter plot, učenci in romi")


#### Napoved razreda glede na oddelek, št. učencov, učenk in romov
Za konec pa sem poskušal napovedati, v kateri razred bi spadala določena skupina otrok v nekem oddelku. Še preden sem začel, nisem pričakoval dobrih rezultatov, saj poskušam napovedati leto iz števila otrok in črke oddelka. Poskušal sem nekaj modelov, vendar so bili rezultati sledeči.

| Method                    | AUC    | CA     |  F1     | Precision  | Recall |
| ------------------------- |--------|--------|---------|------------|--------|
| Logistic Regression       | 0.532  | 0.127  |  0.104  | 0.128      | 0.127  |

Kot pričakovano, model je neuporaben, ker nimamo zadosti dobre podatke.

#### Analiza OŠ
Analiziral sem datoteko OŠ.xslx, ki vsebuje osnovne podatke o slovenskih osnovnih šolah (Šifra, Občina, Naslov, Naziv...).
Za boljši občutek o lokacijah šol sem naredil zemljevid vseh šol s pomočjo geolokacije.

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/sole_slo.PNG?raw=true "Lokacije vseh šol")

Naredil sem tudi analizo šol glede na regijo in kasneje tudi glede na območno enoto.

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/st_sol_po_regijah.png?raw=true "Število šol na regijo")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/st_sol_oe.png?raw=true "Število šol na območno enoto")

Največ šol je pričakovano v osrednjeslovenski regiji zaradi največjega števila ljudi. Najmanj šol je v zasavski regiji oziroma v območni enoti Slovenj Gradec, če gledamo območne enote namesto regij.

#### Analiza Izobraževanja da domu
Analiziral sem tudi podatke o izobraževanju na domu. 
Ob analizi podatkov po letih sem ugotovil, da se trend izobraževanja na domu povečuje zadnja leta.

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/st_otrok_izob_hist.png?raw=true "Število otrok, ki se izobražujejo doma (histogram)")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/st_otrok_izob_line.png?raw=true "Število otrok, ki se izobražujejo doma")

Pregledam sem tudi zgodovino, kako se število otrok razporedi po razredih in dobil sledeč histogram.

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/st_otrok_izob_po_razredih.png?raw=true "Število otrok po razredih")

Rezultati so nekako smiselni, saj si lahko predstavljam, da se največ staršev odloči za to potezo na začetku otrokovega šolanja.

Ko pogledamo številke po šolah, dobimo sledečih 5 šol z največjim številom:

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/st_otrok_izob_top5.png?raw=true "Število otrok po šolah")

Na vrhu je prepričljivo osnovna šola Livada v kateri je vpisanih približno 90% otrok, ki niso iz slovenskih družin. Tako je nekako pričakovano, da se veliko takih družin odloči za šolanje doma. Velik vpliv ima seveda tudi to, da je to najbližja šola azilnemu domu na Viču.
Predpostavljam, da je podobno z OŠ Trnovo saj je precej blizu OŠ Livada.

#### Podrobnejša analiza po regijah

Naredil sem analizo po regijah. Opazoval sem število učencev, romov, učencev, ki obiskujejo podaljšano bivanje, učencev z odločbo o usmerjanju. Naračunal sem povprečne vrednosti na oddelek. Prišel sem do zanimive ugotovite, da pomurska regija v veliko primerih odstopa od ostalih regij.

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/regije/st_oddelkov.jpg?raw=true "Število oddelkov po regijah")

Najprej sem izdelal graf, ki prikazuje število oddelkov. Zelo izstopa osrednjeslovenska regija, kar je pričakovano, saj ima glede na zgornje rezultate največ šol in učencev.

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/regije/avg_st_ucencev.jpg?raw=true "Povprečno število učencev v oddelku po regijah")

Pri pregledu povprečnih velikosti oddelkov sem ugotovil, da so vrednosti med 7 in 17, kar je neobičajno za normalen oddlek. Sklepam, da je to zaradi velikega števila podružnic, ki imajo majhne oddelke in tako znižujejo povprečje. Precej izstopa pomurska regija z zelo nizkim povprečjem. Sklepam, da je na tem območju veliko podružnic. Resničnost te hipoteze bomo raziskovali v nadaljevanju.

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/regije/avg_st_romov.jpg?raw=true "Povprečno število romskih otrok v oddelku po regijah")

Naslednja stvar, ki sem jo preučevanjem števila romskih učencev. Povprečno število romov v oddelku se zelo razlikuje med regijami. Najbolj izstopata pomurska in JV Slovenija, kjer so na oddelek povprečno od 3 do 4 romi. Najmanj romskih otrok pa je v gorenjski, goriški, obalno-kraški in notranjsko-kraški regiji, torej v vzhodni Sloveniji, in pa v koroški ter savinjski regiji.

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/regije/avg_st_OPB.jpg?raw=true "Povprečno število otrok v oddelku, ki obiskujejo podaljšano bivanje, po regijah")

Iz podatkov je razvidno, da je več otrok v podaljšanem bivanju iz zahodne slovenije (Gorenjska, Goriška, Osrednjeslovenska in Obalno-Kraška). Obratno pa je na zahodu in jugu slovenije, kjer je manj otrok v podaljšanem bivanju. Spet posebaj izstopa pomurska regija.

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/regije/avg_st_odlocba.jpg?raw=true "Povprečno število otrok z odločbo o usmerjanju po regijah")

Prišel sem do zanimive ugotovitve, da zasavska regija nenavadno odstopa od ostalih regij. Vse ostanle imajo povprečno manj kot enega učeca na oddelek. Zasavska pa kar 1,6.

### Končne ugotovitve

#### Klasifikacijski in regresijski model za napoved regije iz predmetov

Ker smo že do vmesne predstavitve raziskali veliko osnovnih in smiselnih stvari, je bil sedaj izziv narediti nekaj smiselnega z vsem kar smo se naučili dosedaj in z podatki. Med vmesno predstavitvo smo dobili povrate informacije, da se naj usmerimo v bolj specifične probleme. Tako smo se odločili za analizo predmetov, glede na to iz katere regije izhajajo. Ponovno sem izdelal nekaj skript, ki nam omogočajo, da na preprost način poberemo vse potrebne podatke o predmetih, regijah in o učencih, ki obiskujejo te predmete. Ideja je bila taka, da če imamo šole, ki imajo neke specifične predmete (npr. Kleklanje, Madžarščina, Italianščina), ali lahko napovemo, v kateri regiji so šole, ki vsebujejo te predmete.

```python
regresija_podatki=defaultdict(lambda : defaultdict(int))

for i in range(2,77478):
    sola = sr["A" + str(i)].value
    predmet = sr["B"+str(i)].value
    vsi_predmeti.add(predmet)
    if predmet not in katere_predmete_sola[sola]:
        katere_predmete_sola[sola].append(predmet)
        temp_dict=defaultdict(int)
        regresija_podatki[sola][predmet]=sr["F"+str(i)].value
```

Sledeča zanka iterira čez vse celice (od 2 do 77478), in pobira imena šol in predmetov, predmete dodamo v množico, ker jih bomo rabili kot vrednosti stolpca. Slovar katere_predmete_sola[sola], vsebuje vse predmete, ki jih ima določena šola. Nato si za vsako šolo zapomnimo, koliko udeležencov ima posamezen predmet. Tako lahko sestavimo regresijski model, kjer so stolpci imena predmetov, vrstice šole v določeni regiji, vrednosti v matriki predmetov*šol pa je število otrok, ki obiskuje ta predmet, v šoli, ki spada pod določeno regijo. Načeloma bi lahko poslušal napovedovati šole, vendar je to pretežak problem, s tako množico podatkov. Pri klasifikaciji, pa je bila vrednost 1 če ima šola ta predmet, sicer pa 0.

#### Klasifikacijski model

Model sem testiral z različnimi metodami in dosegel sledeče rezultate.

| Method                    | AUC    | CA     |  F1     | Precision  | Recall |
| ------------------------- |--------|--------|---------|------------|--------|
| Naive Bayes               | 0.749  | 0.232  |  0.226  | 0.282      | 0.232  |
| kNN                       | 0.745  | 0.328  |  0.267  | 0.372      | 0.328  |
| Tree                      | 0.632  | 0.253  |  0.250  | 0.249      | 0.253  |
| Random Forest             | 0.719  | 0.345  |  0.246  | 0.261      | 0.345  |

Presenetljivo je model dokaj dober, v primerjavi z prvim, ki sem ga naredil za regresijo in dosegel CA 0.1, imamo tuka z knn in naključnimi gozdovi klasifikacijsko točnost 0.328, 0.348, sicer ni spet nevem kaj osupljivo, vendar tako vidimo, da je neka povezava med regijam in predmeti, kar pa je bil namen modela. Na spodnji sliki pa lahko vidimo kako sta poskušala ugotoviti predmete Bayes in nakčjučni gozd, model je bil testiran z metodo Leave one out, kjer smo imeli razmerje učne/tesne 70/30.

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/klas/bayes_predicted.png?raw=true "Napovedi Bayesa")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/klas/forest_predicted.png?raw=true "Napovedi Gozda")

#### Regresijski model

Model sem testiral z različnimi metodami in dosegel sledeče rezultate.

| Method                    | AUC    | CA     |  F1     | Precision  | Recall |
| ------------------------- |--------|--------|---------|------------|--------|
| Logistic Regression       | 0.742  | 0.345  |  0.308  | 0.304      | 0.345  |
| AdaBoost                  | 0.589  | 0.272  |  0.277  | 0.283      | 0.272  |
| Naive Bayes               | 0.716  | 0.121  |  0.125  | 0.429      | 0.121  |

Tukaj sem pa poskušal napovedat regijo, na podlagi tega, koliko otrok obiskuje določen predmet. Tudi tukaj imam boljše rezultate od zadnjič, z logično regresijo dosežem klasifikacijsko točnost 0.345, čisto iz fore sem poskusil še Bayesa, ki brez presenečenj, ni imel preveč dobre točnosti. Spodnja slika prikazuje kako je logična regresija napovedovala predmete. Tukaj se mi je zdelo zanimivo, da čisto ignorira zasavsko regijo, tako sem pogledal ROC krivuljo, ki je dokaj slaba, nasproti s savinjsko, ki ima bolj smiselno obliko

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/regresija/regr_log_reg.png?raw=true "Napovedi Logične regresije")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/regresija/zasavska_roc.png?raw=true "Zasavsa ROC krivulja")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/regresija/savinjsa_roc.png?raw=true "Savinjska ROC krivulja")

#### Predmeti in šole

Ker sem imel že pripravljene podatke, sem pogledal kako so zastopani določeni predmeti v vseh šolah v Sloveniji. Hipoteza je bila sledeča, nenavadni predmeti kot so kleklanje in Italianščina so specifični za določene regije, predmeti kot Šport za sprostitev pa so prisotni v skoraj vseh šolah. Spodnja slika predstavlja, šole v specifični regiji, in ali ima predmet ali ne. Zastavljena hipoteza je bila potrjena.

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/klas/kleklanje_regija.png?raw=true "Zastopanje kleklanja")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/klas/ital_regija.png?raw=true "Zastopanje Italianščine")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/klas/šport_zdravje_pravoslavje.png?raw=true "Zastopanje Športa za sprostitev")

#### Predmeti in šole glede na udeležbo

Iz regresije sem še izdelal scatterplot-e, ki predstavljajo število otrok, za določen predmet. Enako kot zgoraj sem gledal za kleklanje, Italianščino in šport za zdravje. Scatter plotti predstavljajo št. otrok, ki obiskuje določen predmet, glede na regijo.

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/regresija/kleklanje_udelezba.png?raw=true "Št. otrok kleklanje")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/regresija/ital_udelezba.png?raw=true "Št. otrok Italianščina")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/regresija/šport_zdravje_udelezba.png?raw=true "Št. otrok šport")

Na koncu pa me je še zanimalo, kako je pri udeležbi pri dveh zelo znanih/popularnih predmetih, ali je stvar približno enaka, ali je kakšen favorit. Tako sem pogledal, udeležbo med športom za zdravje in športom za sprostitev.

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/regresija/zdravje_vs_sprostitev.png?raw=true "Št. otrok Zdravje vs Sprostitev")

