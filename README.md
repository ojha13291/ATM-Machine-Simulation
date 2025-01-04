# ATM Machine Simulation

This repository contains a Python program that simulates the basic functions of an ATM machine. The functionalities include account balance inquiry, cash withdrawal, cash deposit, PIN change, and transaction history.

## Features

- **Account Balance Inquiry**: Check the current balance of the account.
- **Cash Withdrawal**: Withdraw a specified amount of money from the account.
- **Cash Deposit**: Deposit a specified amount of money into the account.
- **PIN Change**: Change the PIN of the account.
- **Transaction History**: View the history of all transactions performed.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ojha13291/ATM-Machine-Simulation.git
    cd ATM-Machine-Simulation
    ```

2. **Ensure you have Python installed** (Python 3.6+ recommended). You can download it from [python.org](https://www.python.org/).

## Usage

To run the ATM simulation, simply execute the `main.py` file:

```sh
python main.py
```


##Example Interaction

1. **Start the ATM Simulation**:

```sh
python main.py
```

2.**ATM Menu**:

--- ATM Menu ---
1: Balance Inquiry
2: Deposit Cash
3: Withdraw Cash
4: Change PIN
5: Transaction History
6: Exit
----------------


3.**Choose an option by entering the corresponding number**.


##Code Overview

**ATM Class**

The ATM class handles all the functionalities of the ATM machine.

1.**Initialization**: Sets the initial balance, PIN, and transaction history.
2.**Balance Inquiry**: Displays the current account balance.
3.**Cash Deposit**: Deposits a specified amount into the account.
4.**Cash Withdrawal**: Withdraws a specified amount from the account if sufficient balance is available.
5.**PIN Change**: Changes the PIN of the account if the old PIN is correct.
6.**Transaction History**: Displays the transaction history.

**Main Function**
The main() function provides a menu for the user to interact with the ATM and calls the appropriate methods based on the user's choice.


##Contribution
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

##License
This project is licensed under the MIT License. See the LICENSE file for details.

##Octanet Internship
This project is part of the Octanet internship for the Python development role. The purpose of this task is to demonstrate the ability to implement basic functionalities of an ATM machine using Python, ensuring the code is well-documented and user-friendly.

