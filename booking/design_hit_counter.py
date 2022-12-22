"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the
system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp
starts at 1.

It is possible that several hits arrive roughly at the same time.
"""


class HitCounter:
    def __init__(self, ts, hits):
        self.ts = [300]
        self.hits = [300]

    # Record a hit
    # Record a hit
    # @param timestamp - The current timestamp (in seconds granularity)
    def hit(self, timestamp):
        i = timestamp % 300
        if (self.ts[i] != timestamp):
            self.ts[i] = timestamp
            self.hits[i] = 1
        else:
            self.hits[i] += 1

    # Return the number of hits in the past 5 minutes
    # @param timestamp - The current timestamp (in seconds granularity)
    def get_hits(self, timestamp):
        result = 0
        for i in range(0, len(self.hits) - 1):
            if (timestamp - self.ts[i] < 300):
                result += self.hits[i]

        return result
    '''
    Your Hitcounter object will be instantiated and called as such
    
    '''