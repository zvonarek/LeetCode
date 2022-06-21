Description
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF

Example 1 <br/>

Input: <br/>
[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]] <br/>
Output: <br/> 
[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]] <br/>

Explanation: <br/>
the 2D grid is: <br/>
INF  -1  0  INF <br/>
INF INF INF  -1 <br/>
INF  -1 INF  -1 <br/>
  0  -1 INF INF <br/>
the answer is: <br/>
  3  -1   0   1 <br/>
  2   2   1  -1 <br/>
  1  -1   2  -1 <br/>
  0  -1   3   4 <br/>

Example 2 <br/>

Input: <br/>
[[0,-1],[2147483647,2147483647]] <br/>
Output: <br/>
[[0,-1],[1,2]]
