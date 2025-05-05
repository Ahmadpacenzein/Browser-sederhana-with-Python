import socket
import ssl
from urllib.parse import urlparse

def main_browser(url):
    try:
        parsed = urlparse(url)
        scheme = parsed.scheme
        host = parsed.hostname
        port = parsed.port or (443 if scheme == 'https' else 80)
        path = parsed.path if parsed.path else "/"
        use_ssl = (scheme == 'https')

        sock = socket.create_connection((host, port))
        if use_ssl:
            context = ssl.create_default_context()
            sock = context.wrap_socket(sock, server_hostname=host)

        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        sock.send(request.encode())

        response = b""
        while True:
            data = sock.recv(4096)
            if not data:
                break
            response += data
        sock.close()

        parts = response.split(b"\r\n\r\n", 1)
        body = parts[1] if len(parts) == 2 else response
        return body.decode(errors="ignore"), None

    except Exception as e:
        return "", str(e)
