# Konfigurationen
- Diese Datei bietet einen Überblick, über die Notenrechner Konfigurationen


| Kennzahl | Name           | host                                         | location | datasource    | csv type | status  |update/refernce |
|----------|----------------|----------------------------------------------|----------|---------------|----------|---------|----------------|
| 0        | streamlit      | [web](https://notenrechner.streamlitapp.com) | -        | csv Datei     | minimal  | HALTED  |                |
| 1        | local csv      | localhost                                    | local    | csv Datei     | medium   | DEV     |                |
| 2        | local oracle   | localhost                                    | local    | ORA DB 21c XE | -        | PLANING |                |
| 3        | local csv full | localhost                                    | local    | csv Datei     | full     | CONCEPT |                |


# Erklärung der Konfigurationen

## Konfiguration 0:
- Diese Konfiguration ist für jeden frei von jedglichem Aufwand bequem über das Internet abrufbar
- Die Funktionalität beschränkt sich auf die Nutzung simpler Funktionen
- Für die Notenanalyse kommt nur das lesen von csv Dateien, welche der Nutzer selbst generieren und auf seinem Gerät speichern muss, in Frage
- Die Entwicklung dieser Konfiguration wurde angehalten


## Konfiguration 1:
- Diese Konfiguration ist auf relativ simple Art und Weise lokal zu nutzen
- Sie bietet ähnliche Funktionalität wie die webversion
- Für die Notenanalyse werden automatisch lokal Dateien gespeichert und verwaltet
- Diese Konfiguration befindet sich in der Entwicklungsphase


## Konfiguration 2:
- Diese Konfiguration ist die derzeit komplexeste
- Die Konfiguration verbindet sich mit einer lokal betriebenen oracle Datenbank und nutzt diese für die Speicherung der Daten
- Die Konfiguration befindet sich in der Planungsphase


# Konfiguration 3:
- Diese Konfiguration ist bisher nur ein Konzept
