import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443

context = ssl.create_default_context()
context.load_verify_locations(cafile="cert.pem")

HOST_TARGET = 'localhost'

print(f"Conectando ao servidor TLS em {HOST_TARGET}:{PORT}...")

with socket.create_connection((HOST, PORT)) as tcp_socket:
    with context.wrap_socket(tcp_socket, server_hostname=HOST_TARGET) as secure_socket:
        print("Handshake TLS bem-sucedido!")
        
        # Envia uma requisição HTTP simples
        mensagem = b"AUTH_TOKEN:XYZ123:CMD:REBOOT_SERVER."
        secure_socket.sendall(mensagem)
        
        # Recebe a resposta do servidor
        resposta = secure_socket.recv(4096)
        print("\n--- Resposta do Servidor ---")
        print(resposta.decode('utf-8'))