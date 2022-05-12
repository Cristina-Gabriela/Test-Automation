

baieti = int(input("Scrie cati baieti sunt singuri : "))
fete = int(input("Scrie cate fete sunt singure: "))

if baieti > 0 and fete > 0:
    cupluri_de_facut = input("Vrei sa faci cupluri? ").lower()
    if cupluri_de_facut == "da":
       print("Ok.Am cuplat fete cu baieti.")
    else:
        print("Tine-i izolati !")


# To do: convertire intr-o functie  # intersection()?
# nr de rabbits + nr. de breed
