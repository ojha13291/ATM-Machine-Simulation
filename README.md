# ATM Machine Simulation

This repository contains a Python program that simulates basic ATM machine functionalities such as balance inquiry, cash withdrawal, cash deposit, PIN change, and transaction history.

---

## Features

```markdown
- **Balance Inquiry**: Check the current account balance.
- **Cash Deposit**: Deposit money into the account.
- **Cash Withdrawal**: Withdraw money from the account (if balance permits).
- **PIN Change**: Update the account PIN securely.
- **Transaction History**: View a detailed history of all transactions.

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ATM-Machine-Simulation.git
    cd ATM-Machine-Simulation
    ```
2. Ensure Python 3.6+ is installed. Download it from [python.org](https://www.python.org/).

Run the program using:
```sh
python main.py

--- ATM Menu ---
1: Balance Inquiry
2: Deposit Cash
3: Withdraw Cash
4: Change PIN
5: Transaction History
6: Exit

---

## Code Overview

### ATM Class

```markdown
The `ATM` class manages all ATM functionalities:

- **Initialization**: Initializes balance, PIN, and transaction history.
- **Balance Inquiry**: Displays the current balance.
- **Cash Deposit**: Adds a specified amount to the balance.
- **Cash Withdrawal**: Deducts a specified amount from the balance (if sufficient).
- **PIN Change**: Updates the PIN securely after validation.
- **Transaction History**: Logs and displays all account activities.

The `main()` function serves as the entry point, presenting a menu for user interaction and invoking the appropriate methods of the `ATM` class.

Contributions are always welcome! Fork this repository and submit a pull request for any improvements or new features.

This project is licensed under the MIT License. See the `LICENSE` file for more details.

This project was developed as part of the **Octanet Internship** program under the Python development role. It demonstrates the implementation of basic ATM functionalities using Python while focusing on user-friendliness and clear documentation.
