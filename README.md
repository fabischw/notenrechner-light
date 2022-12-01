![stars](https://badgen.net/github/stars/fabischw/notenrechner-light)
![contributors](https://badgen.net/github/contributors/fabischw/notenrechner-light)
![forks](https://badgen.net/github/forks/fabischw/notenrechner-light)
![PRs](https://badgen.net/github/prs/fabischw/notenrechner-light)
![issues](https://badgen.net/github/issues/fabischw/notenrechner-light)
![watchers](https://badgen.net/github/watchers/fabischw/notenrechner-light)
![total lines](https://tokei.rs/b1/github/fabischw/notenrechner-light)
![LoC](https://tokei.rs/b1/github/fabischw/notenrechner-light?category=code)
![files](https://tokei.rs/b1/github/fabischw/notenrechner-light?category=files)




<!-- not working for whatever reason
![downloads](https://badgen.net/github/assets-dl/fabischw/notenrechner-light)
![commits](https://badgen.net/github/commits/fabischw/notenrechner-light)

-->


# notenrechner light
## Notenorganisation mit Vielzahl an Analyse- und Auswertungsfeatures


- Dies ist ein Projekt, an dem ich in meiner Freizeit arbeite.
- Dieses Projekt befindet sich aktuell in der Entwicklung, eine online Testversion mit eingeschränkter Funktionalität finden sie [hier](https://notenrechner.streamlit.app)
- [LICENSE - GNU general public license](LICENSE)


### Funktionen - eine kleine Auswahl (und aktuell nur eine Vorschau )
- Notenverwaltung: Trage deine Noten ein und organisiere an einem Platz 
- Notenanalyse: Analysiere deine Noten: Erstelle Diagramme, erkenne Trends 
- Quality of Life: Liefert eine Vielzahl an kleinen Funktionen, die das Leben bzgl Noten erleichtern 


### An wen richtet sich die Software:
- Schüler : Nutze die Software für die oben aufgezählten Funktionen und noch viel mehr !
- Lehrer : Lerne, wie du die Software nutzen kannst, um deine Arbeit zu beschleunigen und Noten digital zu organisieren.
- Schulverwaltung (nur experimentell) : Der Notenrechner kann auch für die Verwaltung einer Schule verwendet werden, wobei die Auswahl an Funktionen für diesen Bereich noch sehr beschränkt ist.


<details>
<summary>Warum ausgerechnet dieser Notenrechner ?</summary>

### Was diesen Notenrechner von all den anderen unterscheidet: 
# OpenSource 
- Kostenlos : die Software ist vollkommen kostenlos 
- Erweitern: Du kannst selbst Erweiterungen entwickeln oder Änderungen am Quellcode vornehmen 
- Beitragen: Du kannst Verbesserungsvorschläge und Ideen einbringen, die Entwicklung wird von einer Gemeinschaft entwickelt 
- Datenschutz : Es werden keine Daten an Dritte gesendet, überzeuge dich selbst davon 

</details>



###  Überzeugt? Dann lerne [hier]() wie du den Notenrechner installieren kannst und verwendest

### Hinweise:
- Die Kommentare in der Software sind in englischer Sprache, um den Austausch und das Beitragen zu vereinfachen
- Das frontend und alle für den Nutzer zugänglichen Funktionen sind in deutscher Sprache formuliert.
- Da sich das Projekt noch in der Entwicklungsphase befindet, kann nicht für die Sicherheit garantiert werden.
- Dieses Projekt ist außerdem ein Projekt zum Erlernen vieler neuer Fertigkeiten rund um das Aufgabefeld Softwareentwicklung.

<details>
<summary>Du möchtest zu dem Projekt beitragen ?</summary>

### Du bist Programmierer und möchtest zu dem Projekt beitragen ?
Wenn du Programmierkentnisse hast, kannst du bei der Entwicklung des Notenrechners auf folgende Arten helfen:
- Funktionen entwickeln : Hilf mit, die Funktionalität des Notenrechner zu verbessern !
- Software testen : Testen ist ein wichtiger Teil des Entiwcklungsprozesses, der viel Zeit in Anspruch nimmt. Hilf mit 
- Dokumentation anfertigen : Ohne Dokumentation ist es unmöglich, effizient Software für ein Projekt zu entwickeln und sich zurechtzufinden



### Kein Programmerer ? - Wie du ohne Programmierkentnisse helfen kannst, den Notenrechner zu verbessern
Programmierkentnisse sind keine Voraussetzung, um einen wichtigen Teil beizutragen !
Hier ein paar Dinge, die du tun kannst:
- Werde künstlerisch aktiv und helfe, ansprechende Benutzeroberfächen, Logos und Anleitungen für Nutzer zu designen 
- Hilf beim Testen neuer Funktionen und hilf damit, die Entwicklung zu beschleunigen 
- Reiche Verbesserungsvorschläge und eigene Idee ein, die zu neuen Funktionen und Verbesserungen führen 
- Hilf beim Erstellen von Anleitungen 
- Fehler melden: Melde Fehler die du im Programm findest und hilf uns somit den Notenrechner zu verbessern

## Hilf, dieses Projekt auf die nächste Stufe zu heben 

</details>



<details>
<summary>english</summary>

minimal translation of german text above 
### notenrechner light[EN]
- this is a grade managment system which I'm working on my free time
- this project is still under development

##### note:
- this project's code and technical documentation are in english, the frontend is in german
- this branch you're currently in is for the devlopment of configuration 1
- since this project is still in the development phase, there's not a stable version yet

</details>


<details>
<summary>running in github codespaces</summary>

## Running the program in github codespaces (Experimental only !!!)
- Please be aware that github's guidelines apply for codespace usage and this is use at your own risk
- Keep in mind that running this in github codespaces is not ideal as this project is still under development just like codespaces themselves
- There are are tons of known problems when running this in github codespaces, for more information refer to [this](#issues-running-in-github-codespaces)


[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=546249014)

- To start the app run these lines in your terminal (make sure you install the dependencies first):
```bash
cd ./frontend
streamlit run home.py --server.enableCORS false --server.enableXsrfProtection false
```


##### Installing dependencies
```bash
pip install -r requirements.txt
```


##### Issues running in github codespaces
- Please do not create an github issue if the app doesn't run correctly when used in github codespaces
- instead, add the issue in [this folder](./tests/problems/codespaces-issues/), refer to the community guidelines (WIP) on information on how to structure your issues and how to submit them


</details>



### Documentation / Dokumentation
- [technical](./documentation/technical/README.md)
- [User / Nutzer](./documentation/user/README.md)



### contributors
![GitHub Contributors Image](https://contrib.rocks/image?repo=fabischw/notenrechner-light)