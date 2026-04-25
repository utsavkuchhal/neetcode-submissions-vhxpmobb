class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.followers = set()
        self.following = set()


class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = []
        self.tweet_map = {}

    def fetch_or_add_user(self, user_id):
        if user_id not in self.users:
            self.users[user_id] = User(user_id)
        return self.users[user_id]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append(tweetId)
        self.tweet_map[tweetId] = userId

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.fetch_or_add_user(userId)
        results = []
        for i in range(len(self.tweets) - 1, -1, -1):
            tweet_id = self.tweets[i]
            if (self.tweet_map[tweet_id] == userId) or (
                self.tweet_map[tweet_id] in user.following
            ):
                results.append(tweet_id)
            if len(results) == 10:
                break
        return results

    def follow(self, followerId: int, followeeId: int) -> None:
        follower = self.fetch_or_add_user(followerId)
        followee = self.fetch_or_add_user(followeeId)
        followee.followers.add(followeeId)
        follower.following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follower = self.fetch_or_add_user(followerId)
        followee = self.fetch_or_add_user(followeeId)
        if followeeId in followee.followers:
            followee.followers.remove(followeeId)
            follower.following.remove(followeeId)
