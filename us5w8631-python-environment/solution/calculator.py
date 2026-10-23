"""Basic calculator functions."""


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
    """Return a divided by b, or None if b is zero."""
    if b == 0:
        return None
    return a / b


def main():
    """Run a quick example of the calculator."""
    result = divide(10, 0)
    if result is None:
        print("Cannot divide by zero")
    print(add(2, 3), subtract(5, 1), multiply(4, 2), divide(9, 3))


if __name__ == "__main__":
    main()
