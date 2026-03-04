# Simple Python Example

def greet(name):
    return f"Hello, {name}!"

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    # Greeting
    name = input("Enter your name: ")
    print(greet(name))

    # Working with a list
    numbers = [10, 20, 30, 40, 50]
    print("Numbers:", numbers)

    # Loop example
    print("Squared numbers:")
    for num in numbers:
        print(num, "->", num ** 2)

    # Function example
    average = calculate_average(numbers)
    print("Average:", average)

if __name__ == "__main__":
    main()
