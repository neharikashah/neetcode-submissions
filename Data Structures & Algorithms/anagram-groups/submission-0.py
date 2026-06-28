class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        groups = defaultdict(list)
        for s in strs:
            temp = "".join(sorted(s))
            groups[temp].append(s)
        
        for value in groups.values():
   
            res.append(value)

        return res
        