# Import socket module
from socket import *
# In order to terminate the program
import sys
# Import thread module
from _thread import *
import threading

thread_lock = threading.Lock()

# thread function
def run(connectionSocket):
    while True:
        try:
            message = connectionSocket.recv(2048).decode()
            filename = message.split()[1]
            if filename == "/exit":
                break

            # Open the file in binary mode
            with open(filename[1:], 'rb') as f:
                content = f.read()
            
            # Send one HTTP header line into socket
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            
            # Send the content of the requested file into socket
            connectionSocket.sendall(content)
            
            # lock released on exit
            thread_lock.release()
            break

        except IOError:
            # Send response message for file not found
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("File not found".encode())
            # lock released on exit
            thread_lock.release()
            break
        
    # Close client socket
    connectionSocket.close()

if __name__ == '__main__':
    # Prepare a sever socket
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverPort = 50788
    serverAddress = ""
    serverSocket.bind((serverAddress,serverPort))
    serverSocket.listen(2)

    while True:
        # Establish the connection
        connectionSocket, addr = serverSocket.accept()
        print('Serving to :', addr[0], ':', addr[1])
        thread_lock.acquire()
        start_new_thread(run, (connectionSocket,))

    # Close server socket
    serverSocket.close()

    # Terminate the program after sending the corresponding data
    sys.exit()
