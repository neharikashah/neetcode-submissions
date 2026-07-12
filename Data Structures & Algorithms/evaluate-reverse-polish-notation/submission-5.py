class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token in ("+" , "-", "/", "*"):
                x = st.pop()
                y = st.pop()

                if token == '+':
                    new = x + y
                if token == '-':
                    new = y - x

                if token == '*':
                    new = x * y
                if token == '/':
                    new = int(y / x)

                st.append(new)   

            else:
                st.append(int(token))

        return st.pop()