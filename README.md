# Staffordshire University Degree Classification Calculator (Python)

This is a Python-based utility for Staffordshire University students to:

1. **Calculate the required Level 6 average** to achieve a First-Class Honours degree, based on your top three Level 5 module marks.
2. **Simulate the final degree classification** (First, 2:1, 2:2, Third, or Fail) using the same methodology as the official Staffordshire University Degree-Class Calculator.

## Overview

This calculator assists students in determining:

* The exact Level 6 average needed to secure a First-Class Honours degree, based solely on four Level 5 module marks.
* Their projected overall degree classification by combining a Level 5 average with Level 6 module assessments, applying Staffordshire’s official weightings and drop rules.

## Features

* **Option 1**: Input four Level 5 (2nd Year) module marks; calculates the Level 6 average you must achieve to reach a 70% overall for a First-Class Honours.
* **Option 2**: Input your Level 5 average and detailed Level 6 marks; applies Staffordshire’s rules:

  * Level 5 contributes 30%, Level 6 contributes 70%.
  * Three 30‑credit Level 6 modules (ATICS, OSIB, ITIS), dropping the lowest mark.
  * Final Year Project (FYP, 60 credits) weighted 20% Proposal, 60% Report, 20% Viva.
  * Computes the overall weighted average and classifies (1st, 2:1, 2:2, Third, Fail).

## Installation & Requirements

* Python 3.x
* No external libraries required.

```bash
# Clone the repo
git clone https://github.com/yourusername/degree-class-calculator.git
cd degree-class-calculator
# Run the script
python degree_calculator.py
```

## Usage

1. Run the script:

   ```bash
   python degree_calculator.py
   ```
2. Choose an option from the menu:

   * `1` to calculate the Level 6 average required for a 1st Class Honours.
   * `2` to calculate your projected degree classification based on all your marks.
   * `0` to exit.
3. Follow the prompts to enter your marks.

## Example Session

```text
Staffordshire Degree Classification Menu
1. Calculate required Level 6 average for 1st class honours
2. Calculate degree classification from Level 5 & 6 marks
0. Exit
Choose an option: 1

Enter the marks for Level 5 across your four modules:
Enter mark 1: 65
Enter mark 2: 70
Enter mark 3: 62
Enter mark 4: 68

What you'll need to get on your Level 6 modules this year to secure a 1st honours: 71%

---

Choose an option: 2

Enter your marks:
Level 5 average (%): 75

-- ATICS (30 credits, two 50% assessments) --
ATICS Assessment 1 (%): 80
ATICS Assessment 2 (%): 70

-- OSIB (30 credits, two 50% assessments) --
OSIB Assessment 1 (%): 78
OSIB Assessment 2 (%): 82

-- ITIS (30 credits, single assessment) --
ITIS Assessment (%): 68

-- FYP (60 credits) --
FYP Proposal (20%): 85
FYP Report (60%): 88
FYP Viva (20%): 90

-- Summary --
ATICS: 75.00%
OSIB: 80.00%
ITIS: 68.00%
Lowest 30-credit module dropped: 68.00%
FYP: 87.20% (60 credits)
Level 6 average (after drop): 76.00%
Overall weighted average: 75.10%
Projected classification: First (1st)
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.


