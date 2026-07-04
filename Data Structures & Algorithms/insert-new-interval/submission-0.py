class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        x, y = newInterval # 2, 5

        i = 0
        n = len(intervals)

        while i<n and intervals[i][1] < x:
            res.append((intervals[i][0], intervals[i][1]))
            i+=1

        
        while i<n and y >= intervals[i][0]:
            x = min(x, intervals[i][0])
            y = max(y , intervals[i][1])
            i+=1
        res.append((x, y))
            
        while i<n:
            res.append((intervals[i][0], intervals[i][1]))
            i+=1
        

                    

        return res


# 00 01
# 10 11
# 20 21

