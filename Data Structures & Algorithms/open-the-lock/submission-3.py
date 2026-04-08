class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        deadends_set = set(deadends)

        def find_next_slot(slot):
            new_slots = []
            for i, num in enumerate(slot):
                new_num = (int(num) + 1) % 10
                str_num = slot[:i] + str(new_num) + slot[i+1:]
                new_slots.append(str_num)
                new_num = ((int(num) - 1) + 10) % 10
                str_num = slot[:i] + str(new_num) + slot[i+1:]
                new_slots.append(str_num)
            
            return new_slots


        queue = deque()
        queue.append(["0000", 0])
        while(queue):
            lock, turns = queue.popleft()
            if(lock in deadends_set):
                continue
            
            if(lock == target):
                return turns
            
            deadends_set.add(lock)
            for new_lock in find_next_slot(lock):
                if(new_lock not in deadends_set):

                    queue.append([new_lock, turns + 1])

        return -1

