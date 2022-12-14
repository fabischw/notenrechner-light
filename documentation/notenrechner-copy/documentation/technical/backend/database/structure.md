# Database structure (work in progress)
- This README is meant to outline the fundamental  data structure behind the Notenrechner Oracle database

# general structure of the database
- [database blueprint](./linked_resources/tables/blueprint.drawio)
- Link to the file to create the databse structure: 

#### Administrative tables
- PERMISSIONS: This table contains the different permissions copes defined by the administrator
- USERS: This table contains the data about the different Users
- LOG: This table contains the logs of all activities happening on the database, however this is not the official database log table, it's a dedicated table

#### system tables
- LOG: This table contains the logs of all activities happening on the database, however this is not the official database log table, it's a dedicated table
- DEL: This table contains deleted data for a not yet specified time until it's finally deleted
- TABLES: This table contains data on all the tables that make up the Notenrechner database structure

#### REF tables
- Lehrer-Fach-REF: This table contains the link between the Lehrer and the Fach tables
- Kurs-Stunden-REF: This table contains the link between the Kurs and the Stunden tables
- Kur-Events-REF: This table contains the link betwwen the Kurse and the Events tables
- Noten-Schueler-REF: This table contains the link between the Kurs and Schueler tables
- Kurs-Schueler-REF: This table contains the link between the Kurs and the Schueler table
- Users-Permissions-REF: This table contains the link between the Users and the permissions table

#### data tables
- Kurse: This table contains the data on the courses/classes
- Stunden: This table contains the different course time frames
- Lehrer: This table contains the teacher data
- Noten: This table contains the exam results
- Schueler: This table contains the students
- Arbeiten: This table contains the exams
- Kalender: This table contains different events for a specific student (exams, events, etc.)
- Schul_Events: This table contains different school events

### Explanation behind structure
This structure was chosen as a result of different facotrs and requirements set up for the database structure, it needs to be highly efficient when it coems to reading operations since the notenrechner has to work with data warehouse applications, it achieves these goals by using sequences and other techniques


### structure table

| Table_name                                                                        | table_id | table_usecase |
|-----------------------------------------------------------------------------------|----------|---------------|
| [kurs](./linked_resources/tables/data/kurs.md)                                    | 1        | data          |
| [stunden](./linked_resources/tables/data/stunden.md)                              | 2        | data          |
| [fach](./linked_resources/tables/data/fach.md)                                    | 3        | data          |
| [schulevents](./linked_resources/tables/data/schulevents.md)                      | 4        | data          |
| [arbeiten](./linked_resources/tables/data/arbeiten.md)                            | 5        | data          |
| [kalender](./linked_resources/tables/data/kalender.md)                            | 6        | data          |
| [schueler](./linked_resources/tables/data/schueler.md)                            | 7        | data          |
| [noten](./linked_resources/tables/data/noten.md)                                  | 8        | data          |
| [lehrer](./linked_resources/tables/data/lehrer.md)                                | 9        | data          |
| [fach](./linked_resources/tables/data/fach.md)                                    | 10       | data          |
| [schule](./linked_resources/tables/data/schule.md)                                | 22       | data          |
| [kursschuleventsref](./linked_resources/tables/ref/kursschuleventsref.md)         | 11       | ref           |
| [kursstundenref](./linked_resources/tables/ref/kursstundenref.md)                 | 12       | ref           |
| [kursschuelerref](./linked_resources/tables/ref/kursschuelerref.md)               | 13       | ref           |
| [lehrerfachref](./linked_resources/tables/ref/lehrerfachref.md)                   | 14       | ref           |
| [notenschuelerref](./linked_resources/tables/ref/notenschuelerref.md)             | 15       | ref           |
| [USERRPERMISSIONNREF](./linked_resources/tables/ref/USERRPERMISSIONNREF.md)       | 16       | ref           |
| [TABLESS](./linked_resources/tables/sys/TABLESS.md)                               | 17       | system        |
| [LOGS](./linked_resources/tables/sys/LOGS.md)                                     | 18       | system        |
| [USERR](./linked_resources/tables/sys/USERR.md)                                   | 19       | system        |
| [DELL](./linked_resources/tables/sys/DELL.md)                                     | 20       | system        |
| [PERMISSIONN](./linked_resources/tables/sys/PERMISSIONN.md)                       | 21       | system        |

- NOTE: some table names are misspelled on purpose since oracle reserves some keywords like logs, users et.