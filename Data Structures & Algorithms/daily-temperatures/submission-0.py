class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        res = [0] * n
        st = [] #pair -> temp, index

        for i, temp in enumerate(t):
            while st and temp > st[-1][0]: #list element in stack and its index value
                sttemp , stind = st.pop()
                res[stind] =  (i - stind)

            st.append([temp, i])
          

            

        return res
