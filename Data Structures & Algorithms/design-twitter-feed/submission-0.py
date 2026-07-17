class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets_time = 0
    
    def creatingUser(self, userId: int):
        self.users[userId] = {
            "following": set(),
            "tweets": []
        }


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.creatingUser(userId)
            
        self.users[userId]["tweets"].append((self.tweets_time, tweetId))
        self.tweets_time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []

        heap = []

        # Include followed users and the user themself
        followed_users = self.users[userId]["following"] | {userId}

        for followed_user_id in followed_users:
            if followed_user_id not in self.users:
                continue

            for timestamp, tweet_id in self.users[followed_user_id]["tweets"]:
                heapq.heappush(heap, (timestamp, tweet_id))

                # Remove the oldest tweet
                if len(heap) > 10:
                    heapq.heappop(heap)

        # Heap pops oldest first, so reverse the result
        news_feed = []

        while heap:
            timestamp, tweet_id = heapq.heappop(heap)
            news_feed.append(tweet_id)

        return news_feed[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.creatingUser(followerId)
        self.users[followerId]["following"].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            return
        self.users[followerId]["following"].discard(followeeId)
        
