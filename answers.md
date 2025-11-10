# CMPS 2200 Assignment 3
## Answers

**Name:** Nikhil Modayur


Place all written answers from `assignment-03.md` here for easier grading.

## Part 1
1a) Greedy: repeatedly take the largest power of 2 coin without exceeding the remaining amount. Subtract and continue until you reach 0. This is the same as using the 1 bits of the binary representation of N.

1b) Optimal: Using greedy choice property: Let 2^k be the largest coin <= remaining R. Any optimal solution must use a coin of value 2^k because replacing smaller coins summing to 2^k would require at least 2 coins but using one 2^k uses fewer or equal coins. Optimal substructure: After taking 2^k, we are left with R - 2^k; the optimal solution for R - 2^k plus coin 2^k yields optimal for R. Repeating corresponds to binary expansion which is minimal in number of powers of two summations.

1c) Number of iterations equals number of 1 bits in N (<= log2 N + 1). Work O(log N) (or O(k) with k = floor(log2 N)+1). Span O(log N) for the sequential loop. Space of O(1).

## Part 2
2a) Counterexample: Denominations {1,3,4}, N=6. Greedy picks 4 + 1 + 1 = 3 coins, but the optimal is 3 + 3 = 2 coins.

2b) Optimal substructure: Let OPT(A) be min coins to make amount A (if possible). Then OPT(A) = 0 if A=0; otherwise OPT(A) = 1 + min_{d in D, d <= A and OPT(A-d) defined} OPT(A-d). Proof: Any optimal solution for A ends with some coin d, so removing it leaves amount A-d solved optimally (else we could improve A). Taking minimum over choices d gives this formula.

2c) Bottom-up DP: Initialize dp[0]=0; for a from 1..N set dp[a] = 1 + min dp[a-d] over d <= a with defined dp[a-d]; if none, dp[a] undefined (or inf). Work O(kN) where k=#denominations. Span O(N) sequential with parallelization per amount using reductions span could be O(N) still (since dependencies linear). Space of O(N).

## Part 3
3a) fast_MED: Build (m+1)x(n+1) table dp; base row/col are lengths; recurrence: if chars equal dp[i][j]=dp[i-1][j-1]; else dp[i][j]=1+min(dp[i-1][j], dp[i][j-1]) (delete or insert). Returns dp[m][n]. Work O(mn); span O(mn) sequential; wavefront parallel span O(m+n).

3b) Alignment: After filling dp, backtrack from (m,n): if chars equal move diagonally adding both chars; else choose deletion if dp[i][j]==dp[i-1][j]+1 (emit S char and '-' for T), else insertion (emit '-' for S and T char). Continue until i=j=0; reverse accumulated lists. This yields one optimal alignment consistent with edit distance.

