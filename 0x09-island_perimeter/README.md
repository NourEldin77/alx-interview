# Island Perimeter

This project contains a Python function to calculate the perimeter of an island in a grid. The function is in `0-island_perimeter.py`.

## Requirements

- Editors: `vi`, `vim`, `emacs`
- Python 3.4.3 on Ubuntu 20.04 LTS
- Files end with a new line
- First line: `#!/usr/bin/python3`
- `README.md` is mandatory
- PEP 8 style (version 1.7)
- No module imports
- Documented code
- Executable files

## Task

Create a function `def island_perimeter(grid):` that returns the island's perimeter.

- `grid` is a list of lists of integers:
    - `0` is water
    - `1` is land
    - Cells are square (side length 1)
    - Cells are connected horizontally/vertically
    - `grid` is rectangular (max 100x100)
- Grid is surrounded by water
- One island or none
- No lakes

## Example

```python
def island_perimeter(grid):
    # Your implementation here
```

## Usage

```python
from 0-island_perimeter import island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output: 12
```

## Author

Part of the ALX Interview preparation curriculum. Island Perimeter

