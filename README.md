# nlsh_DatevStapelZerlegen
 Python - Zerlegung eines mehrmonatigem DATEV- Buchungsstapels in einzelne Monate

Hi, dies ist mein erstes Programm in Python. Bitte nicht gleich verdammen,
ich lerne noch und bin über Vorschläge zur Verbesserung immer interessiert.
Es entstand in dieser Version innerhalb der ersten Stunden des Kennenlernens
dieser Programmiersprache, aus der Not heraus.

Also, dieses Programm wurde geschrieben, da es immer mal wieder vorkommt, dass
man eine Jahresbuchhaltung auf den Tisch geknallt bekommt,  mit den Vorgaben,
diese schnell und ohne großem Aufwand abzubuchen. Meist erledige ich diese
Aufgabe über Buchungsstapel, die über mehrere Monate laufen, einfach um den
lästigem Wechsel der Buchungsstapel zu entgehen.

Dann, aus welchen Gründen auch immer, ist dann auf einmal eine monatliche
Auswertung wichtig.

## Mist, was jetzt?

Naja, wenn man sich mit dem Import- und Export- Funktionen von DATEV
auskennt und auch mit Excel umzugehen weiß, kein Problem, außer die
benötigte Zeit.

Um diese jetzt zu verkürzen, entstand dieses Programm.

## Aufgabe

Aufsplitten eines mehrmonatigem Buchungsstapel in die einzelnen Monate.

**Es wird immer der komplette, exportierte Buchungsstapel von DATEV, ohne
  Löschung einzelner Felder wieder eingespielt, d.h. auch verlinkte, an den
  Buchungssätzen angehängte Dateien, egal, ob aus der Dokumentenverwaltung,
  oder aus Unternehmen- Online, bleiben erhalten!**

## Vorgehensweise

- Sicherung des Mandanten (zur 100% Sicherheit)
- Ausdruck Summen- und Saldenliste zur nachträglichen Kontrolle
- Export des Buchungsstapels aus DATEV- RW in ein separates Verzeichnis
- Aufruf des Programmes (noch in Python, (später als DatevStapelZerlegen.exe)
  siehe Aufruf
- Programm starten und im Ordner des Buchungsstapel werden die neuen
  monatlichen Buchungsstapel abgelegt
- Import der Buchungsstapel über DATEV- RW
- Löschung des originalen Buchungsstapel
- Kontrolle des Endergebnisses über die Summen- und Saldenliste
- hoffentlich nicht: Wiederherstellung der Ausgangssituation durch die
  Sicherung.

## Aufruf

##### Voraussetzung:
Installation von [Python](https://www.python.org/downloads/ "Python") ( bei Windows unbedingt "**Add Python to environment variables**" aktivieren!)
Aufruf in der Konsole:
```console
<Pfad zu>Nlsh_DatevStapelZerlegen.py <Pfad zu >DTVF_xxxx.csv
```
