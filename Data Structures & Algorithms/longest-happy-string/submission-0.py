class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        max_heap = []

        for count, char in [(a, "a"), (b, "b"), (c, "c")]:
            if count != 0:
                heapq.heappush_max(max_heap, (count, char))

        ret = ""
        while(max_heap):
            cnt, ch = heapq.heappop_max(max_heap)
            if(len(ret) > 1 and ret[-2] == ret[-1] == ch):
                if(max_heap):
                    cnt_2, ch_2 = heapq.heappop_max(max_heap)
                    ret += ch_2
                    cnt_2 -= 1
                    if(cnt_2 > 0):
                        heapq.heappush_max(max_heap, (cnt_2, ch_2))
                    heapq.heappush_max(max_heap, (cnt, ch))
                else:
                    break
            else:
                ret += ch
                cnt -= 1
                if(cnt > 0):
                    heapq.heappush_max(max_heap, (cnt, ch))
        
        return ret
