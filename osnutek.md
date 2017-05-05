# Tema
S skupino bomo uporabljali podatkovno množico Ministrstva za izobraževanje, znanost in šport. Delali bomo statistično analizo na področju osnovnošolskih dejavnosti.

# Problem
Poskušali bomo ugotoviti, kakšni so trenutni trendi v osnovnih šolah, bolj specifično razliko med tem kako je bilo včasih in kako je danes. Povdarek bo na specifičnih regijah in dejavnostih osnovnošolcev. 

# Vprašanja, cilji, opis problema
Ker imamo veliko različnih podatkov in tudi vpogled v zgodovino, se bomo v to nalogo usmerili bolj splošno. 

Specifični problemi so (naprimer) sledeči:
 * Koliko otrok obiskuje podaljšano bivanje po specifičnih regijah, kako je bilo včasih...
 * Kateri izbirni predmeti so bolj popularni in kateri manj
 * Izbira neobveznih izbirnih predmetov
 * Kateri tuji jeziki prevladujejo, koliko otrok hodi v glasbene šole...

Na voljo imamo tudi podatke za 10 let nazaj, zato bo eden od ciljev ugotoviti, kako je bilo npr. 10 let nazaj v primerjavi z danes.

Na koncu bi lahko izdelali aplikacijo, ki bi prikazovala trende za specifične regije po Sloveniji in tudi možnost za vpogled po letih.

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
