class Node:
    def __init__(self, data):
        self.data = data
        self.next : Node = None
    
class LinkedList:
    def __init__(self):
        self.start = None
    
    def create(self):
        ch = 'y'
        while(ch == 'y'):
            d = int(input("Enter Data: "))
            new = Node(d)
            if self.start is None:
                self.start = new
            else:
                temp : Node = self.start
                while temp.next is not None:
                    temp = temp.next
                temp.next = new
            ch = input("Do you want more nodes [y/n]? ")
            
    def disp(self):
        if self.start is None:
            print("No node found")
        else:
            temp : Node = self.start
            print()
            print("Start", end=" -> ") 
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("End")
            
    def add(self, data):
        new = Node(data)
        if self.start is None:
            self.start = new
        else:
            temp : Node = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new
    
    def count(self):
        temp : Node = self.start
        c = 0
        while temp:
            temp = temp.next
            c += 1
        return c
        
    def insert(self, data, position='last', index=1):
        new = Node(data)
        
        if position == 'first':
            if self.start is None:
                self.start = new
            else: 
                new.next = self.start
                self.start = new
        elif position == 'last':
            if self.start is None:
                self.start = new
            else:
                temp : Node = self.start
                while temp.next is not None:
                    temp = temp.next
                temp.next = new
        elif position == 'any':
            if index <= 0 or index > (self.count() + 1):
                raise IndexError("Insertion Failed! Invalid index, it should be in between 1 to ", self.count())
            else: 
                temp : Node = self.start
                i = 1
                while i < index - 1:
                    temp = temp.next
                    i += 1
                new.next = temp.next
                temp.next = new
        else:
            raise ValueError("Invalid Position")
    
    def merge(self, list):
            
    
def main():
    p = LinkedList()
    # p.create()
    # p.disp()
    p.add(100)
    p.add(100)
    p.add(400)
    p.add(300)
    p.disp()
    p.insert(200, 'any', 4)
    p.disp()
    print("No. of nodes:", p.count())
        
if __name__ == "__main__":
    main()