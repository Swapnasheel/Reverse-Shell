
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

# Bind the socket to the host and the port
def bind_socket():
        
    try:
        global hostname
        global port
        global conn
        print ("Binding host: {} with port: {}".format(str(host), str(port)))
        conn.bind((host, port))
        conn.listen(5)
    except socket.error as err:
        print ("Couldn't bind the socket due to: {}".format(str(err)))
        print ("Retrying...")
        bind_socket()

# Establish connection with the client
def accept_connection():

    try:
        conn, add = conn.accept()
        print ("Connection established with host: {} on port: {}".format(add[0], add[1]))
        send_commands(conn)
        conn.close()


