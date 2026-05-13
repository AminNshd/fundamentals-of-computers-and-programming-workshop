# 💻 Fundamentals of Computer Science Projects

**Course:** Fundamentals of Computer Science and Programming

**Status:** Complete

**Instructor:** Dr. Soheila Ashkezari-Tousi

This repository contains a collection of core projects exploring fundamental programming concepts, data structures, and algorithmic logic. The projects range from traffic simulation and knowledge graphs to adversarial search.

---

## 📂 Project Overview

| Project | Concept | Description |
| --- | --- | --- |
| **1. Traffic Simulator** | Simulation & Logic | A grid-based traffic simulation featuring cars, squares, and crosses with randomized movement logic. |
| **2. Movie Knowledge Graph** | Data Structures | A movie management system that builds knowledge graphs and adjacency matrices to visualize relationships. |

---

## 1️⃣ Traffic Simulator (Project 1)

**Location:** `/Traffic-Simulator`

A 20x20 grid simulation that models traffic flow. The environment includes different cell types such as squares and intersections (crosses), where cars navigate based on specific movement rules and randomized decision-making.

### Key Components

* **Cell & Car Classes:** Objects representing the grid state and vehicle properties (coordinates and direction).
* **Grid Logic:** Implements specialized cell types (`SQUARE`, `CROSS`, `LEGAL`) that dictate how vehicles transition through the map.
* **Movement Engine:** A `next_step` function that updates the entire system state, using `time.sleep` to provide a real-time visual update in the console.

### 💻 How to Run

```bash
python NOSHADI_PROJECT1.py

```

*Note: The program will prompt for the number of cars, squares, and crosses to initialize the simulation.*

---

## 2️⃣ Movie Knowledge Graph (Project 2)

**Location:** `/Movie-Graph`

This project transforms a movie database into a structured graph. It maps the relationships between movies, directors, and actors, allowing for complex queries and visual representation of data connections.

### Key Components

* **Graph Implementation:** Custom `Vertex` and `Graph` classes that manage adjacency lists and vertex connections.
* **Data Visualization:** Integrates `networkx` and `matplotlib` to draw knowledge graphs based on search queries.
* **Adjacency Matrices:** Functions to generate and print mathematical representations of the relationships between different data categories.

### 💻 How to Run

```bash
python Movies.py

```

---

## 🛠 Tech Stack

* **Languages:** Python 3.x
* **Libraries:** `networkx`, `matplotlib`, `random`, `json`, `time`
* **Approach:** All algorithms and data structures (Graphs, Search Trees, Matrices) are implemented from scratch to demonstrate an understanding of computer science fundamentals.

**Developer:** Amirhossein Noshadi

**Date:** February 2023 (Bahman 1401)
