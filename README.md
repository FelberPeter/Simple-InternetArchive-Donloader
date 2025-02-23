# Simple-InternetArchive-Downloader

**WICHTIG:**  
Es müssen mindestens "WÄHLE LINKS DATEI", "WÄHLE ZIELORDNER" und "WÄHLE LOGIN DATEI" ausgewählt sein, damit der Download gestartet werden kann!

---

## PROGRAMMVERWENDUNG:

1. Speichern der Seite als Downloadlink im HTML-Format.
2. Starten des Programmes.
3. Den ersten Button anklicken, um das Ziel-HTML auszuwählen.
4. "Erstelle Downloadlinks" -> nimmt die HTML-Datei und extrahiert alle Z7-Downloadlinks und speichert sie in einer TXT-Datei.  
    Diese TXT-Datei wird bei jedem Generieren überschrieben und kann auch manuell bearbeitet werden.  
    Nach dem Generieren wird die TXT-Datei automatisch ausgewählt (kann auch manuell mit dem "Wähle Links Datei" ausgewählt werden).
5. Mit dem Button "Wähle Zielort aus" wird ausgewählt, wohin die Downloads gespeichert werden.
6. "Erstelle Login Datei" -> öffnet Google Chrome mit der Login-Seite von Internet Archive.  
    Nach abgeschlossenem Login schließt sich die Website automatisch.  
    Es wird eine JSON-Datei mit den Login-Daten anhand der Cookies erstellt.  
    Diese wird automatisch ausgewählt oder kann auch manuell mit dem "Wähle Login Datei" ausgewählt werden.
7. "Start Download" -> öffnet ein weiteres Fenster mit dem Fortschritt inkl. Pause- und Abbruch-Button.

Beim erneuten Öffnen werden die vorhin ausgewählten Dateien gespeichert!

---

## FEATURES:

- Pfade werden gespeichert.
- Wenn die Downloaddatei bereits vorhanden ist, wird diese im erneuten Downloadvorgang übersprungen.
- Teilweise heruntergeladene Dateien werden komplett heruntergeladen.
- Automatische Dateiauswahl nach Generierung.
- Das Programm lädt die Dateien dort weiter herunter, wo es aufgehört hat, sollte es zu einer unvorhersehbaren Programmschließung kommen, weil es die bereits heruntergeladenen Daten überspringt.
- Das Programm überprüft auch, ob die Dateien vollständig heruntergeladen worden sind, falls nicht, startet der Download erneut.

---
