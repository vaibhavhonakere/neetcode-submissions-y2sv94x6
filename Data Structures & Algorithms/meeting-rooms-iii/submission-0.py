class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        used = [] # (end_time, room_number)
        count = [0]*n

        for start, end in meetings:
            while(used and used[0][0] <= start):
                _, room_num = heapq.heappop(used)
                heapq.heappush(available, room_num)
            
            # If there is no room available 
            if(not(available)):
                e, room_num = heapq.heappop(used)
                end = (end - start) + e
                heapq.heappush(available, room_num)
            
            # If there is a room available
            room_num = heapq.heappop(available)
            heapq.heappush(used, (end, room_num))
            count[room_num] += 1

        return count.index(max(count))