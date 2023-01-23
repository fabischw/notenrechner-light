# recurisve page load
This folder contains resources and thoughts to solve a pressing issue which causes the app to crash because of an infinite recursion
problem introduced in d1c3f1828a76bca4d7d7406be49f72f1ce9f1b46

- STATUS: temporary fix deployed

### problem description:
in order to perform the security checks on read/write operations the corrosponding settings have to be in the session_state.
If the data is not in the session_state the datareader re-loads the settings using a utility-module which triggers an infinite loop

### possible solutions to the problem:
- perform secuirty checks on data in a seperate file (-> may not work if this different file is called by the data_reader itself, different loading process required)
- load the security data not using the data-reader but a dedicated function / module / file

### UPDATES
- the checks have been moved to the data_checks file
- temporary fix introduced in commit 5f39aea3b82e4b37355298416381391c155dfe7b
  (import, security settings loading commented out until solution is found)
-
