import tweepy
from tweepy import OAuthHandler

consumer_key = 'GX7lOCXw83OazopRcuIaZOmTs'
consumer_secret = 'NFb9XSp3fcuN6ZnFCpHqndDrg9tV4XKmpCW7XRC7tKtVrDQY2M'
access_token = '835182701636378624-O4Efhti4V22D8XA1Pbf0SiGxypMPOrk'
access_secret = '9sv3RZBdVheF8vl4iv91XXXnRmgzdKbAU0jkV7TbnviXr'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
print "I'm using python to mine twitter!"
