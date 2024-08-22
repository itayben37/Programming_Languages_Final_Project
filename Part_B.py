from functools import reduce


# 1. Fibonacci Sequence Generator
def fibonacci_sequence(n):
    fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])[:n]
    print(f"First {n} Fibonacci numbers: {fibonacci(n)}")


# 2. Concatenate Strings with a Space (Without 'join')
def concat_with_space(lst):
    return reduce(lambda x, y: x + ' ' + y, lst)


# 3. Cumulative Sum of Squares of Even Numbers in Sublists
def cumulative_sum_of_squares(lists):
    process_sublist = lambda sublist: (
        (lambda filter_evens: (
            (lambda square_evens: (
                (lambda sum_squares: (
                    (lambda total: total)(
                        sum_squares
                    )
                ))(
                    sum(square_evens)
                )
            ))(
                [x ** 2 for x in filter_evens]
            )
        ))(
            [x for x in sublist if x % 2 == 0]
        )
    )

    # Apply the nested lambda function to each sublist
    result = list(map(process_sublist, lists))
    return result


def cumulative_operation(op):
    """
    Higher-order function that takes a binary operation (as a lambda function)
    and returns a function that applies this operation cumulatively to a sequence.
    """
    def apply_cumulative(sequence):
        # Start with the first element of the sequence
        result = sequence[0]
        # Apply the operation cumulatively
        for element in sequence[1:]:
            result = op(result, element)
        return result
    return apply_cumulative

# Define the binary operation for multiplication
multiplication = lambda x, y: x * y

# Create the factorial function using cumulative_operation
factorial = cumulative_operation(multiplication)

# Factorial function that calculates the factorial of n
def factorial_function(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    # Create a sequence from 1 to n
    sequence = list(range(1, n + 1))
    return factorial(sequence)

# Define the binary operation for exponentiation
# Exponentiation operation is handled within the function itself
def exponentiation_function(base, exponent):
    if exponent < 0:
        raise ValueError("Exponentiation with negative exponents is not handled.")
    # Create a sequence with 'base' repeated 'exponent' times
    sequence = [base] * exponent
    # Use cumulative_operation with multiplication to perform exponentiation
    power = cumulative_operation(multiplication)
    return power(sequence)


# 5. Filter, Map, Reduce for Sum of Squares of Even Numbers
def sum_of_squares_of_evens():
    nums = [1, 2, 3, 4, 5, 6]
    sum_squared = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
    print(sum_squared)


# 6. Count Palindromes in Sublists
def count_palindromes_in_sublists(lists_of_strings):
    return list(map(lambda sublist: reduce(lambda count, s: count + (s == s[::-1]), sublist, 0), lists_of_strings))


# 7. Lazy Evaluation Explanation
def lazy_evaluation_explanation():
    print("In the context of your program, lazy evaluation refers to a process where values are computed only when they are\n"
          "actually needed, rather than being evaluated all at once. In your program, when using generate_values() within a\n"
          "list comprehension, values are generated and processed only as they are required, rather than being precomputed and stored\n"
          "in memory. This approach conserves memory and improves performance by deferring the computation of values until they are\n"
          "specifically needed.")

# 8. Filter and Sort Prime Numbers in Descending Order
def primes_descending(nums):
    return sorted([x for x in nums if (x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)))], reverse=True)
def q1():
    lambda: fibonacci_sequence(int(input("Enter the number of Fibonacci numbers to generate: ")))

def q2():
     print()

def q3():
    input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = cumulative_sum_of_squares(input_list)
    print(result)

def q4():
    print(factorial_function(5))  # Output: 120
    print(exponentiation_function(2, 3))

def q5():
    sum_of_squares_of_evens()

def q6():
    lists_of_strings = [["level", "world", "radar"], ["apple", "banana", "civic"], ["madam", "racecar"]]
    print(count_palindromes_in_sublists(lists_of_strings))

def q7():
    lazy_evaluation_explanation()

def q8():
    nums = [10, 15, 2, 7, 3, 11, 6]
    print(primes_descending(nums))

def main():
    options = {
        '1': q1,
        '2': q2,
        '3': q3,
        '4': q4,
        '5': q5,
        '6': q6,
        '7': q7,
        '8': q8
    }

    while True:
        print("\nChoose a question to run:")
        print("1. Fibonacci Sequence Generator")
        print("2. Concatenate Strings with a Space")
        print("3. Cumulative Sum of Squares of Even Numbers in Sublists")
        print("4. Higher-Order Function (Factorial and Exponentiation)")
        print("5. Sum of Squares of Even Numbers Using Filter, Map, Reduce")
        print("6. Count Palindromes in Sublists")
        print("7. Lazy Evaluation Explanation")
        print("8. Filter and Sort Prime Numbers in Descending Order")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == '9':
            break
        elif choice in options:
            options[choice]()
        else:
            print("Invalid choice, please try again.")


main()
