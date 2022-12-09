# settings explenation
This file describes what different settings in notenrechnersettings do


<details>
<summary>datasource</summary>

## datasource setting explenation:

- location: where the app is running, local being on a local machine as localhost and cloud meaning either linked to a cloud for data or running in the web configuration
- type: this is what kind of data the app has to load: either csv's in appdata/user_data or a database
- db_link: whether the app is linked to a database or not
- db_type:
    - db_name: either null if no DB is present or a string with the DB name (ex: myOracle)
    - db_username: database username, null if not present, string with username if present
    - db_userpass: database password, null if not present, string with password if present
    - db_specific: array with database specific information

</details>




<details>
<summary>version</summary>

## version

- platform: what platform the app is running on (either localhost or deployed)
- type: what type of version the current version is: either "DEV","PROD-ALPHA","PROD-BETA" or "PROD-STABLE", names should be self-explaining.
- version: version float, countint up from 0.001
- keyword: a keyword assigned to each 'release', shown to user to provide additional info
- full: if the current ap config is a full version or not (-> minimal if not full, see configurations for more info)

</details>




<details>
<summary>settings</summary>

## settings
- inpt_prefered: what input the user prefers (slider vs input field)
- theme: the theme a user picks (not avilable yet)

</details>






<details>
<summary>security</summary>

## security


#### write:
- check_dangerous: check whether a input is potentially dangerous
- check_path_existence: check if the path exists before writing data (prevents creating files and writing data to wrong files)
- check_if_data_already_present: check if the data is already present (should be turned off when using the simplified scheme)
- check_indexing: check if the indexes are correct and continues
- check_length: check if the defined length from the PL/SQL database schemes are correct, if this is turnedof, maximum length can be ignored, makes connecting to DB impossible!
- enforce_required: enforce the required datatypes and similar, should always be on !
- check_general_format: check whether the general format of the data being written is correct, should always be on !



#### read:
- check_dangerous: check whether a input is potentially dangerous
- check_path_existence: check if the path exists before writing data (prevents creating files and writing data to wrong files)
- check_if_data_already_present: check if the data is already present (should be turned off when using the simplified scheme)



</details>