class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        minHeap = [[0, 0, 0]] #[diff, r, c]
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        visit = set()
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if r == rows - 1 and c == cols - 1:
                return diff
            for dr,dc in directions:
                nr, nc = r + dr, c+  dc
                if (
                    nr in range(rows) and
                    nc in range(cols) and
                    (nr, nc) not in visit
                ):
                    newDiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(minHeap, [newDiff, nr, nc])
        return 0