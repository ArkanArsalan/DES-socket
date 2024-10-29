import socket
from DES import DES


def client_program():
    des = DES(role="Sender")
    
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    while True:
        message = input(" -> ")
        if message.lower().strip() == 'stop':
            des.log_with_timestamp("Stop signal sent.")
            client_socket.sendall(bytes("stop", 'utf-8'))  # Kirim sinyal “stop” ke receiver
            print("Stop signal sent to receiver. Closing connection.")
            break  # Akhiri loop untuk menutup koneksi

        # Kirim pesan terenkripsi
        cipher_text = des.encryption_cbc(message, output_format="hex")
        des.log_with_timestamp(f"Cipher text sent: {cipher_text}")
        client_socket.sendall(bytes(cipher_text, 'utf-8'))

        # Terima pesan dari receiver
        data = client_socket.recv(1024)
        raw_message = data.decode('utf-8')
        des.log_with_timestamp(f"Cipher text received: {raw_message}")

        if raw_message.lower() == 'stop':
            print("Stop signal received from receiver. Closing connection.")
            break  # Akhiri loop untuk menutup koneksi

        plain_text = des.decryption_cbc(raw_message, output_format="text")
        des.log_with_timestamp(f"Plain text: {plain_text}")
        print(f'Plain Text: {plain_text}')

    client_socket.close()
    print("Connection fully closed by both parties.")


if __name__ == '__main__':
    client_program()
