class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        lowerBound = t - 3000
        
        while(len(self.requests) != 0 and self.requests[0] < lowerBound):
            self.requests.pop(0)
        
        self.counter = len(self.requests)
        
        return self.counter

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)