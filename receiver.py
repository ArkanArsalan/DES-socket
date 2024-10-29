import socket
from DES import DES


def server_program():
    des = DES()
    
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024)
        if not data:
            break
        
        raw_message = data.decode('utf-8')
        print("Cipher text received: " + str(raw_message))
    
        plain_text = des.decryption(raw_message)
        print("Plain text received: " + str(plain_text))

    conn.close()


if __name__ == '__main__':
    server_program()