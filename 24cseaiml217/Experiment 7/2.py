def find_primes_in_range(start, end):
    """
    Generates all prime numbers within the specified start and end range.
    """
    # Ensure start is at least 2, as numbers less than 2 are not prime
    if start < 2:
        start = 2
        
    print(f"Prime numbers between {start} and {end} are:")

    for num in range(start, end + 1):
        # All prime numbers are greater than 1
        if num > 1:
            # Check for factors from 2 up to the square root of the number
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    # If a factor is found, it is not a prime number
                    is_prime = False
                    break
            if is_prime:
                print(num, end=' ')
    print() # For a final newline


if __name__ == "__main__":
    try:
        # Prompt the user for input
        start_str, end_str = input("Enter the start and end values of the range (e.g., 10 50): ").split()
        
        # Convert inputs to integers
        start = int(start_str)
        end = int(end_str)
        
        # Call the function to find and print primes
        find_primes_in_range(start, end)
        
    except ValueError:
        print("Invalid input. Please enter two valid integer numbers separated by a space.")

