class Stack():
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = []
    
    def push(self,item):
        if not self.isFull():
            self.stack.append(item)
        else:
            print ("Stack full.")
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print ("Stack empty.")
            return None
    
    def isFull(self):
        return len(self.stack) == self.maxSize
    
    def isEmpty(self):
        return len(self.stack) == 0
    
print ("Please enter a word or phrase to be tested")
myString = input()
myString = myString.lower()
list1 = list(myString)
numChars = len(list1)
s = Stack(10)
palindrome = True
list2 = []*numChars
for char in range (0,numChars):
    s.push(list1[char])

for char in range (0,numChars):
    list2.append(s.pop())
    
for char in range (0,numChars):
    if list1[char] != list2[char]:
        palindrome = False

if palindrome == False:
    print ("Not a palindrome")
else:
    print ("Is a palindrome")