from proxy_mod.core.server import Server, CONSOLE
import socket

class HttpProxy(Server):
    def __init__(self, host=None, port=None):
        super().__init__(host, port)
        CONSOLE.info(f"HTTP Proxy initialized on {self.host}:{self.port}")

    def handle_client(self, client_socket, client_address):
        """Handles an HTTP client connection by forwarding the request."""
        request = client_socket.recv(4096)
        request_str = request.decode(errors="ignore")

        CONSOLE.debug(f"Received request from {client_address}")
        CONSOLE.debug(request_str)
        
        """
        Example request:
        
        GET http://www.google.com/ HTTP/1.1
        Host: www.google.com
        User-Agent: curl/8.5.0
        Accept: */*
        Proxy-Connection: Keep-Alive      
        """

        first_line = request_str.split("\n")[0]
        url = first_line.split(" ")[1] # 
        host = None
        port = None

        CONSOLE.debug(f"Request URL: {url}")

        if "://" in url:
            url = url.split("://")[1]

        CONSOLE.debug("URL after stripping protocol: " + url)
        if ":" in url:
            host = url.split(":")[0]
            port = int(url.split(":")[1].split("/")[0])

        else:
            port = 80
            
        CONSOLE.debug(f"Forwarding request to {host}:{port}")

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((host, port))
        server_socket.send(request)

        response = server_socket.recv(4096)
        server_socket.close()
        
        CONSOLE.debug("Received response from server: {}".format(response))

        client_socket.sendall(response)
        client_socket.close()

    def listen(self):
        """Starts listening for incoming client connections."""
        super().listen()

        CONSOLE.log(f"HTTP Proxy listening on {self.host}:{self.port}")

        while True:
            try:
                client_socket, client_address = self.accept()
                CONSOLE.info(f"Connection from {client_address}")
                self.handle_client(client_socket, client_address)
            except OSError as e:
                CONSOLE.error(f"[ERROR] {e}")
