# Number Baseball Game

## Game Description

Number Baseball is a guessing game where:

- The computer generates a secret 3-digit number(0-9) with no repeated digits.
- The player tries to guess this number.
- After each guess, the computer provides feedback:
  - **Strike**: Correct digit in the correct position
  - **Ball**: Correct digit in the wrong position

The goal is to guess the secret number in as few attempts as possible.

## File Description

- `number_baseball.py`: Contains all game logic including number generation, user input handling, score calculation, and gameplay.

## Functions

- `generate_numbers()`: Generates the secret 3-digit number.
- `take_guess()`: Handles user input for guessing.
- `get_score(guess, answer)`: Calculates the number of strikes and balls.
- `main()`: Runs the main game loop.

## Usage as a Module

This script can also be imported as a module. The game will only run if the script is executed directly, not when imported.
