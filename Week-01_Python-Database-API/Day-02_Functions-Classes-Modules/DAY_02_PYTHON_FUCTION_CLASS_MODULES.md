# Day 2 — Functions, Classes & Modules

## Learning Resource

I learned Python Functions, Classes, and Modules through practical coding and hands-on exercises.

## Topics Learned

* Functions
* Function Definition and Calling
* Function Parameters and Arguments
* Return Values
* Classes
* Objects
* Modules
* Importing Modules
* Module Aliases using `as`
* Python `random` Module

## Practical Work

* Practiced creating and calling Python functions.
* Practiced function parameters, arguments, and return values.
* Practiced basic classes and objects.
* Created and imported custom Python modules.
* Practiced using module aliases with the `as` keyword.
* Used the `random` module to generate random numbers.
* Built a simple CLI-based Number Guessing Game.

## Utility Project

### Number Guessing Game

A simple command-line game where the computer generates a random number between 1 and 100, and the user tries to guess the number.

### Features

* Generates a random number between 1 and 100.
* Takes the user's guess as input.
* Provides **Too High** and **Too Low** hints.
* Counts the number of attempts.
* Displays a success message when the correct number is guessed.

### Module Usage

The game functionality is written in a separate Python module and imported into the main program using an alias.

```python
import GameModule as game

game.numbergame()
```

## Project Structure

```text
Day-02_Functions-Classes-Modules/
│
├── README.md
│
├── Python-Functions-Practice/
│
├── Python-Classes-Practice/
│
├── Python-Modules-Practice/
│
└── Utility-Project/
    │
    └── NumberGuessingGame/
        ├── GameModule.py
        └── number_guessing.py
```

## Timeline

**18-08-2026:** Learned and practiced Functions, Classes, and Modules.

**19-08-2026:** Completed the Number Guessing Game utility project.

## Status

**Day 2 — Completed** ✅
