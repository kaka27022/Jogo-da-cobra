# 🎲 Snakes and Ladders – Simulation & Probability Analysis

## 📌 Project Overview

This project simulates the classic **Snakes and Ladders** board game to analyze winning probabilities and other statistical properties under different scenarios.

The objective is not only to compute final probabilities, but also to clearly demonstrate the modeling strategy, simulation logic, and analytical reasoning behind the results.

Each scenario is evaluated through **10,000 independent simulations**.

---

## 🎯 Objectives

This project aims to answer the following questions:

1. What is the probability that the starting player wins in a two-player game?
2. On average, how many snakes do players land on per game?
3. If ladders only activate with 50% probability, what is the average number of dice rolls required to finish a game?
4. What starting position should Player 2 have to make the game approximately fair?
5. If Player 2 is immune to the first snake they land on, what is Player 1’s probability of winning?

---

## 🧠 Methodology

The solution is based on **Monte Carlo simulation**, following these steps:

- Simulate 10,000 independent games per scenario
- Model a fair 6-sided die
- Implement the snakes and ladders board structure
- Simulate turn-based player movement
- Track relevant metrics:
  - Game winner
  - Number of snakes encountered
  - Total number of dice rolls
- Modify rules according to each experimental scenario

Repeated random simulations allow us to approximate the true probabilities of each outcome.

---

## 🛠️ Technologies Used

- Python 3
- `random` module for dice simulation
