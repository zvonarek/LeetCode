class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weakestRows = {}
        for i, row in enumerate(mat):
            weakestRows[i] = sum(row)
        sorted_weakestRows = dict(sorted(weakestRows.items(), key = lambda x: x[1]))
        return list(sorted_weakestRows.keys())[:k]
        
# attempt not using dictionary as a mini-challenge to myself, indexing check
#         weakestRows = []
        
#         for i in range(len(mat[:][0])-1):
            
#             currRow = sum(mat[i])
#             nextRow = sum(mat[i+1])
            
#             if (currRow <= nextRow):
                
#                 weakestRows.append(tuple((i,currRow)))
                
#         sortedWeakestRows = sorted(weakestRows[0:k+1], key = lambda x: x[1])
        
#         res = [sortedWeakestRows[i][0] for i in range(len(sortedWeakestRows))]
        
#         return res[:k]
    