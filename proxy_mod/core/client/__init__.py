from proxy_mod.utils import vars
from proxy_mod.utils.console import Console
import socket

class Client:
  def __init__(self, host:str, port:int):
    self.host = host
    self.port = port
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.connect((self.host, self.port))