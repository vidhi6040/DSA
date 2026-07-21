class Node:
    def __init__(self, dat=0):
        self.data = dat
        self.next : Node = None
    
def create():
    d = int(input("Enter Data: "))
    return Node(d)

def insert_first(start, dat):
    new = Node(dat)
    new.next = start
    return new

def insert_last(start, dat):
    new = Node(dat)
    temp = start
    while temp.next is not None:
        temp = temp.next
    temp.next = new
    return start

def insert_any(start, dat, n):
    new = Node(dat)
    temp = start
    i = 1
    while i < n-1:
        temp = temp.next
        i += 1
    new.next = temp.next
    temp.next = new
    return start    

def delete_first(start):
    return start.next

def delete_last(start):
    temp = start
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return start

def delete_n(start, n):
    temp = start
    i = 1
    while i < n-1 and temp.next is not None:
        i += 1
        temp = temp.next
    temp.next = temp.next.next
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
    start = insert_first(start, 100)
    start = insert_last(start, 300)
    start = insert_any(start, 200, 3)
    disp(start)    

if __name__ == "__main__":
    main()
    
#insert at first and at last