# MatrixPattern.py

## Overview

`MatrixPattern.py` is a Python script that generates a square matrix representing either a **linear** or **cyclical** connectivity pattern between elements. These matrices are commonly used in modeling systems in **quantum chemistry** and **solid-state physics** — particularly in **tight-binding models**. (It is also available in Java)

## How It Works

Upon execution, the script prompts the user to:
- Enter the **size** of the matrix `n` (number of atoms or sites).
- Specify the **type** of system: `"linear"` or `"cyclical"`.

Based on the input, the script creates an `n x n` matrix with the following rules:
- Diagonal entries (self-connections) are set to `0`.
- Entries where atoms/sites are directly connected are set to `1`:
  - In the **linear model**, only immediate neighbors are connected.
  - In the **cyclical model**, it also connects the first and last atoms (i.e., a closed ring).

The matrix is then printed in both a human-readable format and a format compatible with **Wolfram Mathematica**.

## Scientific Context

While not explicitly performing any quantum chemistry calculations, the output matrix can represent a **Hamiltonian** or an **adjacency matrix** in **tight-binding** or **Hückel** theory models:

- `"Linear"` configuration can model a **linear chain of atoms**, such as a conjugated polymer chain.
- `"Cyclical"` configuration can model a **ring of atoms**, such as **benzene**.

In these contexts:
- The `1`s in the matrix represent **beta (β) values**, or **hopping integrals**, which describe the strength of interaction (electron "hopping") between neighboring atomic orbitals.
- The matrix can be used as a foundation for further computations, such as **eigenvalue analysis** to determine **molecular orbitals** or **energy levels**.

**Note:** This script **does not compute** β values or energy levels — it only generates the matrix structure used in such models.

## Example

For `n = 4` and `type = cyclical`, the generated matrix would be:

