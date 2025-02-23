import logging
import sys
from datetime import datetime
from .colors import Colors

class Console:
    def __init__(self, **kwargs):
      self.context = kwargs
      if self.context.get("DEBUG"):
        self.DEBUG = self.context.get("DEBUG")
      else:
        from .vars import DEBUG
        self.DEBUG = DEBUG
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%H:%M:%S",
            level=logging.DEBUG if DEBUG else logging.INFO,
            handlers=[logging.StreamHandler(sys.stdout)]
        )
      self.logger = logging.getLogger("ProxyMod")

    def log(self, message: str):
        self._print("LOG", Colors.WHITE.value, message)
        self.logger.info(message)

    def info(self, message: str):
        self._print("INFO", Colors.BLUE.value, message)
        self.logger.info(message)

    def error(self, message: str):
        self._print("ERROR", Colors.RED.value, message)
        self.logger.error(message)

    def success(self, message: str):
        self._print("SUCCESS", Colors.GREEN.value, message)
        self.logger.info(message)

    def warning(self, message: str):
        self._print("WARNING", Colors.YELLOW.value, message)
        self.logger.warning(message)

    def debug(self, message: str):
        if self.debug:
            self._print("DEBUG", Colors.MAGENTA.value, message)
            self.logger.debug(message)

    def custom(self, type: str, color: str, message: str):
        self._print(type, color, message)
        self.logger.info(f"[{type}] {message}")

    def _print(self, type: str, color: str, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{color}[{Colors.RESET.value}{timestamp} {type}{color}]{Colors.RESET.value} {message}")
