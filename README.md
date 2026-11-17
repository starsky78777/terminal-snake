# 🐍 Terminal Snake TUI (Python / POSIX Curses)

An interactive, object-oriented implementation of the classic Snake game built directly for the terminal using Python and POSIX `curses` libraries. Designed to showcase terminal buffer manipulation, event-driven loops, and clean systems programming practices.

---

## 🚀 Features

* **Object-Oriented Architecture (`OOP`):** Refactored from flat procedural scripts into a clean, modular Python class structure.
* **POSIX Curses Integration:** Directly interfaces with terminal screen buffers (`curses`), handling raw key inputs, window resizing safety, and cursor states.
* **WASD Controls:** Responsive directional controls with built-in collision prevention to avoid accidental instant self-collisions.
* **Dynamic Speed Scaling:** The game loop dynamically increases speed as your score increases.

---

## ⚙️ Prerequisites & System Requirements

This project runs on any Unix-like operating system (Linux, macOS, or WSL for Windows) with **Python 3** installed.

---

## 🛠️ Installation & Quick Start

Clone the repository and set up the project locally via your terminal:

```bash
# 1. Clone the repository
git clone git@github.com:starsky78777/terminal-snake.git
cd terminal-snake

# 2. Create and activate a Python virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Run the game
python3 src/game.py
