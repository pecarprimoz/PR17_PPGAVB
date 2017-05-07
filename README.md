
# Primož
Vprašanja, ki smo si jih zastavili so bila preveč optimistična.

#### Popravil podatke
Podatke, ki smo dobili v originalnem stanju, so imele težave s šumniki (encodano v windows-1250, namest utf-8), tako da sem napisal parser za to, kasneje smo ugotovili, da je potrebno v excelu shraniti v pravilnem encodingu.

Vse datoteke so imele "," za delimiter, kar je problem je to, da podatki sami v sebi uporabljajo vejice v npr. imenah šole, spisal skripto, ki reši ta problem.

```python
p = re.compile(r'(?<=[a-zA-Z]),(?=[a-zA-Z\s])')
```

In še zadnja stvar, podatki niso popolni, nekaj jih je izpolnjenih čisto nesmiselno, kdorkoli je dodajal v bazo, je enkrat uporabljal ID-je, ki se navezujejo na določen podatek, enkrat pa je vnesel kar normalno (v oddelkih so šifre za leta, nekaj tisoč vrednosti je imeno namesto IDja kar z besedami napisano 12-> 1. razred, kar se je pa poznalo v analizi). Take podatke, če se je le dalo sem ročno popravil.

#### Izdelal skripte za analzio
Naredil sem nekaj preprostih skrip za samo parsanje datotek, npr. za oddelke pobere le vrednosti o letu, oddelku, učencih, učenkah in romih, tako sem zbil iz 2.852.050 na 428.820 celic, posledično hitrejše izvajanje skript in nasploh delovanje v Orange3. Izdelal skripte, za izdelavo novih excel datotek z podatki, ki so me zanimali.

##### Število otrok na šolo za 10 let
Pobral vse možne šole in seštel koliko otrok hodi na določeno šolo. Tako sem dobil porazdelitev za število otrok vseh slovenskih šol. V primeru, da ne uporabimo histograma, dobimo normalno porazdelitev.
![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/hist_otroci.png?raw=true "Porazdelitev otrok v histogramu.")

##### Clustering na predmetih
Naredil sem hierarhičen clustering na vseh predmetih. Rezultati so bli ne preveč dobri, sicer je v isti cluster dal izbirne športe.
![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/clustering_predmeti.png?raw=true "Hierarhičen clustering na predmetih.")

##### Porazdelitev otrok glede na razred
Pobral sem podatke za vse otroke, jih razdelil v 3 skupine in pogledal porazdelitve za sledeče 3 skupine.
![alt text](https://raw.githubusercontent.com/pecarprimoz/PR17_PPGAVB/master/slikice/ucenci_na_leto.png "Porazdelitev učencov, glede na leto.")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/ucenke_na_leto.png?raw=true "Porazdelitev učenk, glede na leto.")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/romi_na_leto.png?raw=true "Porazdelitev romov, glede na leto.")

##### Število otrok na oddelek
Vzel sem vse informacije o oddelkih, o letih in številu otrok na oddelek, to pa sem predstavil v škatli z brki.
![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/oddelki_ucenci.png?raw=true "Št. otrok, na oddelek, na leto.")

##### Scatter ploti
Izdelal sem še dva scatter plotta, kako so učenci in učenke zastopani glede na letnik, tukaj, kot pričakovano smo imeli neko veliko gručo, katere so bile obe zastopane enako, kar pa je zanimivo pa je scatter plot med učenci in romi, v tem scatter plottu pa so romi veliko manj zastopani, ko se bolj nagibamo višjim razredom (št. romov pada od 1. razreda do 9. po ~1000 na razred)


![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/scatter_ucenkeXucenci_po_razredih.png?raw=true "Scatter plot, učenci in učenke")

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/scatter_ucenciXromi_po_razredih.png?raw=true "Scatter plot, učenci in romi")

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

Ko pogledamo številke po šolah, dobimo sledečih 5 šol z največnim številom:

![alt text](https://github.com/pecarprimoz/PR17_PPGAVB/blob/master/slikice/st_otrok_izob_top5.png?raw=true "Število otrok po šolah")

Na vrhu je prepričljivo osnovna šola Livada v kateri je vpisanih približno 90% otrok, ki niso iz slovenskih družin. Tako je nekako pričakovano, da se veliko takih družin odloči za šolanje doma. Velik vpliv ima seveda tudi to, da je to najbližja šola azilnemu domu na Viču.
Predpostavljam, da je podobno z OŠ Trnovo saj je precej blizu OŠ Livada.
