#constructor with 3 components
class Node:
    def __init__ (self,data):
        self.data = data 
        self.next = None
        self.prev = None 
    
    # gets our data form the node 

    def get_data(self):
        return self.data

    # get_next , gets the next data 

    def get_next(self):
        return self.next
    
#doubly linked class

class DoublyLinkedList:
    def __init__ (self):
        self.head = None

    # methods 

    # takes data , creates node and adds it to the end
    # Then takes that new node and appropriatley positions it while manipulating the directional of the nodes  

    def append(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    # takes data , creates node and put it in the front
    #  then takes that new node and appropriatley positions it while manipulating the directional of the nodes     

    def prepend(self,data):
        if self. head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    # this will display our list

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

# append right ( key rpresents the element that we are adding to the right of) with a lot of positional adjustments of directional of nodes

    def add_after_node(self,key,data):
        cur = self.head
        while cur : 
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next


    # append left ( key rpresents the element that we are adding to the left of ) with a lot of positional adjustments of directional of nodes

    def add_before_node(self,key,data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
               self.prepend(data)
               return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
            cur = cur.next 

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # This is when the node I want to remove is the head , therefore left with zero nodes
                if not cur.next:
                    cur = None 
                    self.head = None
                    return

                # this is for when there is the head node along with a finite amount of nodes , but I only want to remove the head node
                else:
                    # this includes the next and previouse pointers
                    nxt = cur.next
                    cur.next = None 
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return 

            elif cur.data == key:
                # This is the pop out of the next node method i.e pop right 
                if cur.next:
                    nxt = cur.next 
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None 
                    cur.prev = None
                    cur = None
                    return

                # removing last node in list 
                else:
                    prev = cur.prev 
                    prev.next = None 
                    cur.prev = None 
                    cur = None 
                    return 
            cur = cur.next


    def findNode(self,value):

       curr = self.head
       while curr:
           if curr.get_data() == value:
               return print('We Found your Node')
           curr = curr.get_next()
       return print('This Node doesnt exist')



#Tester

if __name__ == '__main__':


    DLL = DoublyLinkedList()


    
    DLL.append(1)
    DLL.append(2)
    DLL.append(3)
    DLL.append(4)
    DLL.append(5)
    DLL.append(6)
    DLL.append(7)
    DLL.append(8)
    DLL.append(9)
    DLL.prepend(29)


    
    DLL.add_before_node(4,11)
    DLL.add_before_node(1,.5)
    
    DLL.add_after_node(4,25)
    
    DLL.delete(2)
    DLL.delete(3)
    
    (DLL.findNode(5))

    DLL.print_list()
