import pcapy
from datetime import datetime

# usei aqui lo0 pois é o padrão do mac, no linux é lo e no windows pode ser outra
INTERFACE = "lo0"
PORTA = 8443
MAX_BYTES = 65535
PROMISCUOUS = 1
TIMEOUT_MS = 100

print(f"Iniciando captura na interface '{INTERFACE}' para a porta {PORTA}...")

cap = pcapy.open_live(INTERFACE, MAX_BYTES, PROMISCUOUS, TIMEOUT_MS)
cap.setfilter(f"tcp port {PORTA}")

def packet_handler(header, data):
    timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
    
    # O tamanho do cabeçalho IP e TCP varia, mas os dados úteis (payload) ficam no final.
    # Como o TLS/HTTP é texto/binário legível em partes, vamos tentar decodificar o payload.
    # Nota: Como o tráfego é TLS, os dados pós-handshake aparecerão criptografados (garbaged text).    
    print(f"\n[{timestamp}] Pacote capturado! Tamanho: {header.getlen()} bytes")
    
    # Tenta extrair e exibir caracteres imprimíveis dos dados brutos (estilo dump do wireshark)
    payload = data[54:] # Pula aproximadamente os cabeçalhos Ethernet+IP+TCP (simplificado)
    if payload:
        # Mostra os primeiros 150 caracteres do que está passando
        printable_data = ''.join(chr(b) if 32 <= b < 127 else '.' for b in payload[:150])
        print(f"  Dados (fatia): {printable_data}")

try:
    # -1 = ler indefinidamente
    cap.loop(-1, packet_handler)
except KeyboardInterrupt:
    print("\nCaptura encerrada.")