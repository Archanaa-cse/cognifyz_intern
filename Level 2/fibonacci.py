def generate_fibonacci_sequence(n_terms):
    if n_terms <= 0:
        return "Please enter a positive integer."
    elif n_terms == 1:
        return [0]
    elif n_terms == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for _ in range(2, n_terms):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    try:
        n_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        fibonacci_sequence = generate_fibonacci_sequence(n_terms)
        print(f"Fibonacci sequence with {n_terms} terms: {fibonacci_sequence}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
