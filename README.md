# 🎮 Python Hangman Game

A classic word-guessing game with a programming twist! Part of the CodeAlpha internship program.

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## 🎯 Game Features

- 📚 Programming-themed word bank
- 🎨 ASCII art visualization
- 📝 Letter tracking system
- 🔄 Play again functionality
- 🖥️ Clear screen for better UI
- ⌨️ Input validation
- 📊 Remaining tries counter

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- A terminal/command prompt

### Installation
1. Clone the repository
```bash
git clone https://github.com/mohamed682004/CodeAlpha_Hangman_Game.git
cd CodeAlpha_Hangman_Game
```

2. Run the game
```bash
python hangman.py
```

## 🎮 How to Play

1. The game will select a random programming-related word
2. Guess one letter at a time by typing it and pressing Enter
3. You have 6 lives (wrong guesses) before the game ends
4. Correct guesses reveal the letter's position in the word
5. Win by guessing all letters in the word before running out of lives!

## 🎯 Game Controls
- Enter a single letter to make a guess
- Type 'Y' to play again after a game ends
- Type 'N' to exit after a game ends

## 🖼️ Game Preview
```
   --------
   |      |
   |      O
   |     \|/
   |      |
   |     / \
   -
   
Current word: P Y T H _ N
Used letters: A E I N P T Y
```

## 📋 Project Structure
```
CodeAlpha_Hangman_Game/
├── hangman.py          # Main game file
└── README.md          # Project documentation
```

## 🛠️ Technical Details
- Written in Python 3
- Uses built-in libraries:
  - `random` for word selection
  - `os` for screen clearing

## 🤝 Contributing
Feel free to fork this project and enhance it. Some ideas for improvements:
- Add more words to the word bank
- Implement difficulty levels
- Add sound effects
- Create a graphical user interface
- Add scoring system

## 📝 Author
**Mohamed Ahmed Mohamed Hossen**
- GitHub: [@mohamed682004](https://github.com/mohamed682004)
- Project Link: [CodeAlpha_Hangman_Game](https://github.com/mohamed682004/CodeAlpha_Hangman_Game)

## 🎓 Acknowledgments
- Created as part of the CodeAlpha Internship Program
- Special thanks to CodeAlpha for the project opportunity

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
