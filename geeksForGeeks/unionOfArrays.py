class Solution:    
    def findUnion(self, a, b):
        union_set = set(a)  
        union_set.update(b)
    
        return list(union_set)
