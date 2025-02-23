# Simple-InternetArchive-Downloader

**WICHTIG:**  
Es müssen mindestens "LINKS DATEI", "ZIELORDNER" und "LOGIN DATEI" ausgewählt sein, damit der Download gestartet werden kann!

---

## PROGRAMMVERWENDUNG:

1. Speichern der Seite mit den Downloadlinks im HTML-Format. (Strg+S)
2. Starten des Programmes.
3. Den "Wähle HTML Datei" Button anklicken, um das gespeicherte HTML auszuwählen.
4. "Erstelle Download Links" -> nimmt die HTML-Datei und extrahiert alle Z7-Downloadlinks und speichert sie in einer TXT-Datei.  
    Die Anzahl der gefundenen Links wird angezeigt.
    Diese TXT-Datei wird bei jedem Generieren überschrieben.  
    Nach dem Generieren wird die TXT-Datei automatisch ausgewählt (kann auch manuell mit dem "Wähle Links Datei" ausgewählt werden).
6. Mit dem Button "Wähle Zielordner" wird ausgewählt, wohin die Downloads gespeichert werden.
7. "Erstelle Login Datei" -> öffnet Google Chrome mit der Login-Seite von Internet Archive.  
    Nach abgeschlossenem Login schließt sich die Website automatisch.  
    Es wird eine JSON-Datei mit den Login-Daten anhand der Cookies erstellt.  
    Diese wird automatisch ausgewählt oder kann auch manuell mit dem "Wähle Login Datei" ausgewählt werden.
8. "Start Download" -> öffnet ein weiteres Fenster mit dem Fortschritt inkl. Pause- und Abbruch-Button.

Beim erneuten Öffnen werden die vorhin ausgewählten Dateien gespeichert!

---

## FEATURES:

- Pfade werden gespeichert.
- Wenn die Downloaddatei bereits vorhanden ist, wird diese im erneuten Downloadvorgang übersprungen.
- Teilweise heruntergeladene Dateien werden komplett heruntergeladen.
- Automatische Dateiauswahl nach Generierung von Links Datei und Login Datei.
- Das Programm lädt die Dateien dort weiter herunter, wo es aufgehört hat, sollte es zu einer unvorhersehbaren Programmschließung kommen, weil es die bereits heruntergeladenen Daten überspringt.
- Das Programm überprüft auch, ob die Dateien vollständig heruntergeladen worden sind, falls nicht, startet der Download erneut.

---
## EXE
https://github.com/FelberPeter/Simple-InternetArchive-Donloader/blob/9b50848a6df04e5f53c34e138ec4612c5d0b5def/dist/InternetArchiveDonwloader.exe
