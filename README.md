# TSP Local Search AI (Python)

Project developed for the **Artificial Intelligence** course (2024/2025), Computer Engineering. Solving and testing the **Traveling Salesman Problem (TSP)** with Local Search Algorithms: **Hill Climbing**, **Stochastic Hill Climbing**, **Partial Hill Climbing**, and more.

---

## 🚀 Features

- Representation of cities with (x, y) coordinates
- Distance calculation using the circular TSP formula
- Multiple local search optimization algorithms:
  - `optDistCircularIC` (reference algorithm)
  - `greedy` (Hill Climbing)
  - `sGreedy` (Stochastic Hill Climbing)
  - `pGreedy` (Partial Hill Climbing)
  - `rGreedy` (Hill Climbing with Restarts) [optional/bonus]
- Randomized starting positions
- Runtime and distance tracking
- Visual representation of the tours (if available via `libic`)

---

## 🧪 Usage

```bash
python main.py [iterations]
```

- Load an instance (e.g., `berlin52.tsp`)
- Select the desired algorithm (`sGreedy`, `greedy`, etc.)
- Optionally pass the number of iterations as a command-line argument
- Visualize the tour and results in terminal or window

---

## 📁 Project Structure

```
.
├── ic.py               # Core functions for city and distance operations
├── algoritmos.py       # Implementation of the local search algorithms
├── libic.py            # Graphical and utility support (provided)
├── main.py             # Entry point for running experiments
├── berlin52.tsp        # Sample TSP instance
├── README.md
```

---

## 📊 Experimental Setup

- Tested on the `berlin52` TSP instance
- Algorithms compared by:
  - Initial vs. final tour distance
  - CPU time
- Multiple runs per algorithm to analyze average performance

> Results summarized in tables for the report, with visual support where applicable.

---

## 📚 Technologies Used

- Python 3.x
- Standard libraries: `math`, `random`, `time`, `sys`
- Optional: Custom `libic` for visualization

---

## 👨‍💻 Authors & Acknowledgments

Developed as part of the Artificial Intelligence course  ( IPP / ESTG), 2024/2025.

---

## 📄 License

This project is for academic use. Feel free to explore and adapt for educational purposes.
