# Analiza vprašanj na Math StackExchange

Z analizo poskušamo ugotoviti, kako postaviti vprašanje z največjo možnostjo uspeha na spletni strani
Math Stackexchange - analiziramo glavne značilnosti uspešnih vprašanj in jih primerjamo z značilnostmi
neuspešnih vprašanj.

## Opis  
Program pobere in obdela seznam vprašanj s spletne strani Math StackExchange iz treh kategorij:  
- **highest-score** (najvišje ocenjena vprašanja)  
- **trending** (trenutno priljubljena vprašanja)  
- **unanswered** (vprašanja brez sprejetih odgovorov)  

Za vsako vprašanje izlušči: ID, naslov, število ogledov, glasov, odgovorov, ali ima sprejet odgovor, avtorja in njegov ugled, ter oznake.

Preberi_podatke.py s pomočjo regularnih izrazov izlušči informacije za vsako vprašanje in jih shrani v slovar.
pobiranje_podatkov.py shrani HTML-je ter informacije o vprašanjih shrani v csv datoteke.
# Navodila za uporabo
- Zaženite datoteko main.py
- Na vprašanje odgovorite z "da", če želite pobrati sveže podatke. Sicer program analizira že vnaprej pobrane podatke.
- Zaženite datoteko Analiza_MSE.ipynb in začnite analizo
