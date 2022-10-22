# data managment documentation for the notenrechner light project
- there are multiple possible settings / configurations in which data can be managened


## possible setttings / configurations

| setting_number | setting_name         | setting_description                                | location | type              | size       | additional                      |
|----------------|----------------------|----------------------------------------------------|----------|-------------------|------------|---------------------------------|
| 0              | full local csv       | uses local csv according to the database scheme    | local    | appdata/user_data | full       | all except noten_simplified.csv |
| 1              | simplified local csv | uses a single, simplified csv for grades only      | local    | appdata/user_data | simplified | noten_simplified.csv            |
| 2              | full local DB        | uses local oracle db with the full database scheme | local    | --DATABASE--      | full+      | ORA 21c XE                      |