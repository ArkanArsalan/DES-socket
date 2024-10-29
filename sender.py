import socket
from DES import DES


def client_program():
    des = DES()
    
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    user_input = input("Masukkan input (8 Karakter Text): ")

    if not (1 <= len(user_input) <= 8):
        raise ValueError("Input text harus berisi 1 hingga 8 karakter.")

    encrypted_msg = des.encryption(user_input)
    
    client_socket.sendall(bytes(encrypted_msg, 'utf-8'))
    
    client_socket.close()
        

if __name__ == '__main__':
    client_program()