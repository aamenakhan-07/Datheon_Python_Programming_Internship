Datheon Python Programming Internship

Welcome to my Python Programming Internship project repository. This repository contains the tasks completed as part of the Datheon Python Programming Internship.

Task 1: Hangman Game

Description

Hangman is a word-guessing game in which the player attempts to guess a hidden word one letter at a time.

Features

- Random word selection
- Letter-by-letter guessing
- Tracks incorrect guesses
- Displays the progress of the game
- Uses a separate word list file

Files

- "hangman.py" — Main Python game
- "words.txt" — Contains words used in the game

How to Run

python hangman.py

---

Task 2: Stock Portfolio Performance Tracker

Description

The Stock Portfolio Performance Tracker is a Python program that calculates the performance of stock holdings using purchase prices, share quantities, and online stock price data.

Features

- Accepts stock ticker symbols such as AAPL, MSFT, and GOOGL
- Takes purchase price and quantity from the user
- Fetches available stock prices online
- Calculates total invested amount and current market value
- Calculates gain or loss for each holding
- Calculates percentage return
- Generates a CSV report containing portfolio results

Files

- "portfolio.py" — Main stock portfolio tracker program
- "portfolio_summary.csv" — Generated portfolio performance report

How to Run

Make sure Python and an internet connection are available.

python portfolio.py

Enter the ticker symbol, purchase price per share, and number of shares when prompted. Enter "DONE" to finish adding stocks.

Output

The program displays the portfolio summary and saves the results to "portfolio_summary.csv".

Note: Online prices depend on data availability and may be delayed. The CSV report is overwritten with a new report when the program runs successfully.

---

Technologies Used

- Python
- CSV file handling
- JSON
- URL requests
- Date and time handling

Learning Outcomes

- Practiced Python programming and user input handling
- Learned to work with dictionaries and loops
- Performed calculations using financial data
- Retrieved online data using HTTP requests
- Saved structured data to CSV files

This repository demonstrates the implementation of Python programming tasks, problem-solving skills, data handling, and basic application development.

Task 4: Rule-Based Interactive Terminal Chatbot

Description

This project is a rule-based interactive chatbot developed using Python. It helps users find answers to frequently asked questions related to internship support, business hours, project submission, and certificates.

Features

- Interactive terminal-based conversation.
- Greeting detection for messages such as "hello", "hi", and "hey".
- FAQ responses loaded from a JSON dataset.
- Regex-based keyword matching and multi-intent recognition.
- Fallback responses for unrecognized queries.
- Exit commands: "bye", "exit", and "quit".
- Error handling for missing or invalid JSON data.

Project Files

- "chatbot.py" — Main chatbot program.
- "sample_faq.json" — Contains greeting keywords and FAQ questions with answers.

Technologies Used

- Python 3
- "json" — Loading FAQ data.
- "re" — Regular expressions and keyword matching.
- "pathlib" — Accessing the dataset file.

How to Run

1. Keep "chatbot.py" and "sample_faq.json" in the same folder.
2. Open "chatbot.py" in Python or Pydroid 3.
3. Run the program.
4. Ask questions about business hours, internship project submission, or certificates.
5. Type "bye", "exit", or "quit" to end the conversation.

Learning Outcomes

- Understanding rule-based chatbot development.
- Working with JSON datasets.
- Using regular expressions for text matching.
- Implementing error handling and conversational flow.

Author

Python Programming Internship Participant

Repository Purpose
