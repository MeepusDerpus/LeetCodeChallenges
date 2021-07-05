class StacksQueues:
    def __init__(self):
        pass

    def isValidPair(self,s1,s2):
        """Helper Function for isvalid, Checks if s1, s2 are a valid bracket pair"""
        if (s1 == '(' and s2 == ')'):
            return True
        if (s1 == '[' and s2 == ']'):
            return True
        if (s1 == '{' and s2 == '}'):
            return True
        return False

    def isValid(self, s: str) -> bool:
        """Checks if s contains valid ({[]}) pair in correct order"""
        st = []

        for char in s:
            if (len(st) != 0):
                e = st[-1]
                if (self.isValidPair(e,char)):
                    st.pop()
                    continue
            st.append(char)
        return (len(st)==0)


#



