from collections import defaultdict
import heapq
class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.followers = set()
        self.following = set()


class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = defaultdict(list)
        self.time = 0

    def fetch_or_add_user(self, user_id):
        if user_id not in self.users:
            self.users[user_id] = User(user_id)
        return self.users[user_id]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((tweetId, self.time))

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.fetch_or_add_user(userId)
        followers = user.following | {userId}
        curr_queue = []
        for follower in followers:
            n = len(self.tweets[follower])
            if n > 0:
                tweet_id, timestamp = self.tweets[follower][n - 1]
                heapq.heappush(curr_queue, (-timestamp, n - 1, tweet_id, follower))
        feed = []
        while len(feed) < 10 and curr_queue:
            _, idx, tweet_id, follower = heapq.heappop(curr_queue)
            feed.append(tweet_id)
            if idx > 0:
                tweet_id, timestamp = self.tweets[follower][idx - 1]
                heapq.heappush(curr_queue, (-timestamp, idx - 1, tweet_id, follower))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        follower = self.fetch_or_add_user(followerId)
        followee = self.fetch_or_add_user(followeeId)

        follower.following.add(followeeId)
        followee.followers.add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        follower = self.fetch_or_add_user(followerId)
        followee = self.fetch_or_add_user(followeeId)

        follower.following.discard(followeeId)
        followee.followers.discard(followerId)
