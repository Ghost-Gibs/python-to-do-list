class InsufficientFundsError(Exception):
    """Custom exception raised when withdrawal exceeds account balance."""
    pass

def withdraw(balance, amount):
    """
    Simulates an ATM withdrawal process.

    Args:
        balance (float): The current account balance.
        amount (float): The amount to withdraw.

    Returns:
        float: The remaining balance after withdrawal.

    Raises:
        TypeError: If the amount is not a number.
        ValueError: If the amount is negative.
        InsufficientFundsError: If the withdrawal exceeds the account balance.
    """
    try:
        amount = float(amount)
    except ValueError:
        raise TypeError("Invalid input. Please enter a numeric value for the withdrawal amount.")

    if amount <= 0:
        raise ValueError("Invalid input. Please enter a positive value for the withdrawal amount.")

    if amount > balance:
        raise InsufficientFundsError("Insufficient funds. Withdrawal amount exceeds account balance.")

    balance -= amount
    return balance

def main():
    balance = 1000  # Initial account balance
    while True:
        try:
            amount = input("Enter the amount to withdraw (or 'quit' to exit): ")
            if amount.lower() == 'quit':
                break
            new_balance = withdraw(balance, amount)
            print(f"Withdrawal successful. Remaining balance: ${new_balance:.2f}")
            balance = new_balance
        except (TypeError, ValueError, InsufficientFundsError) as e:
            print(f"Error: {e}")
        finally:
            print(f"Current balance: ${balance:.2f}")  # Display balance even if error occurs

if __name__ == "__main__":
    main()