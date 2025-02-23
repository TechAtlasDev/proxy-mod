import socket
from ..utils.console import Console
from ..utils import vars

env = vars.ServerEnv()
HOST = env.HOST
PORT = env.PORT

CONSOLA = Console(DEBUG=env.DEBUG)

def main():
  CONSOLA.info("Starting server...")
  CONSOLA.debug(f"Host: {HOST}")
  CONSOLA.debug(f"Port: {PORT}")

  CONSOLA.info("Creating socket...")
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  CONSOLA.info("Socket created")
  server.bind((HOST, PORT))
  CONSOLA.info("Socket binded")

  CONSOLA.info("Listening...")
  server.listen(1)
  conexion, direccion = server.accept()
  CONSOLA.info(f"Connected: {direccion}")
  conexion.recv(1024)
  CONSOLA.log("Sending data...")
  conexion.sendall(b'Hello, world')

  CONSOLA.warning("Closing connection...")
  server.close()
  conexion.close()
