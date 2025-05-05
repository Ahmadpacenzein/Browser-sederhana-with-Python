import socket
import ssl
from urllib.parse import urlparse


def main_browser(url):
    parsed = urlparse(url)
    scheme = parsed.scheme
    host = parsed.hostname
    port = parsed.port or (443 if scheme == 'https' else 80)
    path = parsed.path if parsed.path else "/"

    use_ssl = (scheme == 'https')

    # Membuat koneksi socket
    try:
        sock = socket.create_connection((host, port))  # perbaikan: tuple
        if use_ssl:
            context = ssl.create_default_context()
            sock = context.wrap_socket(sock, server_hostname=host)
    except Exception as e:
        print("Gagal Terhubung ke server:", e)
        return

    # Kirim request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    sock.send(request.encode())

    # Terima response
    response = b""
    while True:
        data = sock.recv(4096)
        if not data:
            break
        response += data
    sock.close()

    # Pisah header dan body
    parts = response.split(b"\r\n\r\n", 1)
    if len(parts) == 2:
        header, body = parts
        print(body.decode(errors="ignore"))
    else:
        print(response.decode(errors="ignore"))


# Input dari user
url = input("Masukkan URL (http:// atau https://): ")
main_browser(url)