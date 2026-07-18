class Solution(object):
    def rearrangeString(self, s, x, y):
        """
        :type s: str
        :type x: str
        :type y: str
        :rtype: str
        """
        before = []
        middle = []
        after = []
        for c in s:
            if c ==x:
                after.append(c)
            elif c==y:
                before.append(c)
            else:
                middle.append(c)
        final = before+middle+after
        return ''.join(final)