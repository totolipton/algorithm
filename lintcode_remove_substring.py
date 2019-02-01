Given a string s and a set of n substrings. You are supposed to remove every instance of those n substrings from s so that s is of the minimum length and output this minimum length.

Example

Given s = ccdaabcdbb, substrs = ["ab", "cd"]
Return 2

Explanation: 
ccdaabcdbb -> ccdacdbb -> cabb -> cb (length = 2)


class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
   """
   这里最关键的问题就是删除短字符串的顺序会影响到最终结果，因此这就变成了一道搜索问题：
   我们每次删掉一个短字符串，把剩下的字符串当做一个子问题继续进行搜索，在搜索过程中记录所得到的最短字符串长度即可。
   同时为了避免重复搜索，我们用一个set来记录已经搜索过的字符串。
   """

    def minLength(self, string, dictionary):
    	if len(string)==0 or len(dictionary)==0:
    		return -1

    	q=collections.deque([string])
    	visited=set([string])
    	min_len=len(string)

    	while q:
    		origin=q.popleft()
    		min_len=min(min_len, len(origin))

    		for sub in dictionary:
    			idx=origin.find(sub)
    			while idx:
    				newString=string[:idx]+string[idx+len(sub):]
    				if newString not in visited:
    					q.append(newString)
    					visited.add(newString)
    				idx=origin.find(sub, idx+1)
    	return min_len

