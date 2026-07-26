class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for c in s:
            if c=='(':
                st.append('(')
            elif  c =='[':
                st.append('[')
            elif  c=='{':
                st.append('{')
            else:
                if st:
                    if c==')' and st[-1]=='(':
                        st.pop()
                    elif  c ==']' and st[-1]=='[':
                        st.pop()
                    elif  c=='}' and st[-1]=='{':
                        st.pop()
                    else:
                        return False
                else:
                    return False
        
        if not st:
            return True
        else:
            return False