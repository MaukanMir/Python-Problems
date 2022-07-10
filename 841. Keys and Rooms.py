# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

 

# Example 1:

# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation: 
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.
# Example 2:

# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

# Success
# Details 
# Runtime: 64 ms, faster than 84.89% of Python3 online submissions for Keys and Rooms.
# Memory Usage: 14.9 MB, less than 34.24% of Python3 online submissions for Keys and Rooms.




class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        seen = [False] * len(rooms)
        seen[0] = True
        
        stack = [0]
        
        while stack:
            node = stack.pop()
            
            for adjacent in rooms[node]:
                if not seen[adjacent]:
                    seen[adjacent] = True
                    stack.append(adjacent)
        return all(seen)
       
       
       Success
Details 
Runtime: 72 ms, faster than 87.43% of Python3 online submissions for Keys and Rooms.
Memory Usage: 14.9 MB, less than 24.11% of Python3 online submissions for Keys and Rooms.
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        seen = [False] * len(rooms)
        seen[0] = True
        visited = set()
        def dfs(node):
            if node in visited or node >= len(rooms):
                return False
            
            for nextNode in rooms[node]:
                if not seen[nextNode]:
                    seen[nextNode] = True
                    dfs(nextNode)
        dfs(0)
        return all(seen)
       
