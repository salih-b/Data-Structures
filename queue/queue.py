"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) == 0:
            print('storage is empty fam')
        else: 
            return self.storage.pop(0)

# if True == True:
#     test = Queue()
#     test.enqueue(2)
#     test.enqueue(45)
#     an1= test.__len__()
#     re1 = test.dequeue()
#     an2 = test.__len__()
#     print(f"TESTING: \n answer one: {an1} \n answer two: {an2} \n removing test returning two: {re1}")
