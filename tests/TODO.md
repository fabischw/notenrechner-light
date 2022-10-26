# TODO things
This is a simple TODO things for the notenrechner app



<details>
<summary>testing</summary>

### /glue


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



### glue
- finish the function to load data
- finish the function to read data
- add initial read to startup process according to the selected setting


###### data_core
- add functionality for reading (file)
- add functionality for writing (file)
    -> add functions for appending to session_state DATE
    -> add functions for stripping elements from session_state DATA

###### data_reader
- add function to translate PLSQL datatypes to python


## possible design changes:
- make main.py into a init function to init the app
- add check for each file if page is rerun -> rerun using proposed init app
- add check value to session_state

</details>







<details>
<summary>DOCUMENTATION</summary>

### documentation required:

### frontend (USER) -> GERMAN
- Install
- Usage



### frontend (technical)
- structure
- flowchart events



### glue
- ALL


</details>