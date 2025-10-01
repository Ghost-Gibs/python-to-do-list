# While Loop Practices - Python
# Practice different while loop patterns and scenarios

def main():
    print("Welcome to While Loop Practices!")
    print("=" * 40)
    
    # Basic while loop example
    print("\n1. Basic counting while loop:")
    count = 1
    while count <= 5:
        print(f"Count: {count}")
        count += 1
    
    # While loop with user input (commented for now)
    # print("\n2. User input example:")
    # user_input = ""
    # while user_input.lower() != "quit":
    #     user_input = input("Type 'quit' to exit: ")
    #     if user_input.lower() != "quit":
    #         print(f"You typed: {user_input}")
    
    # While loop with list processing
    print("\n3. Processing a list:")
    numbers = [10, 20, 30, 40, 50]
    index = 0
    while index < len(numbers):
        print(f"Number at index {index}: {numbers[index]}")
        index += 1
    
    # While loop with condition checking
    print("\n4. Finding a target value:")
    target = 30
    current = 0
    attempts = 0
    while current != target:
        current += 5
        attempts += 1
        print(f"Attempt {attempts}: current value = {current}")
    
    print(f"\nTarget {target} reached in {attempts} attempts!")

if __name__ == "__main__":
    main()

