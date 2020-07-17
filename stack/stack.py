"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.storage = []
#         self.size = len(self.storage)

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) == 0:
#             print('storage is empty fam')
#         else: 
#             return self.storage.pop()

from sll import LinkedList

class Stack:
    def __init__(self):
        self.storage = LinkedList()
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            print('storage is empty fam')
        else: 
            self.size -= 1
            return self.storage.remove_tail()





if True == True:
    test = Stack()
    an0= test.__len__()
    test.push(2)
    an1= test.__len__()
    test.push(45)
    an2= test.__len__()
    re1 = test.pop()
    test.push(5)
    test.push(4)
    test.push(3)
    test.push(2)
    test.push(1)
    order = test.storage
    re2 = test.pop()
    print(f"TESTING: \n expect zero: {an0} \n expect one: {an1} \n expect two: {an2} \n removing test returning forty-five: {re1} \n Testing order: {order} \n emoving test returning the one: {re2}")
