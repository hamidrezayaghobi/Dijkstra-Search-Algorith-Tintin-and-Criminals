# Dijkstra Search Algorithm: Tintin and criminals

## Problem:
Consider N cities and M roads. Tintin is in S city and wants to go to G city. There are T criminals in T cities who wish to catch Tintin. There are C cars that were randomly parked in C cities. These cars help criminals to pass the road 2X faster. Find the fastest way  which Tintin can go from S to G and if he cant, print "Poor Tintin".

## Input:
1. Number of tests (K)
2. Number of cities and roads(N, M)
3. In the next M line, roads from (u) to (v) with distnace (d)
4. Number of Criminals (T)
5. Cities where criminals are located in ([a1, a2, ... , aT])
6. Start and End (S, G)

## Output:
1. For each k test, 
    - If he can go from S to G without visiting criminal:
        1. Time of his path
        2. Number of cities in his path
        3. His path
    - else:
        1. Print "Poor Tintin"

## Constraint
1. 1 <= K <= 5
2. 1 <= N <= 5 * 10^4
3. 1 <= M <= min(N * (N- 1) / 2, 10^5)
4. 1 <= T, C, u, v, s, g, a_i, b_i <= N
5. 1 <= d <= 10^5

## Example
1. 
 ```
    Input       output
    1           Poor Tintin
    6 7
    1 2 2
    2 3 2
    2 4 3
    2 5 4
    3 4 2
    4 5 2
    3 6 1
    1
    5
    2
    2 4
    1 6
```
2.  
```
    Input       output
    1           5
    6 7         4
    1 2 2       1 2 3 6
    2 3 2
    2 4 3
    2 5 4
    3 4 2
    4 5 2
    3 6 1
    1
    5
    1
    2
    1 6
```
