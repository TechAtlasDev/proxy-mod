from abc import ABC, abstractmethod
from typing import Any, Tuple
from proxy_mod.core.server import Server

class BaseProxy(Server, ABC):
    """
    Abstract base class for a proxy server.
    
    This class extends BaseServer and defines the core functionality that any
    proxy implementation should have.
    """
    
    @abstractmethod
    def handle_client(self, client_socket: Any, client_address: Tuple[str, int]) -> None:
        """
        Handles an incoming client connection.
        
        Args:
            client_socket (Any): The socket object representing the client connection.
            client_address (Tuple[str, int]): The address (IP, port) of the client.
        """
        pass
    
    @abstractmethod
    def forward_request(self, data: bytes) -> bytes:
        """
        Forwards the client's request to the target server.
        
        Args:
            data (bytes): The raw request data received from the client.
        
        Returns:
            bytes: The response received from the target server.
        """
        pass
    
    @abstractmethod
    def modify_response(self, response: bytes) -> bytes:
        """
        Modifies the response before sending it back to the client.
        
        Args:
            response (bytes): The raw response data from the target server.
        
        Returns:
            bytes: The modified response data.
        """
        pass
