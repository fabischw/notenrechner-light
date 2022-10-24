# tests for notenrechner
- this folder contains all the testing code for the notenrechner code



## NOTE:
- these tests are NOT automatic and not integrated using github actions
- these are manual tests


## test 'formatting':
for new tests please follow the steps below:
- test should be located in their respective layerof the app (either /frontend, /gue or /backend)
- in those folders, there should be a folder for each file (subfolder / file if needed), if the folder isnt present, simple create one
- in the files's folder, there should be a folder for each function test called test_FUNCTIONNAME
- in the file's folder there should be different folders numbered 0001-9999 (or beyond) which represent the individual tests, the folder name should have a PASS / PEND / FAIL before their number
- in those numbered folders, there should be a test_FUNCTIONNAME.py, a README.md and possibly other required files

- the test repot should be in the README.md along with the test description

- for an example check [this folder](./EXAMPLE_TEST/)

- Happy testing !