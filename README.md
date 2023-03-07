# Binghamton University, Spring 2023

## CS428/528 Project-1: Web Server

### SUMMARY

Part 1: By requesting a server with specified HTML file name, server sends the encoded format of file's content. And the content of that file will be shown in the browser of client. #
Part 2: In this, multiple clients can request server at the same time. Server will send the encoded format of PDF file's content to all clients. To serve multiple clients, we have used multithreading in python. #
Error 404: If file is not present at server, it will show "File not found" error. #

### NOTES, KNOWN BUGS, AND/OR INCOMPLETE PARTS

[Add any notes you have here and/or any parts of the project you were not able to complete]: #
1. Because PDF file cannot be opened using normal open(), webserver1.py will not work with pdf files. 
2. webserver2.py is only suitable for PDF files and may or may not work for HTML files. (To check multiple requests for HTML file, use webserver2_reqHTML.py if necessary.)
3. There is no screenshot available for multiple pdf file request as it is shown in the demo itself.

### REFERENCES

1. https://stackoverflow.com/questions/4584904/what-causes-the-broken-pipe-error
2. https://realpython.com/python-sockets/

### INSTRUCTIONS

1. Replace the port number and IP address of your system at line number (10) and (11) respectively in webserver1.py and (59) and (60) respectively in webserver2.py. #
2. Now, run any of the server. #
3. Access this server by using this URL in the browser: http://<IP_ADDRESS_HERE>:<PORT_NUMBER_HERE>/home.html for webserver1.py #
4. 3. Access this server by using this URL in the browser: http://<IP_ADDRESS_HERE>:<PORT_NUMBER_HERE>/Project1-WebServer.pdf for webserver2.py
5. For multiple requests, you can use bash file calling the same URL multiple times. #

### SUBMISSION

I have done this assignment completely on my own. I have not copied it, nor have I given my solution to anyone else. I understand that if I am involved in plagiarism or cheating I will have to sign an official form that I have cheated and that this form will be stored in my official university record. I also understand that I will receive a grade of "0" for the involved assignment and my grade will be reduced by one level (e.g., from "A" to "A-" or from "B+" to "B") for my first offense, and that I will receive a grade of "F" for the course for any additional offense of any kind.

By signing my name below and submitting the project, I confirm the above statement is true and that I have followed the course guidelines and policies.

Submission date: 03-03-2023

Team member 1 name: Devashri Pramodrao Shirbhate

Team member 2 name: Jay Balaram Sankhe