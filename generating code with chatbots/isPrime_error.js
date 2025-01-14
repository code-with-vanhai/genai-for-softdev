function isPrime(number) {
    // Error handling: Check if the input is a positive integer
    if (typeof number !== "number" || !Number.isInteger(number)) {
        return "Error: Input must be an integer.";
    }
    if (number <= 0) {
        return "Error: Input must be a positive integer.";
    }

    // Handle edge cases
    if (number === 1) {
        return false; // 1 is not a prime number
    }
    if (number <= 3) {
        return true; // 2 and 3 are prime numbers
    }
    if (number % 2 === 0 || number % 3 === 0) {
        return false;
    }

    // Check divisors from 5 to the square root of the number
    for (let i = 5; i * i <= number; i += 6) {
        if (number % i === 0 || number % (i + 2) === 0) {
            return false;
        }
    }

    return true;
}

// Example usage
const inputs = [29, 1.5, -7, 0, "string", 17];

inputs.forEach((input) => {
    console.log(`Input: ${input} => Result: ${isPrime(input)}`);
});
