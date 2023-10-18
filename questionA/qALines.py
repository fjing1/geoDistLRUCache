from typing import Tuple

def do_lines_overlap(line1: Tuple[int, int], line2: Tuple[int, int]) -> bool:
    """Check if two lines on the x-axis overlap.

    :param line1: A tuple representing the first line with two integers.
    :param line2: A tuple representing the second line with two integers.
    :return: True if the lines overlap, otherwise False.
    """

    return max(line1) > min(line2) and max(line2) > min(line1)

# Test the function
print(do_lines_overlap((1, 5), (2, 6)))  # Expected output: True
print(do_lines_overlap((1, 5), (1, 5)))  # Expected output: True
print(do_lines_overlap((1, 5), (6, 8)))  # Expected output: False
# Edge cases
print(do_lines_overlap((1, 5), (5, 8)))  # Expected output: False
print(do_lines_overlap((2, 1), (0, 1)))  # Expected output: False

