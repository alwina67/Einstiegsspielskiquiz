import random

fragen_liste = [
    {
        "frage": "Was ist der höchste Punkt im Skigebiet Großglockner-Heiligenblut?",
        "Optionen": ["a) 2.902m", "b) 3.207m", "c) 2.864m", "d) 2.912m"],
        "Antwort": "a",
        "ID" : "1"

    },
    {
        "frage": "Wie lang ist die schwarze Piste im Skigebiet Großglockner-Heiligenblut?",
        "Optionen": ["a) 5km", "b) 10km", "c) 1km", "d) 3km"],
        "Antwort": "c",
        "ID" : "2"
    },
    {
        "frage": "Wie viele Lifte hat das Skigebiet Hochkönig?",
        "Optionen": ["a) 30", "b) 34", "c) 56", "d) 22"],
        "Antwort": "b",
        "ID" : "3"
    },
    {
        "frage": "Wie viele Schlepplifte hat das Skigebiet Hochkönig?",
        "Optionen": ["a) 3", "b) 11", "c) 19", "d) 26"],
        "Antwort": "c",
        "ID" : "4"
    },
    {
        "frage": "Wie lang ist die rote Piste im Skigebiet Hochkönig?",
        "Optionen": ["a) 23km", "b) 41km", "c) 1km", "d) 19km"],
        "Antwort": "b",
        "ID" : "5"
    },
    {
        "frage": "Für wen ist das Skigebiet Hochkönig das ideale Winterurlaubsziel?",
        "Optionen": ["a) für Erwachsene", "b) für Familien", "c) für Jugendliche", "d) für Einzelgänger"],
        "Antwort": "b",
        "ID" : "6"
    },
    {
        "frage": "Wie viele Zauberteppiche hat das Skigebiet SkiWelt Wilder Kaiser-Brixental?",
        "Optionen": ["a) 20", "b) 11", "c) 9", "d) 2"],
        "Antwort": "b",
        "ID" : "7"
    },
    {
        "frage": "Auf welcher Höhe liegt das Skigebiet Abtenau?",
        "Optionen": ["a) 230m", "b) 470m", "c) 670m", "d) 714m"],
        "Antwort": "d",
        "ID" : "8"
    },
    {
        "frage": "Was gibt es leider nicht im Skigebiet Karkogel-Abtenau?",
        "Optionen": ["a) Snowpark", "b) Pferdeschlittenfahrten", "c) Eisstockschießen", "d) Rodelbahn"],
        "Antwort": "a",
        "ID" : "9"
    },
    {
        "frage": "In welchem Land liegt das Skigebiet Ski Arlberg?",
        "Optionen": ["a) Österreich", "b) Frankreich", "c) Italien", "d) Deutschland"],
        "Antwort": "a",
        "ID" : "10"
    },
    {
        "frage": "Wie viele Kabinenbahnen gibt es im Skigebiet Berchtesgaden?",
        "Optionen": ["a) 2", "b) 6", "c) 13", "d) 7"],
        "Antwort": "a",
        "ID" : "11"
    },
    {
        "frage": "Was ist der tiefste Punkt im Skigebiet Berchtesgaden?",
        "Optionen": ["a) 699m", "b) 789m", "c) 803m", "d) 795m"],
        "Antwort": "d",
        "ID" : "12"
    },
    {
        "frage": "Von wann bis wann sind die Pisten im Skigebiet Hochkössen befahrbar?",
        "Optionen": ["a) von Mitte Dezember bis Anfang April", "b) das ganze Jahr", "c) nur im Sommer", "d) nur im Winter"],
        "Antwort": "a",
        "ID" : "13"
    },
    {
        "frage": "Auf welcher Höhe liegt das Skigebiet Hochkössen?",
        "Optionen": ["a) 600m", "b) 570m", "c) 870m", "d) 658m"],
        "Antwort": "d",
        "ID" : "14"
    },
    {
        "frage": "In welchem Land liegt das Skigebiet Galibier Thabor?",
        "Optionen": ["a) Deutschland", "b) Frankreich", "c) Österreich", "d) Schweiz"],
        "Antwort": "b",
        "ID" : "15"
    },
    {
        "frage": "Wie viele Lifte gibt es im Skigebiet Galibier Thabor insgesamt?",
        "Optionen": ["a) 60", "b) 5", "c) 31", "d) 66"],
        "Antwort": "c",
        "ID" : "16"
    },
    {
        "frage": "Wann waren die Olympischen Winterspiele im Skigebiet Garmisch-Partenkirchen?",
        "Optionen": ["a) 1936", "b) 2018", "c) 1924", "d) 1992"],
        "Antwort": "a",
        "ID" : "17"
    },
    {
        "frage": "Wie ist der Schneezustand im Skigebiet Garmisch-Partenkirchen (Stand 24.04.2026)?",
        "Optionen": ["a) Nassschnee", "b) Pulverschnee", "c) Altschnee", "d) Triebschnee"],
        "Antwort": "a",
        "ID" : "18"
    },
    {
        "frage": "Was ist der höchste Punkt im Skigebiet Paganella Ski?",
        "Optionen": ["a) 2.300m", "b) 3.200m", "c) 2.123m", "d) 2.125m"],
        "Antwort": "d",
        "ID" : "19"
    },
    {   "frage": "In welchem Land liegt das Skigebiet Méribel?",
        "Optionen": ["a) Frankreich", "b) Italien", "c) Schweiz", "d) Österreich"],
        "Antwort": "a",
        "ID" : "20"
    }
    ]  

# ------------------------
# SPIEL START
# ------------------------

name1 = input("Gib deinen Spielernamen ein: ")

modus = input("Alleine oder zu zweit spielen? (alleine/zu zweit): ").lower().strip()

ist_zweier = False

if modus == "zu zweit":
    ist_zweier = True
    name2 = input("Name von Spieler 2: ")
    print("Willkommen " + name1 + " und " + name2 + " beim Skigebiet-Quiz!")
else:
    print("Willkommen " + name1 + " beim Skigebiet-Quiz!")

letzte_punkte = None
nochmal_spielen = "ja"

# ------------------------
# HAUPTSCHLEIFE
# ------------------------

while nochmal_spielen == "ja":

    punkte1 = 0
    punkte2 = 0

    fragen = random.sample(fragen_liste, 10)

    # ------------------------
    # FRAGEN DURCHLAUF
    # ------------------------

    for frage in fragen:
        print("\n" + frage["frage"])

        for option in frage["Optionen"]:
            print(option)

        # Spieler 1
        if not ist_zweier:
            antwort1 = input(name1 + " Antwort (a/b/c/d): ").lower().strip()

            if antwort1 == frage["Antwort"]:
                print("Richtig!")
                punkte1 += 1
            else:
                print("Falsch!")
        

        # Spieler 2
        if ist_zweier:

            antwort1 = input(name1 + " Antwort (a/b/c/d): ").lower().strip()

            if antwort1 == frage["Antwort"]:
                punkte1 += 1
       
            antwort2 = input(name2 + " Antwort (a/b/c/d): ").lower().strip()

            if antwort2 == frage["Antwort"]:
                punkte2 += 1
        print("Die richtige Antwort lautet: ", frage["Antwort"])

        # Zwischenstand
        if ist_zweier:
            
            print(name1 + ": " + str(punkte1) + " | " + name2 + ": " + str(punkte2))
        else:
            print(name1 + ": " + str(punkte1))

    # ------------------------
    # ENDERGEBNIS
    # ------------------------

    print("\n===== ERGEBNIS =====")

    if ist_zweier:
        print(name1 + ": " + str(punkte1))
        print(name2 + ": " + str(punkte2))

        if punkte1 > punkte2:
            print(name1 + " gewinnt!")
        elif punkte2 > punkte1:
            print(name2 + " gewinnt!")
        else:
            print("Unentschieden!")
    else:
        print(name1 + " hat " + str(punkte1) + " Punkte")

        
        # MOTIVATION
        

        if punkte1 == 10:
            print("\nDu scheinst ein richtiger Experte zu sein! Schaffst du das auch ein zweites Mal?")
        elif punkte1== 9:
            print("\nDas war knapp!Schaffst du beim nächsten Mal die volle Punktzahl?")
        elif punkte1== 8:
            print("\nDie zwei Punkte kriegst du noch! Versuch es ein weiteres Mal!")
        elif punkte1 == 7:
            print("\nNur durch erneutes Versuchen kannst du es schaffen!")
        elif punkte1 ==6:
            print("\nBeim nächsten mal klappt es bestimmt!")
        elif punkte1 == 5:
            print("\nSchön mittig! Aber schaffst du die 5 auch mal 2?")
        elif punkte1 == 4:
            print("\nLass deinen Kopf nicht hängen und versuch es erneut!")
        elif punkte1 == 3:
            print("\nBeim nächsten mal schaffst du es bestimmt!")
        elif punkte1 == 2:
            print("\nGlaub an dich und versuche es nochmal!")
        elif punkte1 == 1:
            print("\nZumindest 1 Punkt. Schaffst du aber auch 2?")
        elif punkte1 == 0:
            print("\nMacht nichts, versuch es erneut!")

        # Verbesserung Vergleich
        if letzte_punkte is not None:
            if punkte1 > letzte_punkte:
                print("Besser als letzte Runde!")
            elif punkte1 < letzte_punkte:
                print("Diesmal etwas schlechter.")
            else:
                print("Gleich geblieben!")

        letzte_punkte = punkte1

    # NOCHMAL SPIELEN

    nochmal_spielen = input("\nNochmal spielen? (ja/nein): ").lower().strip()

