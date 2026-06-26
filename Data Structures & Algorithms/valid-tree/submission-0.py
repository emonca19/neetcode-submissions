class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False

        crs_req = {i: [] for i in range(n)}

        for crs, req in edges:
            crs_req[crs].append(req)
            crs_req[req].append(crs)

        visit = set()
        def dfs(course: int, parent: int) -> bool:
            if course in visit:
                return False
            
            visit.add(course)
            
            for nei in crs_req[course]:
                if nei == parent:
                    continue
                if not dfs(nei, course):
                    return False

            return True
        return dfs(0, -1) and len(visit) == n
        