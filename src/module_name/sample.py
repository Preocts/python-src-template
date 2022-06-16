"""This is just a sample file"""


def main() -> bool:
    """Main"""
    print("The squared of 2 is", squared(2))
    return True


def squared(value: int) -> int:
    """Returns the squared value"""
    return value * value
