class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in range(len(s)):
            if s[i] in "([{":
                st.append(s[i])
            elif s[i] == ']':
                if not st or st[-1] != '[':
                    return False
                else:
                    st.pop()

            elif s[i] == '}':
                if not st or st[-1] != '{':
                    return False
                else:
                    st.pop()

            elif s[i] == ')':
                if not st or st[-1] != '(':
                    return False
                else:
                    st.pop()
            
        return len(st) == 0
            
                