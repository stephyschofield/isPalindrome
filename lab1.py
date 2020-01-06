""" 
Stephanie Schofield
CIS 313 Fall 2019
Daniel Lowd
October 27, 2019

Determining if a string is a palindrome using a stack and queue. Implementation in python 3.
"""

class Node(object):
    def __init__(self, data = None, next = None):
        self.__data = data
        self.__next = next
            
    def setData(self, data):
        # Set the "data" data field to the corresponding input
        self.__data = data
    
    def setNext(self, next):
        # Set the "next" data field to the corresponding input
        self.__next = next

    def getData(self):
        # Return the "data" data field
        return self.__data

    def getNext(self):
        # return the "next" data field
        return self.__next

class Queue(object):
    def __init__(self):
        self.__head = None
        self.__tail = None
    
    def enqueue(self, newData):
        # Create a new node whose data is newData and whose next node is null
        # Update head and tail
        # Hint: Think about what's different for the first node added to the Queue
        newQueueNode = Node(newData, None)

        if self.isEmpty():
            self.__head = newQueueNode
            self.__tail = self.__head
        else:
            self.__tail.setNext(newQueueNode)
            self.__tail = newQueueNode
    
    def dequeue(self):
        #  Return the head of the Queue
        #  Update head
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        if self.isEmpty():
            return None
        else: 
            tempnode = self.__head
            self.__head = self.__head.getNext()
            tempnode.setNext(None)
            return tempnode.getData()
    
    def isEmpty(self):
        # Check if the Queue is empty
        return self.__head == None
    
    def printQueue(self):
        # Loop through your queue and print each Node's data
        tempnode = self.__head
        queue = []
        if self.isEmpty():
            return None
        else:
            while tempnode != None:
                queue.append(tempnode.getData())
                tempnode = tempnode.getNext()
            return queue

class Stack(object):
    def __init__(self):
        # We want to initialize our Stack to be empty
        # (ie) Set top as null
        self.top = None
    
    def push(self, newData):
        # We want to create a node whose data is newData and next node is top
        # Push this new node onto the stack
        # Update top
        newStackNode = Node(newData, self.top)
        if self.top == None:
            self.top = newStackNode
        else:
            tempnode = newStackNode
            tempnode.setNext(self.top)
            self.top = tempnode
    
    def pop(self):
        # Return the Node that currently represents the top of the stack
        # Update top
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        if self.isEmpty():
            return None
        else:
            popped = self.top
            self.top = self.top.getNext()
            popped.setNext(None)
            return popped.getData()

        
    def isEmpty(self):
        # Check if the Stack is empty
        return self.top == None
        
    def printStack(self):
        # Loop through your stack and print each Node's data
        tnode = self.top
        stack = []
        if self.isEmpty():
            return None
        else: 
            while tnode != None:
                stack.append(tnode.getData())
                tnode = tnode.getNext()
            return stack

def isPalindrome(s):
    # Use your Queue and Stack class to test wheather an input is a palendrome
    myStack = Stack() 
    myQueue = Queue()

    s = s.lower().replace(" ", "")
    for letter in s:
        myQueue.enqueue(letter)
        myStack.push(letter)

    while (myQueue.isEmpty() != True):
        queueItem = myQueue.dequeue()
        stackItem = myStack.pop()
 
        if (queueItem != stackItem):
            return False
    else:
        return True

    ## Helper function ##
    #print("stack data")
    #myStack.printStack()

    #print("queue data")
    #myQueue.printQueue()
