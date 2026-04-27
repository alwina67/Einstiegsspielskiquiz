
#Liste an Fragen
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

import random

name = input("Gib deinen Spielernamen ein: ")
print("Hallo " + name +  "! Willkommen beim Skigebiet-Quiz! Dir werden nacheinander 10 Fragen zum Thema Skigebiete gezeigt und du hast 4 Auswahlmöglichkeiten. Bei einer richtigen Anwtort erhältst du einen Punkt")

nochmal_spielen = "ja"
letzte_punkte= None

#Schleife des Spiels

while nochmal_spielen.lower() == "ja":

    punkte = 0
    auswahl = random.sample(fragen_liste, 10)
    
    for fragedict in auswahl:
        print("\n" + fragedict["frage"])

        for option in fragedict["Optionen"]:
            print(option)

        antwort = input("Deine Antwort (a/b/c/d): ").lower()

        if antwort == fragedict["Antwort"]:
            print("Richtig!")
            punkte += 1
        else:
            print("Falsch!")

#Punktzahl und Vergleich mit letzter Runde

    print("\nDu hast", punkte, "von 10 Punkten erreicht!")
    if letzte_punkte is not None:
        if punkte> letzte_punkte:
            print("\nSuper! Du hast dich verbessert!")
        elif punkte<letzte_punkte:
            print("\nSchade, diesmal war es schlechter, versuch es einfach nochmal!")
        else:
            print("\nGleiche Punktzahl wie vorher! Sehr gut!")
    
        
#Motivationsprüche
    if punkte == 10:
        print("\nDu scheinst ein richtiger Experte zu sein! Schaffst du das auch ein zweites Mal?")
    elif punkte== 9:
        print("\nDas war knapp!Schaffst du beim nächsten Mal die volle Punktzahl?")
    elif punkte== 8:
        print("\nDie zwei Punkte kriegst du noch! Versuch es ein weiteres Mal!")
    elif punkte == 7:
        print("\nNur durch erneutes Versuchen kannst du es schaffen!")
    elif punkte ==6:
        print("\nBeim nächsten mal klappt es bestimmt!")
    elif punkte == 5:
        print("\nSchön mittig! Aber schaffst du die 5 auch mal 2?")
    elif punkte == 4:
        print("\nLass deinen Kopf nicht hängen und versuch es erneut!")
    elif punkte == 3:
        print("\nBeim nächsten mal schaffst du es bestimmt!")
    elif punkte == 2:
        print("\nGlaub an dich und versuche es nochmal!")
    elif punkte == 1:
        print("\nZumindest 1 Punkt. Schaffst du aber auch 2?")
    elif punkte == 0:
        print("\nMacht nichts, versuch es erneut!")

    letzte_punkte=punkte

#Nochmal spielen Abfrage

    nochmal_spielen = input("\nMöchtest du nochmal spielen? (ja/nein): ")
    