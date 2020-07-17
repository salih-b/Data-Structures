"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
        
    def get_value(self):
        return self.value
​
    def get_next(self):
        return self.next
​
    def set_next(self, new_next):
        self.next = new_next
​    
    def get_prev(self):
        return self.prev
​
    def set_prev(self, new_prev):
        self.prev = new_prev
​ 
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        pass
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return

        if not self.head.get_next():
            head = self.head
            self.head = None 
            self.tail = None 
            return head.get_value()

        val = self.head.get_value()

        self.head = self.head.get_next()

        return val
​
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
​
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return
		
		if self.head is self.tail:
			value = self.head.get_value()
			self.head = None
			self.tail = None
			return value

        current = self.head 
​
        while current.get_next() is not self.tail:
            current = current.get_next()

        val = self.tail.get_value() 

        self.tail = current

		self.tail.next = None

        return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is head and self.tail is node:
            self.head = None
            self.tail = None
        node.prev.next = node.next
        node.next.prev = node.prev
        node = None

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.get_value()
        current = self.head.get_next()

        while current:

            if current.get_value() > max_value:
                max_value = current.get_value()

            current = current.get_next()

        return max_value