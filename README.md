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

### Example of Input
| Input | output |
|  :--------  | :------: |
|  1
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
1 6 | Poor Tintin|

