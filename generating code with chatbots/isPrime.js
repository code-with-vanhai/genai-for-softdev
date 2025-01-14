function isPrime(number) {
    // Handle edge cases
    if (number <= 1) {
        return false;
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
const num = 29;
console.log(`${num} is prime: ${isPrime(num)}`);
