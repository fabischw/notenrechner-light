# app structure
- This is an in-depth explanation on the structure of the app
- it explains the different layers as well as what layer is responsible for as well as how they're linked

<!-->explanation for the frontend folder<!-->
<details>
<summary>frontend structure</summary>

### frontend structure
The frontend is made up of the actual frontend user interface as well as helper functions.

##### GUI
the code for the user-interface

- the entry file for the entire frontend (project in general) is [home.py](../../../frontend/home.py), which includes:
    - code for the GUI of the home-page
    - call to the main / frontend_funcs files to initialize the data core

- in the [pages folder](../../../frontend/pages/) there are all the pages the user will see and be able to navigate using the sidebar
    - the numbers in the page name represent the index in the sidebar list

- the pages include the following:

- [1_einfache-Funktionen](../../../frontend/pages/1_einfache-Funktionen.py) which includes:
    - simple functions not connected to the data_core which provide mostly small QOL (quality of life) features such as:
        - average grade calculator for grades given via input in sidebar
        - calculating a final grade based on previous grades and other information
        - calculating the requires scores for each grade in a exam
        - tool to quickly count points

- [2_notenanalyse](../../../frontend/pages/2_%F0%9F%93%88_notenanalyse.py) which includes:
    - functionality to write and read grades form the local storage when the app is being run as localhost app (GUI only, does not incldue the actual read/write code)
    - functionality to display current data 
    - functions to analyse and graph the present data (calculations not performed in this file, calls to others)

- [3_datenbrowser](../../../frontend/pages/3_datenbrowser.py) which includes:
    - functionality to browse exiting data

- [4_query-data](../../../frontend/pages/4_query-data.py):
    - query data from database extenstions is present

- [5_bibliothek](../../../frontend/pages/5_bibliothek.py):
    - library of useful links for students as well as teachers

- [6_Einstellungen](../../../frontend/pages/6_Einstellungen.py):
    - settings for:
        - input (slider vs field)
        - theme
        - configs



##### init functions, others:
code for initializing different components of the glue / backend layer, other smaller functions which are only required in the frontend, loading the settings
Init functions / files include:

- [main.py](../../../frontend/main.py)
    - load settings and put the data in the session_state dictionairy
    - load the current config
    - call the data_core init function

- [frontend_funcs.py](../../../frontend/frontend_funcs.py)
    - call the main init function



</details>
