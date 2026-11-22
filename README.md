# Monte-Carlo-Poker-Simulation
Vectorized Monte Carlo Simulation for estimating Flush and Four of a Kind by considering 100,000 trials in pure Numpy.

# Math Behind The Code
There are $\binom{52}{5} = 2,598,960$ ways to select 5 cards out of 52 (combination).

Now calculating flush and four of a kind:

$$
P(\text{Flush}) = \frac{4 \times \binom{13}{5}}{\binom{52}{5}} \approx 0.001981
$$

$$
P(\text{Four of a Kind}) = \frac{13 \times 48}{\binom{52}{5}} \approx 0.000240
$$

# How Code Works
- Used `np.broadcast_to()` to stretch the `deck` matrix to 100,000 and created a `grand_matrix`.
- Shuffled the rows (axis = 1) of `grand_matrix` using `rng.permuted(grand_matrix, axis = 1)`.
- Now suffled 'grand_matrix' and extracted (100000, 5) matrix from the `grand_matrix` and create `shuffled_matrix`.
- Used `np.diff()` on `actual_suit` to get to know which row's elements are subtracted to 0.
- Used `np.sort()` on `actual_rank` and did `sort[:, 0] == sort[:, 3]) | (sort[:, 1] == sort[:, 4]` to find out if 1st and 4th and 2nd and 5th element indicating the row has four same rank

# Simple Things To Learn From The Code
1. Boolean Masking - `(diff == 0).all(axis = 1)` on `diff` matrix and `(sort[:, 0] == sort[:, 3]) | (sort[:, 1] == sort[:, 4])` on `sort` matrix
2. `actual_suit` is floor division (`//`) of `shuffled_matrix` and `actual_rank` is modulo (`%`) of `shuffled_matrix`

## Run It
```bash
python monte_carlo.py
```
