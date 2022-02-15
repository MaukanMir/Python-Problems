
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

 

Example 1:


Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:


Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
Example 3:


Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.


Success
Details 
Runtime: 978 ms, faster than 57.74% of Python3 online submissions for Nearest Exit from Entrance in Maze.
Memory Usage: 15.5 MB, less than 41.99% of Python3 online submissions for Nearest Exit from Entrance in



class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS, visited = len(maze), len(maze[0]), set()
        
        start = deque([(entrance[0], entrance[1], 0)])
        
        for i in maze:
            print(i)
        while start:
            
            r,c, distance = start.popleft()

            if r+1 == ROWS and maze[r][c] =='.' and entrance != [r,c]   or r-1 <0 and entrance != [r,c] and maze[r][c] == '.' or c +1 ==COLS  and maze[r][c] =="." and entrance != [r,c] or c-1 <0 and maze[r][c] == '.' and entrance != [r,c]:
               
                return distance


            directions = [ [r+1,c], [r-1,c], [r,c+1], [r,c-1]]

            for x,y in directions:
                if x >=0 and x< ROWS and y>=0 and y< COLS and maze[x][y] == '.' and (x,y) not in visited:
                    start.append([x,y, distance+1])
                    visited.add((x,y))
                
        
        
        return -1
