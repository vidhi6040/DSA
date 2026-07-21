class Node:
    def __init__(self, dat=0):
        self.data = dat
        self.next : Node = None
    
def create():
    d = int(input("Enter Data: "))
    return Node(d)
def insert(start, datt, pos='first', valid_pos=0):
    new = Node(datt)
    if pos == 'first':
        new.next = start
        return new
    elif pos == 'last':
        if start is None:
            return new
        temp = start
        while temp.next is not None:
            temp = temp.next
        temp.next = new
        return start
    elif pos == 'any':
        if start is None:
            return new
        temp = start
        i = 1
        while i < valid_pos-1 and temp.next is not None:
            temp = temp.next
            i += 1
        new.next = temp.next
        temp.next = new
        return start  
    else:
        print("Invalid position declaration")
        return start
    
def delete(start, pos='first', valid_pos=0):
    if pos == 'first':
        return start.next
    elif pos == 'last':
        temp = start
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        return start
    elif pos == 'any':
        temp = start
        n = 1
        while n < valid_pos-1 and temp.next.next is not None:
            temp = temp.next
            n += 1
        temp.next = temp.next.next
        return start
    else:
        print("Invalid position declaration")
        return start

def disp(start):
    print()
    print("Start", end=" -> ")
    while start:
        print(start.data, end=" -> ")
        start = start.next
    print("End")
def main():
    start : Node = None
    new : Node = None
    ch = 'y'
    while(ch == 'y'):
        new = create()
        if start is None:
            start = new
        else:
            temp : Node = start
            while(temp.next is not None):
                temp = temp.next
            temp.next = new
        ch = input('Do you want more node? [y/n]')
    start = insert(start, 100, )
    start = insert(start, 300)
    start = insert(start, 200, 3)
    disp(start)    

if __name__ == "__main__":
    main()
    
#insert at first and at last