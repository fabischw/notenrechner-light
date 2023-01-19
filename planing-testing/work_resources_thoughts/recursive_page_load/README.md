# recurisve page load
This folder contains resources and thoughts to solve a pressing issue which causes the app to crash because of an infinite recursion

### problem description:
in order to perform the security checks on read/write operations the corrosponding settings have to be in the session_state.
If the data is not in the session_state the datareader re-loads the settings using a utility-module which triggers an infinite loop

### possible solutions to the problem:
- perform secuirty checks on data in a seperate file (-> may not work if this different file is called by the data_reader itself, different loading process required)
- load the security data not using the data-reader but a dedicated function / module / file