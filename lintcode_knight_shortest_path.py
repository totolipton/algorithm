# Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) 
#with a source position, find the shortest path to a destination position,
# return the length of the route. 
# Return -1 if knight can not reached.

#  Notice

# source and destination must be empty.
# Knight can not enter the barrier.

# [[0,0,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return 2

# [[0,1,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return 6

# [[0,1,0],
#  [0,0,1],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return -1



class Solution:
    # @param {boolean[][]} grid a chessboard included 0 (False) and 1 (True)
    # @param {Point} source a point
    # @param {Point} destination a point
    # @return {int} the shortest path 
    def shortestPath(self, grid, source, destination):
    	if not grid or not grid[0]:
    		return 0

    	m= len(grid)
    	n=len(grid[0])

    	visited=set()
    	visited.add((source.x, source.y))
    	q=collections.deque([(source.x, source.y, 0)])

    	dirs=[(1,2),(-1,-2),(1,-2),(-1,2),(2,1),(2,-1),(-2,1),(-2,-1)]

    	while q:
    		size=len(q)
    		for _ in range(size):
    			sx, sy, step=q.popleft()
    			if sx==destination.x and sy==destination.y:
    				return step

    			for di, dj in dirs:
    				nx=sx+di
    				ny=sy+dj
    				if 0<nx<m and 0<ny<n and (nx,ny) not in visited:
    					q.append((nx,ny,step+1))
    					visited.add((nx,ny)) 
    	return -1
