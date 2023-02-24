class TweetCounts:

    def __init__(self):
        self.h = collections.defaultdict(list) # key is #tweet, value is a list of time
        self.map = {'minute': 60, 'hour': 3600, 'day': 86400}
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.h[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        slot = int(math.ceil((endTime - startTime + 1) / self.map[freq]))
        res = [0] * slot
        for time in self.h[tweetName]:
            if startTime <= time <= endTime: # time in the selected range
                res[(time - startTime) // self.map[freq]] += 1
        return res
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)