class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):

        new_node=Node(data)
        if self.head is None:
            self.head=Node(data)

            return
        temp=self.head
        while temp.next:
            temp=temp.next

        temp.next=new_node

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("none")
    def prime(self):
        temp=self.head
        count=0
        while temp:
            if temp.data%2==0:
                temp=temp.next
                print("not prime",end="->")

            else:
                temp=temp.next
                print("prime",end="->")
                count+=1

        print(None)
        print(count)
    def evensum(self):
        temp=self.head
        sum=0
        while temp:
            if temp.data%2==0:
                sum=sum+temp.data
            temp=temp.next
        return sum
l1=LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.display()
l1.prime()
l1.evensum()
print("sum of even numbers:",l1.evensum())