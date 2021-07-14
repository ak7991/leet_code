import bisect

class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_right(self.bookings, start)
        j = bisect.bisect_left(self.bookings, end)
        # print(f"right bisecting {self.bookings} for {end} -> {bisect.bisect_right(self.bookings, end)}")
        # print(self.bookings, start, end, i, j)
        if i == j and i % 2 == 0:
            self.bookings.insert(j, end)
            self.bookings.insert(i, start)
            return True
        else:
            return False

        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)