import requests
import time
from Preberi_podatke import vzorec_bloka, izloci_podatke_vprasanja
import csv

def poberi_htmlje_st_strani(od, do):
    # for i in range(od, do + 1):
    #     link = f"https://math.stackexchange.com/questions?tab=votes&page={i}"
    #     odziv = requests.get(link)

    #     time.sleep(2)

    #     if odziv.status_code == 200:
    #         with open(f"(highest-score)-stran-{i}.html", "w", encoding="utf-8") as f:
    #             f.write(odziv.text)
    #             print(f"(highest-score)-stran-{i}.html")
    #     else:
    #         print("napaka")

    # for i in range(od, do + 1):
    #     link = f"https://math.stackexchange.com/questions?tab=trending&page={i}"
    #     odziv = requests.get(link)

    #     time.sleep(2)

    #     if odziv.status_code == 200:
    #         with open(f"(trending)-stran-{i}.html", "w", encoding="utf-8") as f:
    #             f.write(odziv.text)
    #             print(f"(trending)-stran-{i}.html")
    #     else:
    #         print("napaka")


    # for i in range(od, do + 1):
    #     link = f"https://math.stackexchange.com/unanswered/tagged/?page={i}&tab=votes&pagesize=50"
    #     odziv = requests.get(link)

    #     time.sleep(2)

    #     if odziv.status_code == 200:
    #         with open(f"(unanswered)-stran-{i}.html", "w", encoding="utf-8") as f:
    #             f.write(odziv.text)
    #             print(f"(unanswered)-stran-{i}.html")
    #     else:
    #         print("napaka")
    for i in range(od, do + 1):
        link = f"https://math.stackexchange.com/questions?tab=newest&page={i}"
        odziv = requests.get(link)

        time.sleep(4)

        if odziv.status_code == 200:
            with open(f"(newest)-stran-{i}.html", "w", encoding="utf-8") as f:
                f.write(odziv.text)
                print(f"(newest)-stran-{i}.html")
        else:
            print("napaka")
    

    vprasanja = []
    # for type in ["highest-score", "trending","unanswered"]:
    for type in ["newest"]:
        for i in range(od, do + 1):
            with open(f"({type})-stran-{i}.html", encoding="utf-8") as f:
                vsebina = f.read()

            bloki = vzorec_bloka.split(vsebina)[1:] #splita in odstrani vse pred prvim vprasanjem
            for blok in bloki:
                vprasanje = izloci_podatke_vprasanja(blok)
                vprasanje["kategorija"] = type
                vprasanja.append(vprasanje)

    avtorji = {}
    oznake = set()
    oznake_vprasanja = []
    with open("vprasanja.csv", "w", encoding="utf-8") as f:
        pisatelj = csv.writer(f)
        pisatelj.writerow(["Kategorija", "id", "Naslov", "Ogledi", "Glasovi", "Število odgovorov", "Ima sprejet odgovor", "Avtor", "Čas objave"])
        for vprasanje in vprasanja:
            kategorija = vprasanje["kategorija"]
            id = vprasanje["id"]
            title = vprasanje["title"]
            views = vprasanje["views"]
            votes = vprasanje["votes"]
            answers = vprasanje["answers"]
            accepted_answer = vprasanje["has_accepted_answer"]
            author = vprasanje["author"]
            cas = vprasanje["time"]
            pisatelj.writerow([kategorija,id,title,views,votes,answers,accepted_answer,author,cas])
            if vprasanje.get("author") is not None:
                avtorji[vprasanje["author"]] = vprasanje.get("reputation", 0)
            for oznaka in vprasanje["tags"]:
                oznake.add(oznaka)
                oznake_vprasanja.append((vprasanje["id"], oznaka))

    with open("avtorji.csv", "w", encoding="utf-8") as f:
        pisatelj = csv.writer(f)
        pisatelj.writerow(["author", "reputation"])
        for author, rep in avtorji.items():
            pisatelj.writerow([author, rep])

    with open("oznake.csv", "w", encoding="utf-8") as f:
        pisatelj = csv.writer(f)
        pisatelj.writerow(["oznaka"])
        for oznaka in oznake:
            pisatelj.writerow([oznaka])

    with open("oznake_vprasanj.csv", "w", encoding="utf-8") as f:
        pisatelj = csv.writer(f)
        pisatelj.writerow(["id", "oznaka"])
        for id, oznaka in oznake_vprasanja:
            pisatelj.writerow([id, oznaka])
    return
poberi_htmlje_st_strani(1,50)