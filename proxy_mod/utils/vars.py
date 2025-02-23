from dotenv import DotEnv

DEBUG = False

class Env:
  def __init__(self, path_file=".env"):
    try:
      self.env = DotEnv(path_file)
    except FileNotFoundError:
      self.env = {}

  def get(self, key, default=None):
    return self.env.get(key, default)

class ClientEnv(Env):
  def __init__(self):
    super().__init__(".env.client")
    self.DEBUG = self.get("DEBUG", False)

    DEBUG = self.DEBUG

    self.HOST = self.get("HOST", "localhost")
    self.PORT = int(self.get("PORT", 8000))

class ServerEnv(Env):
  def __init__(self):
    super().__init__(".env.host")
    self.DEBUG = self.get("DEBUG", False)

    DEBUG = self.DEBUG

    self.HOST = self.get("HOST", "localhost")
    self.PORT = int(self.get("PORT", 8000))
    self.MAX_CONNECTIONS = int(self.get("MAX_CONNECTIONS", 5))
    self.BUFFER_SIZE = int(self.get("BUFFER_SIZE", 1024))