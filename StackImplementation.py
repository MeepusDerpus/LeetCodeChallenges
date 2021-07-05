class StackImplementation:
    """ Min Stack Question, Implements a Stack DS along with getMin() which retreives the minimum element in O(1)
        utilises pair values for each stack index, [0] storing the element and [1] storing the minimum of the stack.

        push(int) is a normal stack push, utilises append since we are using a list implementation of a stack.

        pop removes the top element without returning anything.

        top returns the top element of the stack
        getMin() returns the minimum element of the stack without removing it
    """


    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin == None or curMin > x:
            curMin = x
        self.st.append((x,curMin))


    def pop(self) -> None:
        self.st.pop()


    def top(self) -> int:
        """returns the top value, referenced by -1,referenced by [0],[1] is the min so far """
        return self.st[-1][0] if self.st else None

    def getMin(self) -> int:
        """returns the top value, referenced by -1,referenced by [0],[1] is the min so far """
        return self.st[-1][1] if self.st else None
