using System;

class Program
{
    // Method to add two numbers
    static int AddNumbers(int a, int b)
    {
        return a + b;
    }

    static void Main(string[] args)
    {
        // Get input from the user
        Console.Write("Enter the first number: ");
        int num1 = int.Parse(Console.ReadLine());

        Console.Write("Enter the second number: ");
        int num2 = int.Parse(Console.ReadLine());

        // Call the AddNumbers method
        int result = AddNumbers(num1, num2);

        // Display the result
        Console.WriteLine($"The sum of {num1} and {num2} is: {result}");
    }
}
