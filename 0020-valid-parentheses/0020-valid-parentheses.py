class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        if len(s)<2:
            return False
        d = {')':'(', '}':'{',']':'['}
        for c in s:
            if (c == ')' or c == '}' or c == ']') and not st:
                return False
            if c == '(' or c=='{' or c=='[':
                st.append(c)
            elif st:
                if d[c] == st[-1]:
                    st.pop()
                else:
                    return False
        
        return True if not st else False
            