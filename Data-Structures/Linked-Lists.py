
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
    
    def get_data(self):
        return self.val
    
    def set_data(self, val):
        self.val = val
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
class LinkedList(object):
    def __init__(self, head=None): #initialise values of instance members for object
        self.head = head
        self.count = 0
    
    def get_count(self):
        return self.count

    # creates and inserts new node 
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1
    
    # find the first item with a given value
    def find(self, val):
        item = self.head
        while(item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None
    
    # deletes an item at given index 
    def deleteAt(self, idx):
        if idx > self.count-1:
            return
    
    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

# creates a linked list and insert items
itemlist = LinkedList()
itemlist.insert (20)
itemlist.insert (50)
itemlist.insert (24)
itemlist.insert (29)
itemlist.dump_list()

print("item count: ", itemlist.get_count())
print("finding item: ", itemlist.find(24))
print ("finding item: ", itemlist.find(29))

# delete an item
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(20))
itemlist.dump_list()