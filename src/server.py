
import socket, sys

# Create socket
def create_socket():

    try:
        global host
        global port
        global s
        host = ''
        port = 12345

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as err:
        print("Couldn't create socket due to: "+ str(err))

# Bind the socket to the host and the port
def bind_socket():
        
    try:
        global host
        global port
        global s
        print ("Binding host: {} with port: {}".format(str(host), str(port)))
        s.bind((host, port))
        s.listen(5)

    except socket.error as err:
        print ("Couldn't bind the socket due to: {}".format(str(err)))
        print ("Retrying...")
        bind_socket()

# Establish connection with the client
def accept_connection():

    try:
        conn, add = s.accept()
        print ("Connection established with host: {} on port: {}".format(add[0], add[1]))
        send_commands(conn)
        conn.close()

    except:
        print("Couldn't connect!")

 
# Send commands
def send_commands(conn):

    while True:

        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            response = str(conn.recv(2048), "utf-8")
            print(response, end="")   ## Don't send the cursor to the new line


def Main():
    create_socket()
    bind_socket()
    accept_connection()


if __name__ == "__main__":
    Main()







            
            



