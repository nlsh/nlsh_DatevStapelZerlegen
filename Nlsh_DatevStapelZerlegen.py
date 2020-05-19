#!/usr/bin/env python
"""
Zerlegung eines mehrmonatigem DATEV- Buchungsstapels in einzelne Monate

"""
# Funktion Definieren
def NlshDatevStapelZerlegen ():
    """
    Die Listen in Python sind mir noch ein Rätsel, aus PHP kenne ich mehrdimensionale Arrays und Arrays, welche auch mit Strings indiziert werden können.
    In Python erkenne ich nur Excel- Zeilen und ihr Anprechen über Schleifen und Zahlen... furchtbar
    Darum erst einmal eine Definition einer Liste
    """
    # Definitionen
    def_monate     = [['DummyMonat0', '0001', '0031', [] ],
                      ['Januar',      '0101', '0131', [] ],
                      ['Februar',     '0201', '0229', [] ],
                      ['März',        '0301', '0331', [] ],
                      ['April',       '0401', '0430', [] ],
                      ['Mai',         '0501', '0531', [] ],
                      ['Juni',        '0601', '0630', [] ],
                      ['Juli',        '0701', '0731', [] ],
                      ['August',      '0801', '0831', [] ],
                      ['September',   '0901', '0930', [] ],
                      ['Oktober',     '1001', '1031', [] ],
                      ['November',    '1101', '1130', [] ],
                      ['Dezember' ,   '1201', '1231', [] ]
                     ]
    # TODO: erst einmal noch vollen Pfad im Code, später mal über Konsole beim Aufruf des Programms
    zu_teilender_buchungsstapel = "D:\ATOM-Projekte\Python\Dateien\DTVF_Buchungsstapel_20200508_112756_00002.csv"

    # Und los geht es
    # Module importieren
    import os       # Pfadangabe
    import copy     # Klonen
    import csv      # CSV Dateien

    # Name und Pfad der zur zerlegenden Datei ermitteln
    name_buchungsstapel = os.path.basename(zu_teilender_buchungsstapel)
    pfad_buchungsstapel = os.path.dirname(zu_teilender_buchungsstapel)

    # CSV Datei zeilenweise einlesen
    with open(zu_teilender_buchungsstapel) as csvdatei:
        csv_reader_object = csv.reader(csvdatei, delimiter=';', quotechar = '"')

        zeilennummer = 0
        for row in csv_reader_object:

            # Erste Zeile sichern
            if zeilennummer == 0:
                first_row = (row)

            # Zweite Zeile sichern
            if zeilennummer == 1:
                secend_row = (row)

            # Jetzt Daten einlesen
            if zeilennummer > 1:
                aktuelle_line   = (row)
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
        for i in def_monate[int(zahler_monat)][3]:
            zu_schreiben.append(i)

        # Pfad und Namen der zu schreibenen Dateien erstellen
        name_write_csv_file = pfad_buchungsstapel + '\\' + 'DTVF_' + first_line[11] + '_' + first_line[14] + '_' + first_line[15] + '_' + first_line[16] + '.csv'
        with open(name_write_csv_file, mode='w') as csv_file:
            # Wichtig hier der lineterminator='\n', entfernt ein zusätzliches CR am Zeilenende!!!!!
            csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', lineterminator='\n')

            for row in zu_schreiben:
                csv_writer.writerow(row)

        zahler_monat += 1

# Hauptprogramm, wenn direkt aufgerufen wird
if __name__ == '__main__':
    NlshDatevStapelZerlegen()
