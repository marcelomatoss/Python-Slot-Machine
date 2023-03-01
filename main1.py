import random


# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

SYMBOL_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def deposit() -> int:
    """Asks the user for the deposit amount and returns it."""
    while True:
        try:
            amount = int(input("What would you like to deposit? $"))
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a number.")


def get_number_of_lines() -> int:
    """Asks the user for the number of lines to bet on and returns it."""
    while True:
        try:
            lines = int(input(f"Enter the number of lines to bet on (1-{MAX_LINES})? "))
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Enter a valid number of lines (1-{MAX_LINES}).")
        except ValueError:
            print("Please enter a number.")


def get_bet() -> int:
    """Asks the user for the bet amount and returns it."""
    while True:
        try:
            amount = int(input(f"What would you like to bet on each line? (${MIN_BET}-{MAX_BET}) $"))
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        except ValueError:
            print("Please enter a number.")


def get_slot_machine_spin(rows: int, cols: int, symbols: dict) -> list:
    """Returns a randomly generated slot machine spin."""
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns: list) -> None:
    """Prints the slot machine spin in a readable format."""
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def check_winnings(columns: list, lines: int, bet: int, values: dict) -> tuple:
    """Checks the slot machine spin for winning lines and returns the winnings and winning lines."""
    winnings = 0
    winning_lines