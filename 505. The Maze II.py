There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.

The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).

 

Example 1:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: 12
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
The length of the path is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
Example 2:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: -1
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: -1
 

Constraints:

m == maze.length
n == maze[i].length
1 <= m, n <= 100
maze[i][j] is 0 or 1.
start.length == 2
destination.length == 2
0 <= startrow, destinationrow <= m
0 <= startcol, destinationcol <= n
Both the ball and the destination exist in an empty space, and they will not be in the same position initially.
The maze contains at least 2 empty spaces.

Success
Details 
Runtime: 688 ms, faster than 11.96% of Python3 online submissions for The Maze II.
Memory Usage: 15 MB, less than 34.50% of Python3 online submissions for The Maze II.


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        ROWS, COLS, visited, routes = len(maze), len(maze[0]), set(), {}
        
        if ROWS == 0:return True
        if maze[start[0]][start[1]] ==1:return False
        
        heapCon = [(0,start[0],start[1])]
        heapq.heapify(heapCon)
        
        while heapCon:
            dist, r,c = heapq.heappop(heapCon)
            
            routes[(r,c)] = min(dist, routes.get((r,c), float('inf')))
            
            directions = [[1,0], [-1,0],[0,-1], [0,1]]
            
            for rX, rY in directions:
                tempX, tempY, tempD = r,c, dist
                
                while tempX+ rX >=0 and tempX +rX < ROWS and tempY + rY >=0 and tempY + rY < COLS and maze[tempX+rX][tempY+ rY] ==0:
                    tempX = tempX + rX
                    tempY = tempY + rY
                    tempD +=1
                
                if (tempX,tempY) not in visited or tempD < routes.get((tempX,tempY), float('inf')):
                    heapq.heappush(heapCon,(tempD,tempX,tempY))
                    visited.add((tempX,tempY))
        
        if (destination[0], destination[1]) not in visited:
            return -1
        
        return routes[(destination[0], destination[1])]
