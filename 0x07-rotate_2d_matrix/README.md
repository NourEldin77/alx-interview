# Rotate 2D Matrix

Rotate an n x n 2D matrix 90 degrees clockwise in place.

## Function Signature

```python
def rotate_2d_matrix(matrix):
```

## Parameters

- `matrix` (list of list of int): A 2D list representing the matrix to be rotated.

## Returns

- `None`: The function modifies the input matrix in place and does not return a value.

## Assumptions

- The matrix will have 2 dimensions and will not be empty.

## Example

### Input

```python
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### Output

```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```