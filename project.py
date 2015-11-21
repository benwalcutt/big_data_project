from tweepy import OAuthHandler
from tweepy import API, Cursor
import time
from py2neo import authenticate, Graph, Node, Relationship

db_string = "http://localhost:7474"
user = "neo4j"
password = "stupdi"

access_token = "2768450545-t7s0uiSKZ8E82zqzxIL1PDy0L0a0FqqOzcLcO5k"
access_token_secret = "5DimJ3PzYYjXUDcKBeB9r6BQptwfDcxNycsE6mehozSCU"
consumer_key = "UpbIPbjpN6bjlFRLOA7OPRAg4"
consumer_secret = "jxUBvjL8UheS977wnAutaROcF6rBfRG9gq0VhM2OQKIEdMcs0l"

if __name__ == '__main__':
	to_be_networked = ['razorbacks_ben'];
	added = [];
	
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	authenticate("localhost:7474", user, password)
	
	graph = Graph(db_string+"/db/data/");
	
	api = API(auth);
	log = open("out.txt", "w");
	f = open("added.txt", "r");
	for line in f:
		added.append(line);
	
	f.close();
	
	counter = 0;
	
	for user in to_be_networked:
		if counter > 1000000:
			break;
			
		if user in added:
			print "Already added " + user + ". Skipping...";
			continue;
		
		print "inspecting " + user;
		log.write(user+"\n")
		added.append(user)
		f = open("added.txt", "a");
		f.write(user);
		f.write('\n');
		f.close();
		'''
		for i in Cursor(api.followers, id=user).items():
			print "adding " + i.screen_name;
			f.write("\t"+i.screen_name+"\n");
			to_be_networked.append(i.screen_name);
		'''
		while True:
		
			try:
				temp_user = api.get_user(user);
				temp_ratio = float(temp_user.followers_count) / float(temp_user.friends_count);
				
				base_node = graph.find_one("regular", "screen_name", user);
				
				if not base_node:
					base_node = graph.find_one("verified", "screen_name", user);
					
				if not base_node:
					base_node = graph.find_one("cautious", "screen_name", user);
				
				if not base_node:				
					if temp_user.verified:
						base_node = Node("verified", screen_name=user, ratio=temp_ratio, tweets=temp_user.statuses_count, created=temp_user.created_at, followers=temp_user.followers_count, following=temp_user.friends_count, location=temp_user.location);
					else:
						if temp_ratio < 0.01:
							base_node = Node("cautious", screen_name=user, ratio=temp_ratio, tweets=temp_user.statuses_count, created=temp_user.created_at, followers=temp_user.followers_count, following=temp_user.friends_count, location=temp_user.location);
						else:
							base_node = Node("regular", screen_name=user, ratio=temp_ratio, tweets=temp_user.statuses_count, created=temp_user.created_at, followers=temp_user.followers_count, following=temp_user.friends_count, location=temp_user.location);
						
					
					graph.create(base_node);
				
				
				for i in Cursor(api.followers, id=user).items():
					print "adding " + i.screen_name;
					log.write("\t"+i.screen_name+"\n");
					to_be_networked.append(i.screen_name);
					
					temp_ratio = float(i.followers_count) / float(i.friends_count);
					
					friend_node = graph.find_one("regular", "screen_name", i.screen_name);
					
					if not friend_node:
						friend_node = graph.find_one("verified", "screen_name", i.screen_name);
						
					if not friend_node:
						friend_node = graph.find_one("cautious", "screen_name", i.screen_name);
					
					if not friend_node:
						if i.verified:
							friend_node = Node("verified", screen_name=i.screen_name, ratio=temp_ratio, tweets=i.statuses_count, created=i.created_at, followers=i.followers_count, following=i.friends_count, location=i.location);
						else:
							if temp_ratio < 0.01:
								friend_node = Node("cautious", screen_name=i.screen_name, ratio=temp_ratio, tweets=i.statuses_count, created=i.created_at, followers=i.followers_count, following=i.friends_count, location=i.location);
							else:
								friend_node = Node("regular", screen_name=i.screen_name, ratio=temp_ratio, tweets=i.statuses_count, created=i.created_at, followers=i.followers_count, following=i.friends_count, location=i.location);
						
					r = Relationship(friend_node, "Follows", base_node);
					graph.create(r);
			except:
				print "Sleeping...";
				time.sleep(60 * 16);
			
			break;
		
		
		counter += 1;
	
	for i in to_be_networked:
		print i;
	
	log.close()
	
	
	