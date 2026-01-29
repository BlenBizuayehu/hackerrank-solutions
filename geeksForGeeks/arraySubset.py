class Solution:
    def isSubset(self, a, b):
        visited = [False] * len(a)
        
        for elem in b:
            found = False
            for i in range(len(a)):
                if a[i] == elem and not visited[i]:
                    visited[i] = True  
                    found = True
                    break
            if not found:
                return False  
        return True 
