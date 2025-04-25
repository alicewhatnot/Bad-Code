class circularQueue: 
    def __init__ (self,maxSize):
        '''Constructing the Queue'''
        self.front = 0
        self.rear = -1
        self.maxSize = maxSize
        self.Q = [0]*maxSize
        self.size = 0
        
    def isFull(self):
        '''Check if full'''
        return (self.size == self.maxSize)
    
    def isEmpty(self):
        '''Check if empty'''
        return (self.size == 0) 
            
    def enQueue(self,newItem):
        '''Append to the queue'''
        if self.isFull():
            print ("\nQueue full")
            return
        else:
            self.rear = (self.rear + 1) % self.maxSize
            self.Q[self.rear] = newItem
            self.size = self.size + 1
            print (f"\n{newItem} added.")
            
    def deQueue(self):
        '''Take an item from front of queue'''
        if self.isEmpty():
            print ("\nnull - empty queue\n")
            return
        else:
            item = self.Q[self.front]
            self.front = (self.front + 1) % self.maxSize
            self.size = self.size - 1
        print (f"\n{item} removed.\n")
    
    def show(self):
        '''Output the contents of the queue'''
        if self.isEmpty():
            print("\nQueue is empty")
            return
        index = self.front
        for i in range (self.size):
            print (self.Q[index], end=", ")
            index = (index + 1) % self.maxSize

queue1 = circularQueue(128)
queue2 = circularQueue(128)
queue3 = circularQueue(128)

def enPriorityQueue(queue1,queue2,queue3):
    userItem = str(input("Enter item to add to the queue: "))
    itemPriority = str(input("Enter the item priority - first, second or third: "))
    if itemPriority == "1":
        queue1.enQueue(userItem)
    elif itemPriority == "2":
        queue2.enQueue(userItem)
    elif itemPriority == "3":
        queue3.enQueue(userItem)


def dePriorityQueue(queue1,queue2,queue3):
    if (queue1.isEmpty == False):
        queue1.deQueue()
    elif (queue2.isEmpty == False):
        queue2.deQueue()
    elif (queue3.isEmpty == False):
        queue3.deQueue()
    else:
        print ("No items in queue.")
        
def printPriorityQueue(queue1,queue2,queue3):
    queue1.show()
    queue2.show()
    queue3.show()
    
while True:
    userChoice = str(input("\nEnter 1 to enQueue \n"
                          "Enter 2 to deQueue \n"
                         "Enter 3 to show the queue \n"
                          "Choice: "))
    if userChoice == "1":
       enPriorityQueue(queue1,queue2,queue3)
    elif userChoice == "2":
       dePriorityQueue(queue1,queue2,queue3)
    elif userChoice == "3":
       printPriorityQueue(queue1,queue2,queue3)
    else:
       print ("You clearly did not enter 1, 2 or 3.")

