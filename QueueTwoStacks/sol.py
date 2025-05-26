import sys

class StackQ:
    
    def __init__(self):
        self.stackIn = []
        self.stackOut = []
    def Dequeue(self):
        self.correct_distribution()
        return self.stackOut.pop()
    def Enqueue(self, ele):
        self.stackIn.append(ele)
    def getHead(self):
        self.correct_distribution()
        print(self.stackOut[-1])
    def correct_distribution(self):
        if self.stackOut:
            return
        while self.stackIn:
            self.stackOut.append(self.stackIn.pop())


Q = StackQ()
first_iter = False

for _ in range(int(sys.stdin.readline())):
    query = input().split()
    
    match int(query[0]):
        case 1:
            Q.Enqueue(query[1])
        case 2:
            Q.Dequeue()
        case 3:
            Q.getHead()

    
        
        