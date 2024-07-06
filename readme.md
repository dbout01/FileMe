## Overview

**Project Title**: FileMe

**Project Description**: A server that allows clients to upload and download files securely over the network. This is a Client-Server application.


**Project Goals**:
- Secure File Transfer: Ensure all file transfers are secured with encryption to protect data integrity and privacy during transmission.
- Scalability: Design the server to handle multiple client connections simultaneously without performance degradation.

## Instructions for Build and Use

Steps to build and/or run the software:
1. Installation of Dependencies:
   1a. Ensure Python 3.x is installed on your system. If not, download and install it from python.org.
   1b. Install necessary Python libraries: pip install <library_name>
2. Server Setup:
  2a. Navigate to the server directory: cd path/to/server
   2b. Start the server by running: python file_server.py
4. Client Setup:
   3a. Navigate to the client directory: cd path/to/client
   3b. Start the client application: python file_client.py

Instructions for using the software:
1. Uploading a File:
    1a. On the client application, select 'Upload' and choose the file you wish to send to the server.
2. Downloading a File:
    2a. Enter the name of the file you want to download from the server.
3. Listing Files:
    3a. To view all files on the server, select the 'List Files' option.
4. Deleting a File:
    4a. To remove a file from the server, enter the file name and select 'Delete'.

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:
* Python: Version 3.8 or higher.
* PySocket: For handling socket connections.
* OS (Operating System): Compatible with Windows, macOS, and Linux distributions.

## Useful Websites to Learn More

I found these websites useful in developing this software:
* [OSI Model](https://en.wikipedia.org/wiki/OSI_model)
* [Client-Server Model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
* [What's the Difference Between TCP and UDP?](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:
* [ ] Better user interface
* [ ] Allow for transfer of multiple files at once
