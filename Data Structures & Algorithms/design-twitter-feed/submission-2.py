class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.last_tweet_id = 0
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.last_tweet_id, tweetId))
        self.last_tweet_id += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = self.tweets[userId][:] # start by adding self tweets
        
        for f in self.following[userId]:
            all_tweets.extend(self.tweets[f])

        all_tweets.sort(key=lambda t: -t[0])
        return [t for _, t in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
