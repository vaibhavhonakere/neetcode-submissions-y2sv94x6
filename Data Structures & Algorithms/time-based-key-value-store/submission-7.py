class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.mapping):
            self.mapping[key] = [[timestamp, value]]
        else:
            self.mapping[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.mapping):
            return ""
        elements = self.mapping[key]
        left = 0
        right = len(elements) - 1
        ret = ""
        while(left <= right):
            mid = (left + right) // 2
            if(elements[mid][0] <= timestamp):
                ret = elements[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return ret


