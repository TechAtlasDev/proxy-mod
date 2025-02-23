from .core.proxy.http import HttpProxy

def main():
    proxy = HttpProxy()
    proxy.listen()