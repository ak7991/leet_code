import bisect

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l_heap = [float("-inf")]
        self.r_heap = [float("inf")]
        self.med = []

    def apt_insert(self, arr, element):
        _idx = bisect.bisect_left(arr, element)
        arr.insert(_idx, element)
        return arr

    def addNum(self, num: int) -> None:
        if num < self.r_heap[0]:
            if self.l_heap[0] <= num <= self.l_heap[-1]:
                self.apt_insert(self.l_heap, num)
            else:
                self.apt_insert(self.med, num)
        else:
            self.apt_insert(self.r_heap, num)      
        # rebalance
        # skip
        if len(self.l_heap) == len(self.r_heap):
            pass
        elif len(self.l_heap) > len(self.r_heap):
            self.med.insert(0, self.l_heap.pop(-1))
        elif len(self.l_heap) < len(self.r_heap):
            self.med.append(self.r_heap.pop(0))
        else:
            pass
        if len(self.med) == 3:
            self.l_heap.append(self.med.pop(0))
            self.r_heap.insert(0, self.med.pop(1))


    def findMedian(self) -> float:
        return sum(self.med) / len(self.med)