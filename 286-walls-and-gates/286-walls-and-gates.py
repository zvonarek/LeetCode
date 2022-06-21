#Solution crafted by LeetCode: https://www.youtube.com/watch?v=e69C6xhiSQE

class Solution:
  def wallsandGates(self, rooms: List[List[int]]) -> None:
    ROWS, COLS = len(rooms), len(rooms[0])
    vist = set()
    queue = deque()
    
    for r in range(ROWS): 
      for c in range(COLS):
        if rooms[r][c] == 0:
          queue.append([r,c])
          visit.add((r,c))
    distGate = 0
    
    while queue:
      for i in range(len(queue)):
        r, c in queue.popleft()
        rooms[r][c] = distGate
        addRoom(r+1,c)
        addRoom(r-1,c)
        addRoom(r,c+1)
        addRoom(r,c-1)
      distGate += 1
      
   def addRoom(r,c):
    if (r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visit or rooms[r][c]==-1): 
      return
    visit.add((r,c))
    queue.append([r,c])
