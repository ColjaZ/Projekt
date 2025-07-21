import pobiranje_podatkov

od = 1
do = 200
poberi_podatke = input("Ali želite pobrati sveže podatke (trajanje: 45 min)? Odgovorite z da/ne: ")
if poberi_podatke.lower() != "da":
    imamo_podatke = True
else:
    imamo_podatke = False

if not imamo_podatke:
    print("Pričenjamo shranjevanje html-jev:")
    pobiranje_podatkov.poberi_htmlje(od, do)
    print("Poteka ustvarjanje csv datotek:")
    pobiranje_podatkov.shrani_csv(od, do)
    print("Končano. Zaženi analizo v Analiza_MSE.ipynb!")
else:
    print("Zaženi analizo v Analiza_MSE.ipynb!")