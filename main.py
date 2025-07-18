import pobiranje_podatkov

od = 1
do = 200
imamo_podatke = False
if not imamo_podatke:
    print("Pričenjamo shranjevanje html-jev:")
    pobiranje_podatkov.poberi_htmlje(od, do)
print("Poteka ustvarjanje csv datotek:")
pobiranje_podatkov.shrani_csv(od, do)
print("Končano. Zaženi analizo v Analiza_MSE.ipynb!")