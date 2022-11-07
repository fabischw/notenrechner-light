# TODO things
This is a simple TODO things for the notenrechner app



<details>
<summary>testing</summary>

### /glue
- ALL

##### /data_core
- init_data_core()
- do_initial_read()
- init_pd_dataframes()


##### /data_formats
- ntr_data_formatter / get_data_format()


##### /data_objcts
- OBJCTS


##### /data_reader
- check_data()
- read_data()
- validate_inpt_13()
- write_data()



</details>



<details>
<summary>DEV</summary>

### frontend
- add config setting to page 6_Einstellungen
- add security settings to page 6_Einstellungen (-> configure how much inputs are being checked)
- remove automatic setting rewrite (bind to config settings, -> make merge to deploy possible)
- add entire page 2 UI



### glue
- finish the function to load data
- finish the function to read data
- 


###### data_core
- add functionality for reading (file)
- add functionality for writing (file)
    -> add functions for appending to session_state DATA
    -> add functions for stripping elements from session_state DATA

###### data_reader
- add function to translate PLSQL datatypes to python
- build secure read function (based on format checking from write function)
- remove comment lines from list of naughty strings comparison


## possible design changes:
- make main.py into a init function to init the app
- add check for each file if page is rerun -> rerun using proposed init app
- add check value to session_state

- change session_state settings to be in a dedicated dictionairy

</details>







<details>
<summary>DOCUMENTATION</summary>

### documentation required:

### frontend (USER) -> GERMAN
- Install
- Usage
    -> reveal.js guide



### frontend (technical)
- structure
- flowchart events



### glue
- ALL

### backend
- Noten simplified layout(table)

</details>



<details>
<summary>important / urgent changes</summary>

## this is a lot of important changes to do
- change SQL table layout for the 'schueler' table, 'schule' column
- change SQL table layout for the 'lehrer' table, 'email' column REQ status
- add Schule table to the SQl layouts


</details>