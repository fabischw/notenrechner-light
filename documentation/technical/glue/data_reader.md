This file documents the inner workings of the data_reader

### functionality
- the data_reader is responsible for all user_data read/write operations except direct  / initial reads / writes and admin-run commands
- It uses the security settings from the session state to determine the amount of security measures that have to be applied for each read / write action, check the security settings settings (backend/glue) to learn more about these settings
- gets the read/write requests from the data_core

### security settings 
| name(official) | read/write | function(+name) | located at |
|--|--|--|--|
| check_if_data_already_present | write | check_if_data_already_present | check if the data that is being written is already present, the function does this by hashing each row of the data excluding the pandas index column | 
| ADD LATER | read, write | ADD LATER | checks if the value being written / read makes sense and fits the column it is in, this does not include database checks (length and similar) |
| ADD LATER | read, write| ADD LATER| checks if the internal data indexing (not the pandas index) is correct and continues, if not a repair is possible via backend functions|
| check_length | write | check_length | check if the data length is correct (length data from the OCL database table layouts) |
| enforce_required | write | enforce_required | setting to enforce the required database table columns (according to the OCL Database layout) |
| check_general_format | write,read | check_general_format | |
| | | | |







### functions: (read internal documentation -> string description )



h