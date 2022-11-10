# Konfigurationen
- Dieses Dokument bietet einen Überblick, über die Notenrechner Konfigurationen



| Kennzahl | Name           | host                                         | location | datasource    | csv type | status                  |update/refernce                                          |
|----------|----------------|----------------------------------------------|----------|---------------|----------|-------------------------|---------------------------------------------------------|
| web      | streamlit      | [web](https://notenrechner.streamlitapp.com) | -        | csv Datei     | minimal  | TEST-DEPLOYED / HALTED  | [online version](https://notenrechner.anvilapp.com)     |
| 0        | local csv full | localhost                                    | local    | csv Datei     | full     | DEV                     |                                                         |
| 1        | local csv      | localhost                                    | local    | csv Datei     | medium   | DEV                     |                                                         |
| 2        | local oracle   | localhost                                    | local    | ORA DB 21c XE | -        | PLANING                 | [repo](https://github.com/fabischw/notenrechner)        |



# Erklärung der Konfigurationen

## Konfiguration web:
- Diese Konfiguration ist für jeden frei von jedglichem Aufwand bequem über das Internet abrufbar
- Die Funktionalität beschränkt sich auf die Nutzung simpler Funktionen
- Für die Notenanalyse kommt nur das lesen von csv Dateien, welche der Nutzer selbst generieren und auf seinem Gerät speichern muss, in Frage
- Die Entwicklung dieser Konfiguration wurde angehalten


## Konfiguration 0:
- Diese Version nutzt eine vereinfachte lokale csv Datei, um die Noten zu speichern und ähnelt der web Konfiguration
- Diese Konfiguration befindet sich in der aktiven Entwicklung


## Konfiguration 1:
- Diese Konfiguration ist auf relativ simple Art und Weise lokal zu nutzen
- Sie bietet ähnliche Funktionalität wie die webversion
- Für die Notenanalyse werden automatisch lokal Dateien gespeichert und verwaltet
- Diese Konfiguration befindet sich in der Entwicklungsphase


## Konfiguration 2:
- Diese Konfiguration ist die derzeit komplexeste
- Die Konfiguration verbindet sich mit einer lokal betriebenen oracle Datenbank und nutzt diese für die Speicherung der Daten
- Die Konfiguration befindet sich in der Planungsphase



