# ver1
# tantagyFelosztas=[]
# with open("beosztas.txt", "r", encoding="UTF-8") as fin:
#     for sor in fin:
#         tantagyFelosztas.append(sor.strip())

# for elem in tantagyFelosztas:
#     print(f"{elem},")
# print(f"A listában {int(len(tantagyFelosztas)/4)} elem van.")

# ver2
tanarok=[]
tantargyak=[]
osztalyok=[]
oraszamok=[]

rekord=[]

with open("beosztas.txt", "r", encoding="UTF-8") as fin:
    for sor in fin:
        rekord.append(sor.strip())
        if len(rekord)==4:
            tanarok.append(rekord[0])
            tantargyak.append(rekord[1])
            osztalyok.append(rekord[2])
            oraszamok.append(int(rekord[3]))

            rekord=[]

for i in range(len(tanarok)):
    print(f"{tanarok[i]}, {tantargyak[i]}, {osztalyok[i]}, {oraszamok[i]}")
print("2. feladat")
print(f"A fájlban {len(tantargyak)}  bejegyzés van.")
print("3. feladat")
print(f"Az iskolában a heti összóraszám: {sum(oraszamok)}.")
print("4. feladat")
def osszegzes(beTanar, tanarok, oraszamok):
    osszOraszam=0
    for i in range(len(tanarok)):
        if tanarok[i]==beTanar:
            osszOraszam+=oraszamok[i]
    return osszOraszam
beTanar=input("Kérem egy tanár nevét: ")
print(f"Heti összóraszám: {osszegzes(beTanar, tanarok, oraszamok)}")
print("6. feladat")
def eldontes(beOsztaly, beTantargy, tantargyak, osztalyok):
    i=0
    while i<len(tantargyak) and not(beTantargy==tantargyak[i] and beOsztaly.split(".")[0]==osztalyok[i].split(".")[0] and "x" in osztalyok[i]): 
        i+=1
    return i>len(tantargyak)
beOsztaly=input("Kérek egy osztályt: ")
beTantargy=input("Kérek egy tantágyot: ")
if eldontes(beOsztaly, beTantargy, tantargyak, osztalyok):
    print("Csoportbontásban tanulják.")
else:
    print("Nem csoportbontásban tanulják.")
print("7. feladat")
def megszamol(tanarok):
    tanarokEgyedi=[]
    for tanar in tanarok:
        if tanar not in tanarokEgyedi:
            tanarokEgyedi.append(tanar)
    return len(tanarokEgyedi)
print(f"Az iskolában {megszamol(tanarok)} tanár tanít.")
print("Házi feladat")
def kiszuro(tantargyak):
    tantargyakEgyedi=[]
    for tantargy in tantargyak:
        if tantargy not in tantargyakEgyedi:
            tantargyakEgyedi.append(tantargy)
    return tantargyakEgyedi
with open("tantargyak", "w", encoding="UTF-8") as cf:
    for sor in kiszuro(tantargyak):
        cf.write(sor + "\n")