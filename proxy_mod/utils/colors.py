from enum import Enum

class Colors(Enum):
  BLACK = '\033[30m'
  RED = '\033[31m'
  GREEN = '\033[32m'
  YELLOW = '\033[33m'
  BLUE = '\033[34m'
  MAGENTA = '\033[35m'
  CYAN = '\033[36m'
  WHITE = '\033[37m'
  RESET = '\033[0m'
  BRIGHT_BLACK = '\033[90m'
  BRIGHT_RED = '\033[91m'
  BRIGHT_GREEN = '\033[92m'
  BRIGHT_YELLOW = '\033[93m'
  BRIGHT_BLUE = '\033[94m'
  BRIGHT_MAGENTA = '\033[95m'
  BRIGHT_CYAN = '\033[96m'
  BRIGHT_WHITE = '\033[97m'

# Example usage
if __name__ == "__main__":
  print(f"{Colors.RED.value}This is red text{Colors.RESET.value}")
  print(f"{Colors.GREEN.value}This is green text{Colors.RESET.value}")
  print(f"{Colors.BLUE.value}This is blue text{Colors.RESET.value}")