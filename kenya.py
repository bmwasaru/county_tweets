from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from keys import access_token
from keys import access_token_secret
from keys import consumer_key
from keys import consumer_secret


class StdOutListener(StreamListener):    
    # on success
    def on_data(self, data):
        print data
        return True

    # on failure
    def on_error(self, status):
    	print status

if __name__ == '__main__':
	listener = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, listener)
	# keywords list
	keywords = []
	# filter to capture county names from the counties list
	for county in open('counties.txt', 'r'):
		keywords.append(county)
	
	stream.filter(track=keywords)