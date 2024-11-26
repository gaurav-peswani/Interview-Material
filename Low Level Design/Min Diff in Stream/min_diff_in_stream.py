from collections import deque
from sortedcontainers import SortedList

class MinDiffInStream:

    def __init__(self, k: int):
        self.queue = deque()
        self.sorted_list = SortedList()
        self.max_size = k

    def push(self, x: int) -> int:
        if len(self.queue) == self.max_size:
            popped = self.queue.popleft()
            self.sorted_list.remove(popped)
        self.queue.append(x)
        self.sorted_list.add(x)
        print(self.sorted_list, self.queue)
        return self._min_difference()

    def _min_difference(self) -> int:
        if len(self.sorted_list) <= 1:
            return 0
        
        min_diff = float('inf')
        for i in range(len(self.sorted_list) - 1):
            min_diff = min(min_diff, abs(self.sorted_list[i + 1] - self.sorted_list[i]))
        return min_diff
    
if __name__ == "__main__":
    md = MinDiffInStream(k=4)

    print(md.push(1))
    print(md.push(2))
    print(md.push(8))
    print(md.push(4))
    print(md.push(7))
    print(md.push(9))
    print(md.push(8))
    print(md.push(7))
    print(md.push(11))



    