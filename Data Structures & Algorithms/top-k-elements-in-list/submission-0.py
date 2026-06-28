class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        m = {}
        for i in range(n):
            m[nums[i]] = m.get(nums[i], 0) + 1

        v = [[] for _ in range(n + 1)]

        for key, value in m.items():
            v[value].append(key)

        res = []
        for i in range(len(v)-1, 0, -1):
            for num in v[i]:
                res.append(num)

            if len(res) == k:
                break
        
        return res
