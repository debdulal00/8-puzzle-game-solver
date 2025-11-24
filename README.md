# 🧩 8-Puzzle Game Solver  
A clean and optimized Python implementation of the classic **8-Puzzle Solver** using **A\*** (Manhattan Distance) and **BFS** algorithms.

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue" />
  <img src="https://img.shields.io/badge/Algorithms-A*%20%7C%20BFS-green" />
  <img src="https://img.shields.io/badge/CLI-Interactive-orange" />
</p>

---

## 🚀 Features
- ✔ **A\* Search (Manhattan Heuristic)** – fast and optimal  
- ✔ **BFS (Shortest Path)** – guaranteed minimal moves  
- ✔ **Solvability Check** – detects unsolvable puzzles  
- ✔ **Direction Tracking** (Up/Down/Left/Right)  
- ✔ **Step-by-step state visualization**  
- ✔ **Clean, modular, readable code**  
- ✔ Runs on any system with Python 3.8+

---

## 📸 Example Output

=== 8 Puzzle Game Solver (Optimized) ===
Goal state:
1 2 3
4 5 6
7 8 _

Enter 9 numbers (0=blank): 1 2 3 4 0 6 7 5 8

Choose Algorithm:

BFS

A* (Recommended)

Solved in 2 moves.

Move tile 5 (RIGHT)

Move tile 8 (UP)

Step 0:
1 2 3
4 _ 6
7 5 8

Step 1: move 5 (RIGHT)
1 2 3
4 5 6
7 _ 8


---

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/8-puzzle-game-solver
cd 8-puzzle-game-solver


Run the solver:

python eight_puzzle_solver.py


No external libraries required.

🎮 How to Use
👉 Input Format

Enter exactly 9 numbers separated by spaces.

Example:

1 2 3 4 0 6 7 5 8


Use 0 for the blank tile

Numbers must be 0–8 with no duplicates

🧠 Algorithms Used
🔹 BFS (Breadth-First Search)

Guarantees shortest solution

Can be slower for deep puzzles

🔹 A* Search (Manhattan Distance)

Fastest and most efficient

Ideal for 8-puzzle

Always returns optimal solution

📁 Project Structure
8-puzzle-game-solver/
│── eight_puzzle_solver.py   # main solver
│── README.md                 # project documentation
└── LICENSE (optional)

📊 Puzzle Example

Initial state:

1 2 3
4 0 6
7 5 8


Goal state:

1 2 3
4 5 6
7 8 0

🧪 Future Enhancements

GUI version (Tkinter)

Web version (Flask / Streamlit)

Animated state transitions

Mobile app version

AI Agent version using search trees

If you want any of these, just tell me!

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first.

📝 License

This project is licensed under the MIT License.
