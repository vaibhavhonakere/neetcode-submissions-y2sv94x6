class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.timeMap):
            self.timeMap[key] = [(value, timestamp)]
        else:
            self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.timeMap):
            return ""
        left = 0
        right = len(self.timeMap[key]) - 1
        #print(left, right)
        store = ""
        while(left <= right):
            mid = (left + right) // 2
            if(self.timeMap[key][mid][1] == timestamp):
                return self.timeMap[key][mid][0]
            elif(self.timeMap[key][mid][1] < timestamp):
                store = self.timeMap[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return store