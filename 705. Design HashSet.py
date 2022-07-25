
# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

# Example 1:

# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
 

# Constraints:

# 0 <= key <= 106
# At most 104 calls will be made to add, remove, and contains.


Success
Details 
Runtime: 237 ms, faster than 76.19% of Python3 online submissions for Design HashSet.
Memory Usage: 19 MB, less than 49.57% of Python3 online submissions for Design HashSet.



class MyHashSet:

    def __init__(self):
        self.cache = set()

    def add(self, key: int) -> None:
        self.cache.add(key)

    def remove(self, key: int) -> None:
        if key in self.cache:
            self.cache.remove(key)

    def contains(self, key: int) -> bool:
        return (key) in self.cache
