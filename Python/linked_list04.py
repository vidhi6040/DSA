class Node:
    def __init__(self, data=0):
        self.data = data
        self.next: Node = None

class LinkedList:

    #TODO: If a list, tuple or linked list is passed then it sould construct

#    def __init__(self, source=None):
#       if source is None:
#           self.start: Node = None
#       elif isinstance(list, source): 
#           for data in source:
#               self.add(data)
#       elif isinstance(tuple, source):
#           for data in source:
#               self.add(data)
#       elif isinstance(LinkedList, source):
#           self.merge(source)
                
    def __init__(self, *data):
        self.start: Node = None
        if len(data) == 0:
            self.start = None
        elif len(data) == 1:
            if isinstance(data[0], (list, tuple)):
                for d in data[0]:
                    self.add(d)
            elif isinstance(data[0], LinkedList):
                self.merge(data[0])
            else:
                new = Node(data[0])
                self.start(new)
        else:
            for d in data:
                self.add(d)

    #TODO: If already list has some elements then it sould caution and ask user like y/n then create 
    # by cleaning all existing data

    def create(self):
        if self.start is not None:
            opt = input('Do you want to delete all the existing data and create a new list [y/n]?... ')
            if opt == 'y':
                self.start = None
            else:
                raise Exception()
        ch = 'y'
        while ch=='y':
            d = int(input("\nEnter Data: "))
            new = Node(d)
            if self.start is None:
                self.start = new
            else:
                temp: Node = self.start
                while temp.next is not None:
                    temp = temp.next
                temp.next = new
            ch = input("Do you want more nodes [y/n]?... ")
            
    def add(self, data):
        new = Node(data)
        if self.start is None:
            self.start = new
        else:
            temp: Node = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new

    def disp(self):
        if self.start is None:
            print("\nNO DATA")
        else:
            temp: Node = self.start
            print("\nSTART :", end=" ")
            while temp is not None:
                print(f"{temp.data}", end=" ")
                temp = temp.next
            print(": END")

    #TODO: Define this as a property
    
    @property
    def Count(self):
        temp: Node = self.start
        n = 0
        while temp is not None:
            temp = temp.next
            n += 1
        return n
    # we can call it using p.Count
        
    def insert(self, data, position='last', index=1):
        new = Node(data)
        if position == 'last':
            if self.start is None:
                self.start = new
            else:
                temp: Node = self.start
                while temp.next is not None:
                    temp = temp.next
                temp.next = new
        elif position == 'first':
            if self.start is None:
                self.start = new
            else:
                new.next = self.start
                self.start = new
        elif position == 'any':
            if index <= 0 or index > (self.count() + 1):
                print("\nInsertion Failed! Invalid index, it should be between 1 to n+1")
            else:
                temp: Node = self.start
                i = 1
                while i < index - 1:
                    temp = temp.next
                    i += 1
                new.next = temp.next
                temp.next = new
    def merge(self, llist):
        if not isinstance(llist, LinkedList):
            print("\nMerge Failed! You must pass a LinkedList object")
        else:
            if self.start is None:
                self.start = llist.start
            else:
                temp: Node = self.start
                while temp.next is not None:
                    temp = temp.next
                temp.next = llist.start

    #TODO: Add few magic functions like __getitem__(), __setitem__(), __delitem__(), they are also
    # called as dunders. With this we can get/set and item like a list element p[3] = 200
    
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Key must be an integer!")
        else:
            if key < 0:
                key = key + self.Count
            if key < 0 or key >= self.Count:
                raise IndexError("Key is out of range")
            temp: Node = self.start
            i = 0
            while i < key:
                temp = temp.next
                i += 1
            return temp.data
        
    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Key must be an integer!")
        else:
            if key < 0:
                key = key + self.Count
            if key < 0 or key >= self.Count:
                raise IndexError("Key is out of range")
            temp: Node = self.start
            i = 0
            while i < key:
                temp = temp.next
                i += 1
            temp.data = value
            
    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Key must be an integer!")
        else:
            if key < 0:
                key = key + self.Count
            if key < 0 or key >= self.Count:
                raise IndexError("Key is out of range")
            temp: Node = self.start
            i = 0
            while i < key-1 and temp is not None:
                temp = temp.next
                i += 1
            temp.next = temp.next.next
            

def main():
    p = LinkedList()
    p.create()
    p.disp()
    p.add(500)
    p.disp()
    p.insert(400, 'any', 4)
    p.disp()
    # p.insert(700, 'any', -3)
    print(f"\nTotal Number of Nodes: {p.count()}")
    q = LinkedList()
    q.add(11)
    q.add(22)
    q.disp()
    p.merge(q)
    p.disp()
    r = [12, 23, 34, 45]
    p.merge(r)
    p.disp()
if __name__ == "__main__":
    main()