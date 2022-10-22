import random

def random_ints(n, a, b):
    """Return a list of n random integers between a and b, inclusive."""
    return [random.randint(a, b) for _ in range(n)]
