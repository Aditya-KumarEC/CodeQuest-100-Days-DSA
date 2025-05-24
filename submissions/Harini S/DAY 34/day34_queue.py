class Queue_new:
    def __init__(self,size):
        self.size=size
        self.Queue_new=[None]*size
        self.front=-1
        self.rear=-1
    def enqueue(self,value):
        if self.rear<self.size-1:
            if self.front==-1:
                self.front=0
            self.rear+=1
            self.Queue_new[self.rear]=value
        else:
            print("Queue overflow")
    
    def dequeue(self):
        if self.front==-1 or self.front>self.rear:
            print("Queue underflow")
        else:
            self.Queue_new[self.front]=None
            self.front+=1
    
    def display(self):
        if self.front==-1 or self.front>self.rear: print("Queue underflow")
        else:
            for i in self.Queue_new[self.front:self.rear+1]: print(i,end=" ")
lis=list(map(int,input("Input: ").split()))
deq=int(input("Dequeue: "))
q=Queue_new(len(lis))
for i in lis: q.enqueue(i)
for i in range(deq): q.dequeue()
print("Remaining Queue:",end=" ")
q.display()       