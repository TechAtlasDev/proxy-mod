import socket
from ..utils.console import Console
from ..utils import vars

env = vars.ServerEnv()
HOST = env.HOST
PORT = env.PORT

CONSOLA = Console(DEBUG=env.DEBUG)

def main():
  CONSOLA.info("Starting client...")
  CONSOLA.debug(f"Host: {HOST}")
  CONSOLA.debug(f"Port: {PORT}")

  CONSOLA.info("Creating socket...")
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  CONSOLA.info("Socket created")
  client.connect((HOST, PORT))
  CONSOLA.info("Socket connected")

  CONSOLA.info("Sending data...")
  client.sendall(b'Hello, world')

  CONSOLA.info("Receiving data...")
  data = client.recv(1024)
  CONSOLA.log(f"Received: {data}")

  CONSOLA.warning("Closing connection...")
  client.close()
  CONSOLA.success("Connection closed")