# Objective

My objective with this project was to improve my scripting skills with Python while automating the timetable generation process.

# Introduction

The objective of this program was to automate how the timetable containing the dedication time of each student for the project was created. Before I entered the Institutional Program of Tutorial Education in Mechatronic Engineering, the process was almost fully manual, in which the responsible Professor would make Google forms to collect data, and then create the timetable manually at Google Sheets.

So when I entered the project, my first task was to automate this process, by creating a script that would take all data from the Forms and create a formatted timetable as specified. 

# Logic and Implementation

First thing first, the script should read the sheet created by Forms, then save it on a dictionary, organise the data in a way that corresponded to the formation, then save the timetable on page 2 of the same sheet created by Forms.

For reading the original sheet, I used Google Sheets API, which would first get the credentials, then connect to Google Drive, and then save the content of the table in the memory. By the end, the same API would be used to save the now formatted timetable on the second page of the same sheet.

# Instalation

For using this script, it is necessary to have Python and Google API Library installed. On Linux systems that use APT as their package manager, the installation of these dependencies can be done by putting the following commands on a terminal:

For installing Python
>> $ sudo apt install python3

As soon as Python is installed, install pip
>> $ sudo apt install pip
    
And then install the google API library
>> $ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

After that, you will need to download the client_secret.json. You can do that by opening google cloud console, then going to API and services, then credentials and downloading the client OAuth key. 

Then, put the file you downloaded in the same folder as the code, rename it to "client_secret.json" and it's done.

# Execution

To execute the program, you just need to run main.py, which can be done by opening a terminal in the same folder as main.py and using the following command:

>> $ ./main.py

# Conclusion

The Script worked as expected, and for the years to come it will not going to be necessary to lose time manually formatting the timetable anymore. But, for me, the major positive of this project was improving my scripting skills with Python and learning how Google APIs worked. 

