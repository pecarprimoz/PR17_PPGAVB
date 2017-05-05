
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

##### Porazdelitev otrok glede na šolo
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
