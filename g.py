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
	
	authenticate("localhost:7474", user, password)
	
	graph = Graph("http://localhost:7474/db/data/");
	a = Node("regular", screen_name="a")
	b = Node("regular", screen_name="b")
	graph.create(a)
	graph.create(b)
	
	c = graph.find_one("regular", "screen_name", "razorbacks_ben")
	
	if not c:
		print "hellllooooooooo"
		
		#479-595-6676 jeremy

