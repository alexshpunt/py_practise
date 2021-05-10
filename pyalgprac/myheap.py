class MyHeap:
    def __init__(self) -> None:
        self.heap = [None]
    
    def __repr__(self) -> str:
        return self.heap[1:].__repr__()

    def __len__(self) -> int:
        return len(self.heap)-1

    def insert(self, x):
        self.heap.append(x)
        self.heapifyUp(len(self.heap) - 1)

    def takeMin(self):
        heap = self.heap
        if len(self) == 1:
            return heap.pop()

        min = heap[1]
        heap[1] = heap.pop()
        self.heapifyDown(1)
        return min

    def heapifyUp(self, i):
        heap = self.heap

        parent = heap[i // 2]
        if not parent:
            return

        if parent > heap[i]:
            heap[i // 2], heap[i] = heap[i], heap[i // 2]
        self.heapifyUp(i // 2)
        
    def heapifyDown(self, i):
        heap = self.heap 
        if i * 2 >= len(self.heap):
            return

        left = i*2 
        right = left + 1

        lChild = heap[left]
        try:
            rChild = heap[right]
        except IndexError:
            rChild = None

        minChild = left
        if rChild and lChild > rChild: 
            minChild = right 
        
        if heap[i] > minChild: 
            heap[i], heap[minChild] = heap[minChild], heap[i]
            self.heapifyDown(minChild)

def TestMyHeap():
    heap = MyHeap()

    for x in [10, 8, 2, 3, 1, 11, 45, 4, 8]:
        heap.insert(x)

    print(heap)
    while len(heap) > 0:
        print(heap.takeMin(), len(heap))