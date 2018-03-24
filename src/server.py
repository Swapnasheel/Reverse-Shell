
import socket, sys

# Create socket
def create_socket():

    try:
        global hostname
        global port
        global conn
        host = ''
        port = 12345

        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("Couldn't create socket due to: "+ str(err))


        
