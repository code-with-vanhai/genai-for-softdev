/**
 * This class provides an implementation of the Bubble Sort algorithm.
 * Bubble Sort is a simple sorting algorithm that repeatedly steps through 
 * the list, compares adjacent elements, and swaps them if they are in the wrong order.
 * The pass-through is repeated until the array is sorted.
 *
 * <p>Time Complexity:
 * - Best Case (already sorted): O(n)
 * - Worst Case (reversed order): O(n^2)
 * - Average Case: O(n^2)
 *
 * <p>Space Complexity: O(1) (in-place sorting)
 */
public class BubbleSort {

    /**
     * Sorts the given integer array in ascending order using the Bubble Sort algorithm.
     * 
     * @param arr the array to be sorted
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    /**
     * The main method to demonstrate Bubble Sort.
     * It initializes an array, sorts it, and prints the sorted output.
     *
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        bubbleSort(arr);
        System.out.println("Sorted array is:");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
