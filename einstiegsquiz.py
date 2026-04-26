

fragen_liste = [
    {
        "frage": "Was ist der höchste Punkt im Skigebiet Großglockner-Heiligenblut?",
        "Optionen": ["a) 2.902m", "b) 3.207m", "c) 2.864m", "d) 2.912m"],
        "Antwort": "a"
    },
    {
        "frage": "Wie lang ist die schwarze Piste im Skigebiet Großglockner-Heiligenblut?",
        "Optionen": ["a) 5km", "b) 10km", "c) 1km", "d) 3km"],
        "Antwort": "c"
    },
    {
        "frage": "Wie viele Lifte hat das Skigebiet Hochkönig?",
        "Optionen": ["a) 30", "b) 34", "c) 56", "d) 22"],
        "Antwort": "b"
    },
    {
        "frage": "Wie viele Schlepplifte hat das Skigebiet Hochkönig?",
        "Optionen": ["a) 3", "b) 11", "c) 19", "d) 26"],
        "Antwort": "c"
    },
    {
        "frage": "Wie lang ist die rote Piste im Skigebiet Hochkönig?",
        "Optionen": ["a) 23km", "b) 41km", "c) 1km", "d) 19km"],
        "Antwort": "b"
    },
    {
        "frage": "Für wen ist das Skigebiet Hochkönig das ideale Winterurlaubsziel?",
        "Optionen": ["a) für Erwachsene", "b) für Familien", "c) für Jugendliche", "d) für Einzelgänger"],
        "Antwort": "b"
    },
    {
        "frage": "Wie viele Zauberteppiche hat das Skigebiet SkiWelt Wilder Kaiser-Brixental?",
        "Optionen": ["a) 20", "b) 11", "c) 9", "d) 2"],
        "Antwort": "b"
    },
    {
        "frage": "Auf welcher Höhe liegt das Skigebiet Abtenau?",
        "Optionen": ["a) 230m", "b) 470m", "c) 670m", "d) 714m"],
        "Antwort": "d"
    },
    {
        "frage": "Was gibt es leider nicht im Skigebiet Karkogel-Abtenau?",
        "Optionen": ["a) Snowpark", "b) Pferdeschlittenfahrten", "c) Eisstockschießen", "d) Rodelbahn"],
        "Antwort": "a"
    },
    {
        "frage": "In welchem Land liegt das Skigebiet Ski Arlberg?",
        "Optionen": ["a) Österreich", "b) Frankreich", "c) Italien", "d) Deutschland"],
        "Antwort": "a"
    },
    {
        "frage": "Wie viele Kabinenbahnen gibt es im Skigebiet Berchtesgaden?",
        "Optionen": ["a) 2", "b) 6", "c) 13", "d) 7"],
        "Antwort": "a"
    },
    {
        "frage": "Was ist der tiefste Punkt im Skigebiet Berchtesgaden?",
        "Optionen": ["a) 699m", "b) 789m", "c) 803m", "d) 795m"],
        "Antwort": "d"
    },
    {
        "frage": "Von wann bis wann sind die Pisten im Skigebiet Hochkössen befahrbar?",
        "Optionen": ["a) von Mitte Dezember bis Anfang April", "b) das ganze Jahr", "c) nur im Sommer", "d) nur im Winter"],
        "Antwort": "a"
    },
    {
        "frage": "Auf welcher Höhe liegt das Skigebiet Hochkössen?",
        "Optionen": ["a) 600m", "b) 570m", "c) 870m", "d) 658m"],
        "Antwort": "d"
    },
    {
        "frage": "In welchem Land liegt das Skigebiet Galibier Thabor?",
        "Optionen": ["a) Deutschland", "b) Frankreich", "c) Österreich", "d) Schweiz"],
        "Antwort": "b"
    },
    {
        "frage": "Wie viele Lifte gibt es im Skigebiet Galibier Thabor insgesamt?",
        "Optionen": ["a) 60", "b) 5", "c) 31", "d) 66"],
        "Antwort": "c"
    },
    {
        "frage": "Wann waren die Olympischen Winterspiele im Skigebiet Garmisch-Partenkirchen?",
        "Optionen": ["a) 1936", "b) 2018", "c) 1924", "d) 1992"],
        "Antwort": "a"
    },
    {
        "frage": "Wie ist der Schneezustand im Skigebiet Garmisch-Partenkirchen (Stand 24.04.2026)?",
        "Optionen": ["a) Nassschnee", "b) Pulverschnee", "c) Altschnee", "d) Triebschnee"],
        "Antwort": "a"
    },
    {
        "frage": "Was ist der höchste Punkt im Skigebiet Paganella Ski?",
        "Optionen": ["a) 2.300m", "b) 3.200m", "c) 2.123m", "d) 2.125m"],
        "Antwort": "d"
    }
]

import random

name = input("Gib deinen Spielernamen ein: ")
print("Hallo " + name + "! Willkommen beim Skigebiet-Quiz! Dir werden 10 Fragen zum Thema Skigebiete gezeigt und du hast 4 Auswahlmöglichkeiten. Bei einer richtigen Anwtort erhältst du einen Punkt")

nochmal_spielen = "ja"

while nochmal_spielen.lower() == "ja":

    Punkte = 0
    auswahl = random.sample(fragen_liste, 10)

    for fragedict in auswahl:
        print("\n" + fragedict["frage"])

        for option in fragedict["Optionen"]:
            print(option)

        antwort = input("Deine Antwort (a/b/c/d): ").lower()

        if antwort == fragedict["Antwort"]:
            print("Richtig!")
            Punkte += 1
        else:
            print("Falsch!")

    print("\nDu hast", Punkte, "von 10 Punkten erreicht!")
    if Punkte == 10:
        print("Du scheinst ein richtiger Experte zu sein! Schaffst du das auch ein zweites Mal?")
    elif Punkte== 10-1:
        print("Das war knapp!Schaffst du beim nächsten Mal die volle Punktzahl?")
    elif Punkte== 10-2:
        print("Die zwei Punkte kriegst du noch! Versuch es ein weiteres Mal!")
    elif Punkte == 10-3:
        print("Nur durch erneutes Versuchen kannst du es schaffen!")
    elif Punkte ==10-4:
        print("Leider kein Lotto, die 6aus49 hättest du!")
    elif Punkte == 10-5:
        print("Schön mittig! Aber schaffst du die 5 auch mal 2?")
    elif Punkte == 10-6:
        print("")

    nochmal_spielen = input("Möchtest du nochmal spielen? (ja/nein): ")