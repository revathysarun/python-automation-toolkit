##Python Automation Toolkit

A beginner-friendly collection of Python scripts built to apply introductory computer science concepts through small but complete programs. This repository focuses on automation, problem-solving, and clear program structure rather than production-level software.
This project was developed alongside my coursework in Introduction to Computer Programming and through self-driven practice.

##Overview

The repository contains independent Python scripts, each solving a well-defined problem. Together, they demonstrate core ideas such as control flow, functions, input validation, file handling, and basic algorithmic reasoning.

##Modules
1. Tic-Tac-Toe Game (Player vs AI)
- Console-based Tic-Tac-Toe game where the user plays against a simple AI
- Implements board representation, win-condition checking, and turn-based logic
- AI uses rule-based decision making to attempt winning moves, block the player, or choose a random valid move


Concepts demonstrated:
- Lists and indexing
- Functions and modular design
- Conditional logic and loops
- Basic algorithmic reasoning
- Input validation and error handling

2. Certificate Generator
- Automatically generates personalized certificates using participant data
- Reads names and certificate IDs from an Excel file
- Writes text onto a certificate template image
- Generates and embeds a QR code for each certificate


Technologies used:
- pandas for reading structured data
- PIL (Pillow) for image processing and text placement
- qrcode for QR code generation


Concepts demonstrated:
- File input/output
- Iterating over structured data
- Automation of repetitive tasks
- Use of external Python libraries

3. Password Generator
- Generates random passwords using letters, digits, and selected symbols
- Enforces a minimum password length
- Accepts user input from the command line


Concepts demonstrated:
- Strings and string operations
- Randomization
- Functions and loops
- Basic input validation

##How to Run
1. Ensure Python 3 is installed
2. Install required libraries for the certificate generator:
pip install pandas pillow qrcode

