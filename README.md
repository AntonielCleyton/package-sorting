# Package Sorting

A simple Python script that sorts packages based on their dimensions and mass.  
This solution was created for a coding challenge at Thoughtful's robotic automation factory.

## Objective

Implement a function (or class, in our OOP version) to determine the correct stack for each package according to the following rules:

- **Bulky**: volume ≥ 1,000,000 cm³ (width × height × length) or any dimension ≥ 150 cm.
- **Heavy**: mass ≥ 20 kg.

### Stacks

- **STANDARD**: packages that are neither bulky nor heavy.
- **SPECIAL**: packages that are either bulky or heavy (but not both).
- **REJECTED**: packages that are both bulky and heavy.

## How It Works

1. We define a `Package` class with:
   - A constructor receiving `width`, `height`, `length`, and `mass`.
   - Methods to calculate `volume()`, check `is_bulky()`, and check `is_heavy()`.
   - A method `designated_stack()` that returns one of the three stacks: **REJECTED**, **SPECIAL**, or **STANDARD**.

2. In `main.py`, we instantiate some example packages and print out the result.

## Installation & Execution

1. **Clone this repository**:
   ```bash

2. **Navigate into the folder**:
   cd package-sorting
   
3. **Run the Python script**:
   python main.py

**Example Output:**

![image](https://github.com/user-attachments/assets/cff0d5ad-c047-466f-8cc5-2e46e39e2cff)
