class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = {i: [] for i in range(n)}
        res = 0
        for a, b in edges:
            nodes[a].append(b)
            nodes[b].append(a)
        
        visit = set()
        def dfs(node: int) -> None:
            if node in visit:
                return
            
            visit.add(node)
            for nei in nodes[node]:
                dfs(nei)
        
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res



        