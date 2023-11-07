# Web Server Project
## Overview
Welcome to the "Web Server" project! This project involves creating a simple web server in Python that can handle HTTP requests and serve web pages. In this README, we will provide an overview of the project, its implementation, and how to use it.

## Project Description
The "Web Server" project consists of two parts:

### Part 1: Single-Threaded Web Server
In this part, you'll develop a basic web server that can handle one HTTP request at a time.
The server will accept and parse incoming HTTP requests, retrieve requested files from the server's file system, and send HTTP response messages.
### Part 2: Multi-Threaded Web Server
Building upon Part 1, you'll implement a multi-threaded web server that can serve multiple requests simultaneously.
Threading will be used to create separate threads for handling each request, ensuring concurrent processing.

## How to Use
Follow these steps to set up and use the web server:
1. Python environment with required libraries.
2. Clone this repository to your local machine:
3. Navigate to the project directory:
4. Running the Web Server
  #### Part 1: Single-Threaded Web Server
  Ensure you have the provided HTML file, "home.html," in the same directory as your server source code.
  Run the web server program:
  Determine the IP address of the host running the server and the port number you used (e.g., "http://128.238.251.26:28000/home.html").
  Open a web browser and access the server by providing the URL:
  To test "404 Not Found" handling, try requesting a file that is not present on the server.

  #### Part 2: Multi-Threaded Web Server
  Run the multi-threaded web server
  To test the server's multi-threading capabilities, consider requesting a large file, such as a PDF, from multiple browser tabs simultaneously.


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
