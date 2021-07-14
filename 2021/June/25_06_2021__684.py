from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        start = {edges[0][0]}
        end = {edges[0][1]}
        connections = {(edges[0][0], 1), (edges[0][1], 1)}
        ans = None
        for edge in edges[1:]:
            l = edge[0]
            r = edge[1]
            # Polygon -> break
            if (l, 1) in connections and (r, 1) in connections:
                ans = edge
                break
            # Reconnecting with non end node
            elif (l, 1) not in connections and (r, 1) not in connections:
                ans = edge
                break
            # Reconnecting with fully connected nodes
            elif (l, 2) in connections or (r, 2) in connections:
                ans = edge
                break
            # l is start or end
            elif (l, 1) in connections and (r, 1) not in connections and (r, 2) not in connections:
                connections.remove((l, 1))
                connections.add((l, 2))
                if l in start:
                    start.remove(l)
                    start.add(r)
                elif l in end:
                    end.remove(l)
                    end.add(r)
                else:
                    print("impossibro!")
                connections.add((r, 1))
            # r is start or end
            elif (r, 1) in connections and (l, 1) not in connections and (l, 2) not in connections:
                connections.remove((r, 1))
                connections.add((r, 2))
                if r in start:
                    start.remove(r)
                    start.add(l)
                elif r in end:
                    end.remove(r)
                    end.add(l)
                else:
                    print("impossibro!")
                connections.add((l, 1))
            else:
                print(l, r, connections, (l, 1) in connections, (r, 1) in connections)
                print("double impossibro!!")
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
    print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]))
    print(sol.findRedundantConnection([[1,2],[2,3],[1,5],[3,4],[1,4]]))
    print(sol.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))