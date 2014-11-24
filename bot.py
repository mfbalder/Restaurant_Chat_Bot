import time
from nltk.corpus import stopwords
import model
from sqlalchemy import or_, and_
import psycopg2

dbconn = psycopg2.connect('dbname=restaurantrec host=localhost port=5432')
cursor = dbconn.cursor()

stopword_list = stopwords.words("english")

city = None
question_path = []
query_filters = []

query = "SELECT r.name, c.category FROM restaurants AS r join categories AS c ON r.id=c.business_id"

d = {
	1: {
		'return': 'question',
		'bot_statement': 'What city are you in?',
		'branches': {
			'answer': [2, " WHERE r.city = '?'", "where", None]
		}
	},
	2: {
		'return': 'question',
		'bot_statement': 'Are you hungry?',
		'branches': {
			('yes', 'ya', 'yeah', 'sure', 'definitely'): [3, " AND EXISTS(SELECT 1 FROM categories AS c1 WHERE c1.business_id=r.id AND c1.category NOT IN('Bars', 'Breweries', 'Coffee & Tea', 'Dive Bars', 'Sports Bars', 'Cafes', 'Tea Rooms', 'Wine Bars', 'Pubs'))", "add_to_query", 'c1'],
			('no', 'nope', 'nah', 'not'): [4, " AND EXISTS(SELECT 1 FROM categories AS c1 WHERE c1.business_id=r.id AND c1.category IN ('Bars', 'Breweries', 'Coffee & Tea', 'Dive Bars', 'Sports Bars', 'Cafes', 'Tea Rooms', 'Wine Bars', 'Pubs'))", 'add_to_query', 'c1']
		}
	},
	3: {
		'return': 'question',
		'bot_statement': 'Snack or meal?',
		'branches': {
			('snack',): [6, " AND EXISTS(SELECT 1 FROM categories as c2 WHERE c2.business_id=r.id AND c2.category IN ('Bakeries', 'Ice Cream & Frozen Yogurt', 'Donuts', 'Cafes', 'Candy Stores', 'Desserts'))", 'add_to_query', "c2"],
			('meal',): [5, " AND EXISTS(SELECT 1 FROM categories as c2 WHERE c2.business_id=r.id AND c2.category IN ('Restaurants'))", "add_to_query", None]
		}
	},
	4: {
		'return': 'question',
		'bot_statement': 'Ok then. Is a stiff drink in order?',
		'branches': {
			('yes', 'ya', 'yeah', 'sure', 'definitely', 'yessir'): [10, " AND EXISTS(SELECT 1 FROM categories as c3 WHERE c3.business_id=r.id AND c3.category IN ('Bars', 'Breweries', 'Dive Bars', 'Sports Bars', 'Wine Bars', 'Pubs'))", "add_to_query", None],
			('no', 'nope', 'nah', 'not'): [11, " AND EXISTS(SELECT 1 FROM categories as c3 WHERE c3.business_id=r.id AND c3.category IN ('Coffee & Tea', 'Cafes', 'Tea Rooms'))", "add_to_query", None]
		}
	},
	5: {
		'return': 'question',
		'bot_statement': 'Are we thinking breakfast, lunch or dinner?',
		'branches': {
			('breakfast', 'brunch'): [8, " AND EXISTS(SELECT 1 FROM categories as c4 WHERE c4.business_id=r.id AND c4.category='Breakfast & Brunch')", "add_to_query"],
			('lunch',): [7, " AND r.lunch=True", "add_to_query"],
			('dinner',): [7, " AND r.dinner=True", "add_to_query"]
		}
	},
	6: {
		'return': 'question',
		'bot_statement': 0#QUERY*****
	},
	7: {
		'return': 'question',
		'bot_statement': 'Eat in, take out, or delivery?',
		'branches': {
			('eat in', 'in'): [8],
			('take out', 'tk', 'out', 'pick up'): [8, " AND r.takeout=True", "add_to_query"],
			('delivery', 'deliver', 'delivered'): [8, " AND r.delivery=True", "add_to_query"],
			("LAZY",): [8, " AND r.drive_thru=True", "add_to_query"]
		}
	},
	8: {
		'return': 'question',
		'bot_statement': 'What about dietary concerns? Gluten? Soy? Vegan? Etc.?',
		'branches': {
			('nope', 'no', 'nah', 'none', 'negative'): [9],
			('vegetarian',): [9, " AND r.vegetarian=True", "add_to_query"],
			('vegan',): [9, " AND r.vegan=True", "add_to_query"],
			('gf', 'gluten', 'gluten-free'): [9, " AND r.gluten_free=True", "add_to_query"],
			('soy',): [9, " AND r.soy_free=True", "add_to_query"],
			('halal',): [9, " AND r.halal=True", "add_to_query"]
		}
	},
	9: {
		'return': 'question',
		'bot_statement': "And last but not least, what's your price range?",
		'branches': {

		}
	},
	10: {
		'return': 'question',
		'bot_statement': 'Righto, bar it is! What kind of vibe were we thinkin? Romantic? Intimate...? Chill yo?',
		'branches': {
			('intimate',): 0,####QUERY,
			('romantic',): [12],
			('chill', 'casual'): [13]
		}
	},
	11: {
		'return': 'question',
		'bot_statement': 'Do you have a preference for coffee or tea?\nTea, right? You know you like tea! (Tea.)',
		'branches': {
			('cafe', 'coffee', 'cappuccino'): 0,###########,
			('tea', 'leaf', 'leaves'): 0,#######,
			('nah', 'nope', 'no preference', "don't care", 'negative'): 0######
		}

	},
	12: {

	}
}




def run_query(data_dict, data_attr, value):
	data_dict.setdefault(data, value)

def generate_query(queryobj, listoffilters):
	l = ""
	for f in listoffilters:
		l += ".filter(l)"

	return l


def traverse_questions(last_state, user_answer):
	"""last state --> the state that a question was just asked from (int)
	   user_answer --> the user's answer to that question (str)

	   Checks that state's branches to see which of them match the answer.
	   Gets the next state from that branch.
	   Adds that state to the list tracking the path of states.

	   Returns the next state"""

	global question_path
	global query
	global join_half
	global where_half
	global cursor



	if last_state == 0:
		return d[1]['bot_statement']

	if last_state == 1:
		next_state = d[1]['branches']['answer'][0]
		query_piece = d[1]['branches']['answer'][1].replace('?', user_answer)
		query = query + query_piece
		cursor.execute(query)
		return next_state

	answer = user_answer.split()
	for branch in d[locals()['last_state']]['branches']:
			for each in branch:
				if each in clean:
					print each
					next_state = d[locals()['last_state']]['branches'][locals()['branch']][0]
					print "next state: ", next_state
					answer_branch = branch
					question_path.append((last_state, answer_branch))
					print question_path


					query_action = d[locals()['last_state']]['branches'][locals()['branch']][2]

					query_addition = d[locals()['last_state']]['branches'][locals()['branch']][1]

					if query_action == 'add_to_query':
						cursor.execute(query + query_addition)
						results = cursor.fetchall()
						if results != []:
							query = query + query_addition
							print "all: ", results

	print "next state", next_state				
	return next_state


def project_logic():
	global stored_info
	# set the current time --> not dealing with this now
	# stored_info.setdefault('current_time', time.strftime("%H:%M"))

	x = 1
	while True:
		if x not in d:
			break
		# prints the next question
		print d[locals()['x']]['bot_statement']

		# gets an answer from the user
		answer = raw_input()
		clean_answer = answer.split()
		# clean_answer = [word for word in answer.split() if word not in stopword_list]
		# print clean_answer

		# gets the value for that branch
		# for item in d[locals()['x']]['branches']:
		# 	for word in clean_answer:
		# 		if word in item:
		# 			next_point = d[locals()['x']]['branches'][locals()['item']]
		# 			x = next_point

		for item in d[locals()['x']]['branches']:
			for each in item:
				if each in clean_answer:
					print each
					next_point = d[locals()['x']]['branches'][locals()['item']]
					print next_point
					x = next_point


# [1, 2, 3, 4] --> list of question #s for order and to keep track of its state
# state machine
# the function is a stateless track
# adding the query string after each branch
# no while loop, pass the current state and the answer into the project_logic function	
# my chat bot as a state machine --> each question is a state, with the branches as transitions
# should i write a class that represents each node --> current state, next state, etc.

	

def main():
	start = raw_input().lower()
	if "hi" in start or "hello" in start and "ronnie" in start:
		print "Well hello there friend!"
		print traverse_questions(0, None)
	else:
		print "I'm Ronnie. I have just met you and a looove you will you be my master?"


if __name__ == "__main__":
	main()