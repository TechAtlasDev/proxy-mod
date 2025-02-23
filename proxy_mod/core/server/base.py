from abc import ABC, abstractmethod
from proxy_mod.core.abs.entity import Entity
from typing import Any, Tuple

class BaseServer(Entity, ABC):
    """
    Base abstract class for a server.

    This class defines the fundamental methods that any server implementation must have.
    It extends `Entity` and enforces required functionalities through abstract methods.

    Attributes:
        host (str): The hostname or IP address where the server will be running.
        port (int): The port number on which the server will listen for connections.
    """

    def __init__(self, host: str = "localhost", port: int = 4440):
        """
        Initializes the BaseServer with a specific host and port.

        Args:
            host (str, optional): The hostname or IP address. Defaults to "localhost".
            port (int, optional): The port number. Defaults to 4440.
        """
        super().__init__(host, port)

    @abstractmethod
    def listen(self) -> None:
        """
        Starts listening for incoming connections.

        This method should configure the server to accept new client connections.
        """
        pass

    @abstractmethod
    def accept(self) -> Tuple[Any, Any]:
        """
        Accepts an incoming client connection.

        Returns:
            Tuple[Any, Any]: A tuple containing the client socket and address.
        """
        pass

    @abstractmethod
    def send(self, data: Any) -> bool:
        """
        Sends data to a connected client.

        Args:
            data (Any): The data to send.

        Returns:
            bool: True if the data was sent successfully, False otherwise.
        """
        pass

    @abstractmethod
    def receive(self) -> str:
        """
        Receives data from a connected client.

        Returns:
            str: The received data as a string.
        """
        pass

    @abstractmethod
    def close(self) -> bool:
        """
        Closes the server and releases resources.

        Returns:
            bool: True if the server was closed successfully, False otherwise.
        """
        pass

    @abstractmethod
    def reboot(self) -> bool:
        """
        Restarts the server.

        This method should handle stopping the server and restarting it with the same settings.

        Returns:
            bool: True if the server was restarted successfully, False otherwise.
        """
        pass
