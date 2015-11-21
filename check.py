from tweepy import OAuthHandler
from tweepy import API, Cursor
import time
from py2neo import authenticate, Graph, Node, Relationship

access_token = "2768450545-t7s0uiSKZ8E82zqzxIL1PDy0L0a0FqqOzcLcO5k"
access_token_secret = "5DimJ3PzYYjXUDcKBeB9r6BQptwfDcxNycsE6mehozSCU"
consumer_key = "UpbIPbjpN6bjlFRLOA7OPRAg4"
consumer_secret = "jxUBvjL8UheS977wnAutaROcF6rBfRG9gq0VhM2OQKIEdMcs0l"

if __name__ == '__main__':

	user = "neo4j"
	password = "stupdi"
	
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	api = API(auth)
	
	temp = api.get_user("razorbacks_ben")
	
	print temp
	print temp.created_at
	print temp.location
	""""
	authenticate("localhost:7474", user, password)
	
	graph = Graph("http://localhost:7474/db/data/");
	a = Node("regular", screen_name="a")
	b = Node("regular", screen_name="b")
	graph.create(a)
	graph.create(b)
	
	c = graph.find_one("regular", "screen_name", "a")
	print c
	
	counter = 0;
	
	temp = api.get_user("Newsweek");
	print temp.followers_count
	print temp.friends_count
	print temp.screen_name
	"""
	counter = 0;
	while True:
		status = api.rate_limit_status()
		resources = status['resources']
		followers = resources['followers']
		f_list = followers['/followers/list']
		remaining = f_list['remaining']
		
		print remaining
		
		if remaining == 0:
			print "Sleeping... ";
			print "minutes passed: " + str(counter);
			counter += 1;
			time.sleep(60)
		else:
			print "Reset..."
			break;
			

