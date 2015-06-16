import json
import re

import pandas as pd
import matplotlib.pyplot as plt

data = 'data/kenya_data.txt'

def county_in_text(county, text):
	text = text.lower()
	match = re.search(coun, text)
	if match:
		return True
	else:
		return False

tweets_data = []
for line in open(data, 'r'):
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		continue

tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)