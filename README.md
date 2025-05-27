# Calculator Module
&nbsp;
&nbsp;

This is a simple command-line calculator that allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division. The calculator prompts the user to select an operation and input two numbers, then it displays the result.
&nbsp;
&nbsp;

## Features
&nbsp;
&nbsp;

- **Addition**: Computes the sum of two numbers.
- **Subtraction**: Computes the difference between two numbers.
- **Multiplication**: Computes the product of two numbers.
- **Division**: Computes the quotient of two numbers, with error handling for division by zero.
&nbsp;
&nbsp;

## Installation
&nbsp;
&nbsp;

To use this calculator, simply clone the repository or download the script. Ensure you have Python installed on your machine.
&nbsp;
&nbsp;

## Usage
&nbsp;
&nbsp;

1. Run the script in your terminal or command prompt.
2. Follow the on-screen prompts to select an operation and enter the numbers.
3. The result will be displayed immediately after the operation.
&nbsp;
&nbsp;

## Code Overview
&nbsp;
&nbsp;

### Functions
&nbsp;
&nbsp;

- **sum()**: Prompts the user for two numbers and prints their sum.
- **sub()**: Prompts the user for two numbers and prints their difference.
- **mult()**: Prompts the user for two numbers and prints their product.
- **div()**: Prompts the user for two numbers and prints their quotient, with a check to prevent division by zero.
&nbsp;
&nbsp;

### Main Functionality
&nbsp;
&nbsp;

The `main()` function provides a loop that:
- Displays a welcome message and available operations.
- Prompts the user to select an operation.
- Calls the corresponding function based on user input.
- Handles invalid selections and exceptions gracefully.
&nbsp;
&nbsp;

### Example
&nbsp;
&nbsp;

```python
Welcome to calculator!
1. Sum
2. sub
3. mult
4. div
Please, select operation >> 1
Enter the first number >> 5
Enter the second number >> 3
8
