def readTranzitii(f):
    numarTranzitii = int(f.readline())
    tranzitii = {}

    for i in range(numarTranzitii):
        n = f.readline().split()
        n[0], n[2] = int(n[0]), int(n[2])

        if n[0] not in tranzitii:
            tranzitii[n[0]] = {n[1]: n[2]}
        else:
            tranzitii[n[0]][n[1]] = n[2]

    return tranzitii


def parentRemForOr(expresie):
    paranteze = 0
    switch = 0
    for carac in expresie:
        if carac == "(":
            paranteze += 1
        elif carac == ")":
            paranteze -= 1

        if paranteze != 0 and switch == 0:
            switch = 1
        elif paranteze == 0 and switch == 1:
            switch = -1

    if switch == 1:
        expresie = expresie.lstrip("(").rstrip(")")

    return expresie


def simplificareTranzitii(stare):
    if stare in tranzitii:
        outgoingPairs = {}
        for x in tranzitii[stare].items():
            if x[1] in outgoingPairs:
                outgoingPairs[x[1]].append(x[0])
            else:
                outgoingPairs[x[1]] = [x[0]]

        # cautam sagetile cu mai multe simboluri pe ele si le "|"
        for x in outgoingPairs.items():
            if len(x[1]) > 1:
                xx = list(set(x[1]))
                newState = parentRemForOr(xx[0])
                for y in range(1, len(xx)):
                    newState += "|" + parentRemForOr(xx[y])
                newState = "(" + newState + ")"
                for y in xx:
                    del tranzitii[stare][y]

                tranzitii[stare][newState] = x[0]

# ===========================================================


with open("complement.txt") as f:
    f.readline()
    stari = [int(x) for x in f.readline().split()]

    f.readline()
    litere = f.readline().split()

    stareInitiala = int(f.readline())
    f.readline()
    stariFinale = [int(x) for x in f.readline().split()]

    tranzitii = readTranzitii(f)

change = 0
inStari = {}
while change == 0:

    inStari = {}
    for stare in stari:
        inStari[stare] = 0
    change = 1

    for i in tranzitii.items():
        for j in i[1].values():
            if inStari[j] == 0 and j != i[0]:
                inStari[j] = 1

    for x in inStari.items():
        if x[1] == 0 and x[0] != stareInitiala:
            change = 0
            stari.remove(x[0])
            if x[0] in tranzitii:
                del tranzitii[x[0]]
            if x[0] in stariFinale:
                stariFinale.remove(x[0])

toBeSkipped = []
for stare in stari:
    if stare not in stariFinale and stare not in tranzitii:
        toBeSkipped.append(stare)
        stari.remove(stare)

for stare in stari:
    simplificareTranzitii(stare)

# Adaug mereu stare initiala si finala noua pt simplificare
x = 0
while x in stari:
    x += 1

stari.append(x)
tranzitii[x] = {".": stareInitiala}
stareInitiala = x

while x in stari:
    x += 1
stareFinala = x

stari.append(stareFinala)
for x in stariFinale:
    if x in tranzitii:
        tranzitii[x]["."] = stareFinala
    else:
        tranzitii[x] = {".": stareFinala}

del stariFinale

# Sterg pe rand starile neinitiale si nefinale
for stare in stari:
    if stare == stareInitiala or stare == stareFinala:
        continue

    into = []
    toStar = []
    inCaseOfStar = ""
    for item in tranzitii.items():
        if item[0] in toBeSkipped and item[0] == stare:
            continue

        for tranzitie in item[1].items():
            if tranzitie[1] in toBeSkipped:
                continue

            if tranzitie[1] == stare:
                into.append((tranzitie[0], item[0]))
                if item[0] == stare:
                    toStar.append(tranzitie[0])

    toBeSkipped.append(stare)

    if toStar:
        for ele in toStar:
            ele1 = parentRemForOr(ele)
            inCaseOfStar += "|"+ele1
        if len(toStar) == 1 and len(toStar[0]) == 1:
            inCaseOfStar = inCaseOfStar[1:] + "*"
        else:
            paranteze = 0
            switch = 0
            for carac in inCaseOfStar:
                if carac == "(":
                    paranteze += 1
                elif carac == ")":
                    paranteze -= 1

                if paranteze != 0 and switch == 0:
                    switch = 1
                elif paranteze == 0 and switch == 1:
                    switch = -1

            if switch == -1 or switch == 0:
                inCaseOfStar = "("+inCaseOfStar[1:]+")*"
            else:
                inCaseOfStar += "*"


    for ele in into:
        if ele[1] in toBeSkipped:
            continue

        for tranzitie in tranzitii[stare].items():
            if tranzitie[1] in toBeSkipped:
                continue
            tranzitii[ele[1]][ele[0]+inCaseOfStar+tranzitie[0]] = tranzitie[1]

    del tranzitii[stare]

simplificareTranzitii(stareInitiala)
rezultat = "Not"

for x in tranzitii[stareInitiala].items():
    if x[1] == stareFinala:
        rezultat = x[0]
        break

rezultat = rezultat.replace("..", ",")
rezultat = rezultat.replace(".", "")
rezultat = rezultat.replace(",", ".")

print(rezultat)
