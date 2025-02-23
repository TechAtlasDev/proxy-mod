from .base import BaseServer
from proxy_mod.utils import vars
from proxy_mod.utils.console import Console
import socket

# ---- SETUP ----
ENV = vars.ServerEnv()
CONSOLE = Console(DEBUG=ENV.DEBUG)

# ---- SERVER ----
class Server(BaseServer):
    def __init__(self, host=None, port=None):
        host = host if host else ENV.HOST
        port = port if port else ENV.PORT
        super().__init__(host, port)

        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.SOCKET.bind((self.host, self.port))
        except OSError as e:
            CONSOLE.error(f"Error binding to {self.host}:{self.port} - {e}")
            raise SystemExit(1)

        CONSOLE.debug(f"Server created with host={self.host} and port={self.port}")

    # ---- METHODS ----
    def listen(self):
        self.SOCKET.listen(ENV.MAX_CONNECTIONS)
        CONSOLE.info(f"Server is listening on {self.host}:{self.port}")

    def accept(self):
        CONSOLE.debug("Server is accepting connections")
        return self.SOCKET.accept()

    def send(self, client_socket, data: bytes):
        try:
            client_socket.sendall(data)
            CONSOLE.debug(f"Sent data: {data}")
            return True
        except Exception as e:
            CONSOLE.error(f"Error sending data: {e}")
            return False

    def receive(self, client_socket):
        try:
            data = client_socket.recv(ENV.BUFFER_SIZE).decode()
            CONSOLE.debug(f"Received data: {data}")
            return data
        except Exception as e:
            CONSOLE.error(f"Error receiving data: {e}")
            return None

    def close(self):
        CONSOLE.debug("Closing server")
        self.SOCKET.close()
        return True

    def reboot(self):
        CONSOLE.debug("Rebooting server")
        self.close()
        return Server(self.host, self.port)

    # ---- CONTEXT MANAGER ----
    def __enter__(self):
        self.listen()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
