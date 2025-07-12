import requests
import time

for i in range(1,3):
    link = f"https://math.stackexchange.com/questions?tab=votes&page={i}"
    odziv = requests.get(link)

    time.sleep(2)

    if odziv.status_code == 200:
        with open(f"(highest-score)-stran-{i}.html", "w", encoding="utf-8") as f:
            f.write(odziv.text)
    else:
        print("napaka")

for i in range(1,3):
    link = f"https://math.stackexchange.com/questions?tab=trending&page={i}"
    odziv = requests.get(link)

    time.sleep(2)

    if odziv.status_code == 200:
        with open(f"(trending)-stran-{i}.html", "w", encoding="utf-8") as f:
            f.write(odziv.text)
    else:
        print("napaka")


for i in range(1,3):
    link = f"https://math.stackexchange.com/unanswered/tagged/?page={i}&tab=votes&pagesize=50"
    odziv = requests.get(link)

    time.sleep(2)

    if odziv.status_code == 200:
        with open(f"(unanswered)-stran-{i}.html", "w", encoding="utf-8") as f:
            f.write(odziv.text)
    else:
        print("napaka")

from Preberi_podatke import vzorec_bloka, izloci_podatke_vprasanja

vprasanja = []
for i in range(1,3):
    with open(f"(highest-score)-stran-{i}.html", encoding="utf-8") as f:
        vsebina = f.read()

    bloki = vzorec_bloka.split(vsebina)[1:] #splita in odstrani vse pred prvim vprasanjem
    for blok in bloki:
        vprasanje = izloci_podatke_vprasanja(blok)
        vprasanja.append(vprasanje)
print(vprasanja)