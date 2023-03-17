# Installing:

First, you have to install python
>> $ sudo apt install python3

As soon as python is installed, install pip
>> $ sudo apt install pip
    
And then install the google API library
>> $ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

After that, you will need to download the client_secret.json. You can do that by opening google cloud console, then going to API and services, then credentials and downloading the client OAuth key. 

Then, put the file you downloaded in the same folder as the code, rename it to "client_secret.json" and it's done.

# Using the program:

Just run main.py

>> $ ./main.py

