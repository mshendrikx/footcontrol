import random

def get_distinct_numbers_random(start, end):
    """Generates a list of distinct numbers between start and end in random order.

    Args:
        start: The starting number.
        end: The ending number.

    Returns:
        A list of distinct numbers in random order.
    """

    num_set = set(range(start, end + 1))
    random_numbers = random.sample(num_set, len(num_set))
    return random_numbers

# Example usage:
start_num = 1
end_num = 3
distinct_numbers = get_distinct_numbers_random(start_num, end_num)
print(distinct_numbers)