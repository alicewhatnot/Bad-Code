class NodeClass:
    def __init__(self, data: str):
        # Private attribute to hold the node data
        self.__data = data

    def setData(self, newData: str):
        # Setter method to change the node data
        self.__data = newData

    def getData(self) -> str:
        # Getter method to return the node data
        return self.__data

class StackClass:
    def __init__(self, maxSize: int):
        # Private attributes for stack management
        self.__TopOfStackPointer = -1       # -1 means the stack is empty
        self.__MaxSize = maxSize            # Maximum number of elements
        self.__Stack = [None] * maxSize     # Array of NodeClass references

    def pushOnStack(self, value: str):
        # Push a new value onto the stack
        if self.__TopOfStackPointer < self.__MaxSize - 1:
            self.__TopOfStackPointer += 1
            self.__Stack[self.__TopOfStackPointer] = NodeClass(value)
        else:
            print("Stack Overflow")

    def popFromStack(self) -> str:
        # Pop the top value from the stack and return its data
        if self.__TopOfStackPointer >= 0:
            item = self.__Stack[self.__TopOfStackPointer].getData()
            self.__TopOfStackPointer -= 1
            return item
        else:
            print("Stack Underflow")
            return ""
        

stack = StackClass(3) 

# Push items onto the stack
stack.pushOnStack("Apple")
stack.pushOnStack("Banana")
stack.pushOnStack("Cherry")

# Attempting to push once full
stack.pushOnStack("Date")  # Should print "Stack Overflow"

# Pop items from the stack
print(stack.popFromStack())  #Gives Cherry as output
print(stack.popFromStack())  #Gives Banana as output
print(stack.popFromStack())  #Gives Apple as output

# Attempting to pop from empty stack
print(stack.popFromStack())  # Should print "Stack Underflow" and return NULL

