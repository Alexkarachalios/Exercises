import tweepy


consumer_key = 'mGRAQmAI1HASoWtgf5H5yD4Jd'
consumer_secret ='2k7CpUpArBTejF4UgEmkHfYUgSwhywKiBrEfATlZmgACA5sicr'
access_token = '775671340451921925-zu5xRPYnKZUV7zcKRhGnK5zGZzGC19m'
access_secret ='DqitlGs2NW79ewGaBvda3lNGEJiVrqrARnrp8EffmuZFf'
auth =tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


first=input('username 1:')
second=input('username 2:')

user1=api.get_user(first)
user2=api.get_user(second)

f=[]
s=[]

for friend in user1.followers():
    f.append(friend.screen_name)


for friend in user2.followers():
    s.append(friend.screen_name)


for item1 in f:
    for item2 in s:
        if item1 == item2:
            print ('Mutual followers:',item1)
            
#written with python 3.6
