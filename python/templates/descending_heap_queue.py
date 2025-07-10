from heapq import heappush as hpush
from heapq import heappop as hpop

class Descending_HeapQueue:
    def __init__(self, hq=[]):
        self.hq = []
        for i in hq:
            self.push(i)
    def push(self, n):
        hpush(self.hq, -n)
    def pop(self):
        return -hpop(self.hq)
    def __str__(self):
        return [-i for i in self.hq].__str__()

dhq = Descending_HeapQueue([8, 6, 2, 1, 5, 7, 4, 3])
print(dhq)
print(dhq.pop())
print(dhq)
print(dhq.pop())
print(dhq)
