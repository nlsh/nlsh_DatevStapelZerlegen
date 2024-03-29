#!/usr/bin/env python
"""
Zerlegung eines mehrmonatigem DATEV- Buchungsstapels in einzelne Monats- Buchungsstapel

 * @package   nlsh/nlsh_DatevStapelZerlegen
 * @author    Nils Heinold
 * @copyright Nils Heinold © 2020
 * @link      https://github.com/nlsh/nlsh_DatevStapelZerlegen
 * @license   LGPL-3.0

"""

# Imports
# Module importieren
import argparse
import copy  # Klonen
import csv  # CSV Dateien
import os  # Pfadangabe
import sys  # System ( übergebene Argumente...)
from argparse import ArgumentParser

"""
 " argparse Modul initialisieren und Fehler im Aufruf des Programmes abfangen"
 " Dokumentation von argparse unter https://docs.python.org/3.9/library/argparse.html")
"""


def parser():
    # Parser- Objekt mit Beschreibung der Funktion des Programmes erzeugen
    #  mit epilog='wird nach der Beschreibung desProgrammes Text aufgelistet'
    input_parser: ArgumentParser = argparse.ArgumentParser(
        # Beschreibung, wird als erste Zeile der Erläuterung angezeigt
        description = 'Programmaufruf',

        # den originalen Namen der ausführenden Datei ersetzen
        # prog='ersetzt den originalen Namen der aufgerufenen Datei',

        # Schlusssatz
        epilog = 'Versuchen Sie es bitte erneut.'
    )

    # Definitionen der unbedingt benötigten Parameter in Reihenfolge, ansonsten Fehlerausgabe
    # ohne "-" im String
    input_parser.add_argument('[Pfad/Name]', type = str, help = 'Pfad/Name zur bearbeitenden Datei')

    # Definitionen der obtionalen Parameter
    # mit "-" im String
    # input_parser.add_argument('-OptionalString', type=str,  help="Optionale Parameter als String")

    # Parameter gemäß argParse Modul zurückgeben, wenn alle Bedingungen erfüllt
    return input_parser.parse_args()

# kurze Kontrolle der zu teilenden Datei
def control_input_file(file):
    # Wenn Datei keine CSV- Datei ist
    pfad, filename = os.path.split(file)
    if not (filename.endswith('.csv')):
        sys.exit('Dies ist keine gültige DATEV- Standard Exportdatei .csv- Datei!')
    # Wenn Datei keine DATEV- Standard- Export- Datei ist
    elif not (filename.startswith('DTVF_')):
        sys.exit('Dies ist keine gültige DATEV- Standard Exportdatei DTVF_- Datei!')


# Funktion Definieren
def nlsh_datev_stapel_zerlegen(zu_teilender_buchungsstapel):
    """
    Zerlegt einen über mehrere Monate gebuchten DATEV- Buchungsstapel in
    monatliche Buchungsstapel und speichert diese ab.

    """
    # Definitionen
    def_monate = [['DummyMonat0', '0001', '0031', []],  # Ist das 0. Element, die nächsten dann mit Index als Monat
                  ['Januar',      '0101', '0131', []],
                  ['Februar',     '0201', '0229', []],
                  ['März',        '0301', '0331', []],
                  ['April',       '0401', '0430', []],
                  ['Mai',         '0501', '0531', []],
                  ['Juni',        '0601', '0630', []],
                  ['Juli',        '0701', '0731', []],
                  ['August',      '0801', '0831', []],
                  ['September',   '0901', '0930', []],
                  ['Oktober',     '1001', '1031', []],
                  ['November',    '1101', '1130', []],
                  ['Dezember',    '1201', '1231', []]
                  ]

    # Name und Pfad der zur zerlegenden Datei ermitteln
    # name_buchungsstapel = os.path.basename(zu_teilender_buchungsstapel)
    pfad_buchungsstapel = os.path.dirname(zu_teilender_buchungsstapel)

    # CSV Datei zeilenweise einlesen
    with open(zu_teilender_buchungsstapel) as csvdatei:
        csv_reader_object = csv.reader(csvdatei, delimiter=';', quotechar='"')

        zeilennummer = 0
        for row in csv_reader_object:

            # Erste Zeile sichern
            if zeilennummer == 0:
                first_row = row

            # Zweite Zeile sichern
            if zeilennummer == 1:
                secend_row = row

            # Jetzt Daten einlesen
            if zeilennummer > 1:
                aktuelle_line = row
                """
                Die letzten beiden Ziffern auslesen, kann dreistellig oder vierstellig sein
                Keine Funktion gefunden, die die letzten x Zeichen eines Strings ausgibt,
                nur Löschen ist möglich!
                Datum Länge ermitteln und Bereich auslesen
                """
                strlen = len(aktuelle_line[9])
                if strlen == 3:
                    aktueller_monat = aktuelle_line[9][1:3]
                if strlen == 4:
                    aktueller_monat = aktuelle_line[9][2:4]

                def_monate[int(aktueller_monat)][3].append(aktuelle_line)

            zeilennummer += 1

    # CSV Dateien schreiben
    zahler_monat = 1

    while zahler_monat < 13:
        # Erste Zeile einlesen und ändern
        zu_schreiben = []
        first_line = copy.deepcopy(first_row)
        first_line[14] = first_line[14][0:4] + def_monate[zahler_monat][1]
        first_line[15] = first_line[15][0:4] + def_monate[zahler_monat][2]
        first_line[16] = first_line[16] + ' ' + def_monate[zahler_monat][0]

        # Erste Zeile hinzufügen
        zu_schreiben.append(first_line)

        # Zweite Zeile hinzufügen
        zu_schreiben.append(secend_row)

        # Daten hinzufügen, da Liste, einzeln durchgehen
        daten_vorhanden = False
        for i in def_monate[int(zahler_monat)][3]:
            if i:
                daten_vorhanden = True
                zu_schreiben.append(i)

        # Wenn Daten vorhanden, dann schreiben
        if daten_vorhanden:
            # Pfad und Namen der zu schreibenden Dateien erstellen
            name_write_csv_file = pfad_buchungsstapel + '\\' + 'DTVF_' + first_line[11] + '_' + first_line[14] + '_' + \
                                  first_line[15] + '_' + first_line[16] + '.csv'
            with open(name_write_csv_file, mode='w') as csv_file:
                # Wichtig hier der lineterminator='\n', entfernt ein zusätzliches CR am Zeilenende!!!!!
                csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', lineterminator='\n')

                for row in zu_schreiben:
                    csv_writer.writerow(row)

        zahler_monat += 1


# Hauptprogramm, wenn direkt aufgerufen wird
if __name__ == '__main__':

    # Kontrolle des Aufrufs, ob alle benötigten Parameter korrekt sind
    # es wird das argparse Modul genutzt
    # es werden die einzelnen Parameter als Liste in argParser gespeichert
    argParser = parser()

    # Kontrolle, ob Parameter übergeben wurde; ([0]->Name der Datei; [1]-> 1. Parameter )
    if len(sys.argv) != 2:
        print('Den zu teilenden Buchungsstapel bitte inklusive kompletten Pfad als Parameter angeben!')
    else:
        # Kurze Kontrolle der Übergabe
        control_input_file(sys.argv[1])

        nlsh_datev_stapel_zerlegen(sys.argv[1])
