# 🚗 Carpooling Optimization System

A smart carpooling system that matches passengers to drivers based on shared routes, capacity constraints, and time windows — using **Integer Linear Programming (ILP)** for optimal matching.

---

## 📌 Features

- ✅ Connects nearby people going to the same or nearby destinations
- 🔁 Matches even if sources are different — as long as paths overlap
- 📉 Uses **ILP** to minimize detour and maximize ride sharing
- 🚘 Supports driver capacity and route constraints
- ⏰ Optional: Add time window constraints for real-world scenarios

---

## 📊 Algorithm Overview

The city map is represented as a **graph**, where:
- **Nodes** = locations (e.g., intersections, landmarks)
- **Edges** = roads (with distances or travel times)

We use:
- **Dijkstra’s algorithm** to compute the shortest paths for each driver
- **ILP (Integer Linear Programming)** to assign passengers to drivers efficiently

### 🧠 ILP Model

- **Objective**: Maximize number of successful ride matches  
- **Decision Variables**: `x_{dp}` = 1 if driver `d` picks up passenger `p`, else 0  
- **Constraints**:
  - One driver per passenger
  - Capacity limits for each driver
  - Only allow match if the driver's route overlaps with passenger’s source

---

## 📦 Requirements

- Python 3.7+
- [PuLP](https://pypi.org/project/PuLP/)

Install dependencies:
```bash
pip install pulp
