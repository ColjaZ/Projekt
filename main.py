import pobiranje_podatkov

od = 1
while True:
    do = input("How many pages per category would you like to analyse? Type in a number: ")
    if not do.isnumeric():
        print("try again")
    else:
        do = int(do)
        break

print("getiing the data ready")
pobiranje_podatkov.poberi_htmlje(od, do)
pobiranje_podatkov.shrani_csv(od, do)