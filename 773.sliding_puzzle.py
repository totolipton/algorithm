On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        def board2str(board):
        	res=''
        	for i in range(2):
        		for j in range(3):
        			res+=str(board[i][j])
        	return res
        goal="123450"
        q=collections.deque()
        newboard=board2str(board)
        q.append((newboard,0))
        visited=set()
        visited.add(newboard)

        while q:
        	path, step=q.popleft()
        	if path==goal:
        		return step
        	zeroPos=path.index('0')
        	x=zeroPos/3
        	y=zeroPos%3
        	path=list(path)
        	for di, dj in zip([0,0,1,-1],[1,-1,0,0]):
        		newx=x+di
        		newy=y+dj
        		if newx<0 or newy<0 or newx>=2 or newy>=3:
        			continue
        		path[newx*3+newy],path[x*3+y]=path[x*3+y],path[newx*3+newy]
        		newPath="".join(path)
        		if newPath not in visited:
        			q.append((newPath, step+1))
        			visited.add(newPath)
        		path[newx*3+newy],path[x*3+y]=path[x*3+y],path[newx*3+y]
        return -1