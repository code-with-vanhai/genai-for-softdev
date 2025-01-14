#Remember to install numpy using pip install numpy
import numpy as np

def add_arrays(array1, array2):
    """
    Adds two NumPy arrays element-wise.

    Parameters:
    array1 (numpy.ndarray): The first array.
    array2 (numpy.ndarray): The second array.

    Returns:
    numpy.ndarray: The element-wise sum of the two arrays.
    """
    return np.add(array1, array2)

# Example usage
if __name__ == "__main__":
    # Define two arrays
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    
    # Add the arrays
    result = add_arrays(arr1, arr2)
    
    print("Array 1:", arr1)
    print("Array 2:", arr2)
    print("Result (Sum):", result)
