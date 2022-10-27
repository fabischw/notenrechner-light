# data_core documentation

### init_pd_dataframes()
- generates all empty pandas dataframes with columns which can be found [here]()
- stores an dictionary with all the generated dataframes as items and table names as keys in st.session_state as "DATA"

### do_initial_read(datasources)
- does the initial data read, reading all the data in the files given via the datasources parameter
- actively appends the read data to the session_state "DATA" dataframes



### init_data_core()
- does all the initialization there is to do
    -> 