from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple

class Entity(ABC):
  def __init__(self, host:str, port:int):
    self.host = host
    self.port = port

  @abstractmethod
  def close(self) -> bool:
    pass