def calculate_square(number):
    """
    Calculates the square of a given number.

    Parameters:
    number (float or int): The number to square.

    Returns:
    float or int: The square of the input number.
    """
    return number ** 2

# Example usage
if __name__ == "__main__":
    num = 5
    result = calculate_square(num)
    print(f"The square of {num} is: {result}")
