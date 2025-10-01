def square_numbers(numbers):
    """
    Squares each number in a list and returns a new list with the squared values.

    Args:
      numbers: A list of numbers.

    Returns:
      A new list containing the square of each number in the input list.
    """
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number ** 2)
    return squared_numbers

# Example usage:
list_of_numbers = [3, 99, 12, 1, 7]
squared_list = square_numbers(list_of_numbers)
print(squared_list)  # Output: [9, 9801, 144, 1, 49]