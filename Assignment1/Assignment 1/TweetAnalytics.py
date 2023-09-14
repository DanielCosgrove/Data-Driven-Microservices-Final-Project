import pandas as pd
import numpy as np
import redis
import datetime

data = pd.read_csv("data.csv").dropna()
shortest = 9999
longest = 0

#MAIN    
for line in data:

	print()
#	tweet = data["Tweet"]
#	print(tweet)
#	print(tweet.len())
#	conn.set("Tweet:"+ str(datetime.datetime.now()),tweet )

#	if(tweet.len() > longest):
#		longest = tweet.len()
#
#	if(tweet.len() < shortest):
#		shortest = tweet.len()
	
	
test_arr = ["Test","Testing","TEST"]

for i in test_arr:
    try:
        conn=redis.StrictRedis(host='redis',port=6379)
        conn.set("key"+ str(datetime.datetime.now()),i )
    except Exception as ex:
        print('Error: ',ex)
    





           
