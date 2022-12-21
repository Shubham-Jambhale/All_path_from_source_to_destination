# All_path_from_source_to_destination

# Question 

You are given a list of connections between train stations, a source station number and a destination station number. Your job is to determine if all the routes from source station end at the
destination station. Return true if all the outgoing routes from source end at destination station.
Input: n: int Number of stations
connections: List[List[int]] list of pairs of connected stations
begin: int Source station number
end: int Destination station number .
Expected Time complexity <= O(n^2)

# Example 1:
n = 3, connections = [[0,1],[0,2]], begin = 0, end = 2

Ans: false

There is no outgoing route from station 1. hence starting from begin(0) and
ending at station 1 will get us stuck at station 1.

# Example 2:
n = 4, connections = [[0,1],[0,3],[1,2],[2,1]], begin = 0, end = 3

Ans: false

Only outgoing route from station 2 is towards station 1 and
from station 1 is towards station 2. Hence we will get stuck indefinitely between these
two stations if we end up at station 1 from begin (0).

# Example 3:
n = 4, connections = [[0,1],[0,2],[1,3],[2,3]], begin = 0, end = 3

Ans: true
