# Rock-Paper-Scissors Game



---

##  Features

-   **User-friendly Interface**: Clean text-based interaction with clear and simple prompts.
-   **Input Validation**: Ensures that only valid choices (`rock`, `paper`, `scissors`) are accepted from the user.
-   **Score Tracking**: Keeps a running score of wins for both the player and the computer.
-   **Randomized Computer Choices**: Uses Python's `random` module for fair and unpredictable gameplay.
-   **Play Again Option**: Allows for multiple rounds of play without needing to restart the program.

##  How to Play

1.  Run the Python script from your terminal.
2.  When prompted, type your choice: `rock`, `paper`, or `scissors`.
3.  The computer will make its random selection.
4.  The winner is determined based on the classic rules:
    -   🗿 Rock beats ✂️ Scissors
    -   ✂️ Scissors beats 📄 Paper
    -   📄 Paper beats 🗿 Rock
5.  Scores are displayed at the end of each round.
6.  You will be given the option to play another round or exit the game.

##  Installation & Usage

1.  Ensure you have **Python 3.x** installed on your system.
2.  Download or clone the repository to your local machine.
3.  Navigate to the project directory in your terminal.
4.  Run the game using the following command:
    ```bash
    python rock_paper_scissors.py
    ```

##  Code Structure

The program is organized into three main functions to ensure modularity and readability:

-   `get_user_choice()`: Handles all user input and includes a loop for validation.
-   `determine_winner()`: Implements the core game logic to decide the winner of each round.
-   `main()`: Controls the main game flow, manages the scoring system, and handles the "play again" loop.

### Technical Highlights

This project serves as a clear demonstration of core Python concepts, including:

-   Functions and modular programming
-   Conditional statements (`if`/`elif`/`else`)
-   Looping structures (`while`)
-   List manipulation
-   Random number generation
-   String operations and methods
-   User input and validation

##  Future Enhancements

Potential improvements and future additions for this project include:

-   Implementing a **Graphical User Interface (GUI)** using a library like Tkinter or Pygame.
-   Adding **multiplayer functionality** over a local network.
-   Creating a **tournament mode** with a "best of X" rounds system.
-   Expanding the game with additional gestures, such as the **Rock-Paper-Scissors-Lizard-Spock** variant.
