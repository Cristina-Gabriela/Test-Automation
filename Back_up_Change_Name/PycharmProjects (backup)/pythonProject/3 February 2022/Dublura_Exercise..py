def functii(*politicieni):
    print("Cel mai bun politician va fi: " + politicieni[0])
    print("Cel mai bun politician va fi: " + politicieni[1])
    print("Cel mai bun politician va fi: " + politicieni[2])


functii("Politicianul care da salarii excelente", "Politicianul care da ", "Politicianul care ridica toata comunitatea")


def functii(**europarlamentari):
    print("Europarlamentarul viitorului: " + europarlamentari["definitia_1"])
    print("Europarlamentarul viitorului: " + europarlamentari["definitia_2"])
    print("Europarlamentarul viitorului: " + europarlamentari["definitia_3"])


functii(definitia_1="Care are un salar = cu fiecare om din Europa", definitia_2="Care ridica toata comunitatea", definitia_3="Care da")














