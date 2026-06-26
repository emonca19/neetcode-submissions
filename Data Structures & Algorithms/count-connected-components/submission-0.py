class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}

        for s1, s2 in edges:
            graph[s1].append(s2)
            graph[s2].append(s1)
        

        visit = set()
        def connected_nodes(node: int) -> None:
            for req in graph[node]:
                if req not in visit:
                    visit.add(req)
                    connected_nodes(req)
        
        res = 0
        for i in range(n):
            if i not in visit:
                connected_nodes(i)
                res += 1
                visit.add(i)
        return res
                
            





        