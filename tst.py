import random

def generate_random_list(length, min_value, max_value):
    """
    Generate a random list of integers.

    Parameters:
    - length: The length of the list to generate.
    - min_value: The minimum possible value for elements in the list.
    - max_value: The maximum possible value for elements in the list.

    Returns:
    - A list of random integers.
    """
    return [random.randint(min_value, max_value) for _ in range(length)]

# Example usage:
random_list = generate_random_list(10, 1, 100)
print("Random list:", random_list)
