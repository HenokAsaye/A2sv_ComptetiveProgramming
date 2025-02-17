# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n+1)
        for i,j,k in bookings:
            ans[i-1]+=k
            ans[j] -=k
        print(ans)
        for a in range(1,len(ans)):
            ans[a] = ans[a-1]+ans[a]
        return ans[:n]
