# NFA to Regular Expression

## Contents
- Overview
- Features
- How It Works
- Installation & Usage
- Example Execution
- License

## Overview
This project implements a **Python program** that converts a **Non-Deterministic Finite Automaton (NFA)** into a **Regular Expression (RE)**. It takes an input file describing an NFA, processes its transitions, and outputs the corresponding regular expression.

## Features
- **Reads NFA definition** from an input file.
- **Eliminates states** systematically while preserving equivalent transitions.
- **Generates a simplified regular expression** that represents the accepted language.
- **Supports multiple input formats** with different state transition representations.

## How It Works
1. **Reads the input file** containing:
   - The set of states.
   - The alphabet (allowed symbols).
   - The start state and final states.
   - The transition table.
2. **Processes the transitions**:
   - Eliminates unnecessary states.
   - Combines transitions using the `|` (OR) operator.
   - Uses the `*` operator for looping transitions.
3. **Simplifies the final regular expression** by removing redundant parentheses and operators.
4. **Outputs the final expression** representing the NFA’s language.

## Installation & Usage
### Prerequisites
- Python 3

### Running the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/NFA-to-RE.git
   cd NFA-to-RE
   ```
2. Run the Python script with an input file:
   ```bash
   python NFA_to_RE.py
   ```

## Example Execution
### Input (`in.txt`):
```
5
5225 9898 6448 1944 3868
2
p g
5225
3
1944 9898 3868
10
3868 g 5225
3868 p 3868
1944 g 6448
1944 p 9898
5225 g 1944
6448 p 5225
9898 g 6448
9898 p 9898
6448 g 3868
5225 p 3868
```

### Output:
```
(p|g)*5225(p|g)*
```

## License
This project is free to use and modify for educational purposes.

