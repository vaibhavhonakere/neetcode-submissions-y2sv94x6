class Twitter:

    def __init__(self):
        # have a mapping of people following one another (one map)
        self.follower_map = defaultdict(set)
        # Mapping of the of the person and their tweets
        self.follower_tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follower_tweets[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        users_following = self.follower_map[userId]
        users_following.add(userId)
        max_heap = [] # (tweet, index, user)
        for user in users_following:
            list_of_tweets = self.follower_tweets[user]
            if(len(list_of_tweets) > 0):
                heapq.heappush_max(max_heap, (list_of_tweets[-1], len(list_of_tweets) - 1, user))

        ret = []
        while(max_heap):
            entry, index, user = heapq.heappop_max(max_heap)
            ret.append(entry)
            if(len(ret) == 10):
                return ret
            index -= 1
            if(index >= 0):
                heapq.heappush_max(max_heap, (self.follower_tweets[user][index], index, user))

        return ret
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followeeId in self.follower_map[followerId]):
            self.follower_map[followerId].remove(followeeId)
        
