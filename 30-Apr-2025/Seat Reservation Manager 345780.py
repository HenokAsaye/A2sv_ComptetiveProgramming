# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.arr = deque()
        self.heaps = []
        for i in range(1, n + 1):  
            heapq.heappush(self.heaps, i)

    def reserve(self) -> int:
        seat = heapq.heappop(self.heaps)
        self.arr.append(seat)
        return seat
        
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heaps, seatNumber)



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)