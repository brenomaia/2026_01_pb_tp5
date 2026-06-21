import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443


ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

# 3. Cria o socket TCP padrão e associa ao endereço
bind_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bind_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
bind_socket.bind((HOST, PORT))
bind_socket.listen(5)

print(f"Servidor TLS rodando em https://{HOST}:{PORT}")

try:
    while True:
        client_socket, from_address = bind_socket.accept()
        print(f"Conexão TCP aceita de {from_address}. Iniciando TLS Handshake...")
        
        try:
            secure_socket = ssl_context.wrap_socket(client_socket, server_side=True)
            
            data = secure_socket.recv(1024).decode('utf-8')
            print(f"Recebido do cliente: {data}")
            
            resposta = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nConexao TLS segura estabelecida com sucesso!"
            secure_socket.sendall(resposta.encode('utf-8'))
            
        except ssl.SSLError as e:
            print(f"Falha no TLS Handshake: {e}")
        finally:
            # Garante o fechamento seguro do socket do cliente
            secure_socket.close()

except KeyboardInterrupt:
    print("\nDesligando o servidor...")
finally:
    bind_socket.close()