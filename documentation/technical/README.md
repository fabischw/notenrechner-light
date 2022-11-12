# Notenrechner (NTR) technical documentation

* this documentation is NOT meant for end-users
* this documentation does not replace the need for a quick look at the source code for contributors
* it is meant to provide a quick overview of the project's codebase
* NOTE: many README's refer to the [notenrechner project's documentation](https://github.com/fabischw/notenrechner/blob/main/documentation/README.md) which is the foundation for this project

### general

* this project represents the frontend as well as the simplified backend for the [notenrechner project](https://github.com/fabischw/notenrechner)
* [used technology](technology.md)
* this project is currently being developed as personalised dashboard which will be hosted on the user's own machine, for more info check [this](./backend/data/README.md) -> configurations

###### project structure:
- [DRAWIO](./structure/general_structure_revamp_01.drawio)
- [PNG](./structure/general_structure_revamp_01.png)
- [SVG](./structure/general_structure_revamp_01.svg)

<details> <summary>documentation structure</summary>

## documentation structure

Quick overview over the structure of the documentation


##### [Notenrechner-copy](../notenrechner-copy)

* This is a copy of the Notenrechner project's documentation which serves as the main repository for backend planing

##### [backend](./backend)

This part of the documentation focuses on the backend part of the Notenrechener which includes:

* the user data (settings and app data)
* code for possible database integrations

##### [glue](./glue)

This part of the documentation focuses on the 'glue' layer which serves as a kind of API between the app's data (backend) and the frontend layer, this includes:

* data querying
* data managment
* read/write logic for the basic data design
* parsing

##### [frontend](./frontend)

This part of the documentation focuses on the frontend section of the app, which includes:

* the different apps pages
* the implementation of settings etc
* scripts for data visualiziation
* glue layer calls and datacore initializatiion

</details>

### [frontend](./frontend/README.md)

### [glue layer](./glue/README.md)

### [backend](./backend/README.md)


