"""Simple calculator with basic arithmetic operations."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raise ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main():
    """Run a few example calculations."""
    print(f"2 + 3 = {add(2, 3)}")
    print(f"7 - 4 = {subtract(7, 4)}")
    print(f"3 * 5 = {multiply(3, 5)}")
    print(f"10 / 4 = {divide(10, 4)}")
    try:
        divide(10, 0)
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
