class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # for i, t in enumerate(tasks):
        #     t.append(i)
        # tasks.sort(key=lambda t: t[0])

        # res, minHeap = [], []
        # i, time = 0, tasks[0][0]

        # while minHeap or i < len(tasks):
        #     while i < len(tasks) and time >= tasks[i][0]:
        #         heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
        #         i += 1
        #     if not minHeap:
        #         time = tasks[i][0]
        #     else:
        #         procTime, index = heapq.heappop(minHeap)
        #         time += procTime
        #         res.append(index)
        # return res
        available = []
        pending = []
        for i, (enqueueTime, processTime) in enumerate(tasks):
            heapq.heappush(pending, (enqueueTime, processTime, i))

        time = 0
        res = []
        while pending or available:
            while pending and pending[0][0] <= time:
                enqueueTime, processTime, i = heapq.heappop(pending)
                heapq.heappush(available, (processTime, i))

            if not available:
                time = pending[0][0]
                # continue
            else:
                processTime, i = heapq.heappop(available)
                time += processTime
                res.append(i)

        return res