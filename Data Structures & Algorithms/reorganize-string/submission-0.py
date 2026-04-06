class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq_count = Counter(s)
        max_heap = []

        for k, v in freq_count.items():
           heapq.heappush_max(max_heap, (v,k))

        ret = ""
        while(max_heap):
            cnt, ch = heapq.heappop_max(max_heap)
            if(len(ret) > 0 and ret[-1] == ch):
                # print(max_heap, ret, cnt, ch)
                if(max_heap):
                    cnt_2, ch_2 = heapq.heappop_max(max_heap)
                    ret += ch_2
                    cnt_2 -= 1
                    if(cnt_2 > 0):
                        heapq.heappush_max(max_heap, (cnt_2, ch_2))
                    heapq.heappush_max(max_heap, (cnt, ch))
                else:
                    return ""
            else:
                ret += ch
                cnt -= 1
                if(cnt > 0):
                    heapq.heappush_max(max_heap, (cnt, ch))
        
        return ret
