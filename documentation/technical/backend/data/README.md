# data managment documentation for the notenrechner light project
- there are multiple possible settings / configurations in which data can be managened
- currently the main focus are configurations 0 and 1, 2 is delayed until further notice, the web version is also postponed


<details>
<summary>configurations</summary>

### possible setttings / configurations

| setting_number | setting_name         | setting_description                                | location | type              | size       | additional                      |
|----------------|----------------------|----------------------------------------------------|----------|-------------------|------------|---------------------------------|
| 0              | full local csv       | uses local csv according to the database scheme    | local    | appdata/user_data | full       | all except noten_simplified.csv |
| 1              | simplified local csv | uses a single, simplified csv for grades only      | local    | appdata/user_data | simplified | noten_simplified.csv            |
| 2              | full local DB        | uses local oracle db with the full database scheme | local    | --DATABASE--      | full+      | ORA 21c XE                      |


- the size refers to how many 'tables' / files the program uses to store data, it also refers to how many columns the main grade data has
- full / full+ refer to the original database layout proposed in the [notenrechner project](https://github.com/fabischw/notenrechner) at [documentation](https://github.com/fabischw/notenrechner/blob/main/documentation/technical/backend/database/structure.md)
- the difference between full and full+ being that full doesn't include the 'SYS' tables
- the simplified layout only supports the noten_simplified.csv file which has less columns than the [notenrechner noten table](https://github.com/fabischw/notenrechner/blob/main/documentation/technical/backend/database/linked_resources/tables/data/noten.md)

</details>