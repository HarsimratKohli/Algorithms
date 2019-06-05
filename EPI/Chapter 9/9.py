class queue:
    def __init__(self):
        self.q=[]

    def insert(self,val):
        self.q.append(val)
    def remove(self):
        self.q.pop(0)
    def print(self):
        print(self.q)

q=queue()
q.insert(1)
q.insert(2)
q.insert(3)
q.print()
q.remove()
q.print()
