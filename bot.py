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
# join_half = "select name from restaurants as r"
# where_half = " where"



def join(categories_alias, join_query):
	join_query = join_query + " join categories as %s on r.id=%s.business_id" % (categories_alias, categories_alias)
	return join_query

d = {
	1: {
		'return': 'question',
		'bot_statement': 'Are you hungry?',
		'branches': {
			('yes', 'ya', 'yeah', 'sure', 'definitely'): [2, " WHERE EXISTS(SELECT 1 FROM categories AS c1 WHERE c1.business_id=r.id AND c1.category NOT IN('Bars', 'Breweries', 'Coffee & Tea', 'Dive Bars', 'Sports Bars', 'Cafes', 'Tea Rooms', 'Wine Bars', 'Pubs'))", "where_exists", 'c1'],
			('no', 'nope', 'nah', 'not'): [3, " WHERE EXISTS(SELECT 1 FROM categories AS c1 WHERE c1.business_id=r.id AND c1.category IN ('Bars', 'Breweries', 'Coffee & Tea', 'Dive Bars', 'Sports Bars', 'Cafes', 'Tea Rooms', 'Wine Bars', 'Pubs'))", 'where_exists', 'c1']
		}
	},
	2: {
		'return': 'question',
		'bot_statement': 'Snack or meal?',
		'branches': {
			('snack',): [5, " AND EXISTS(SELECT 1 FROM categories as c2 WHERE c2.business_id=r.id AND c2.category IN ('Bakeries', 'Ice Cream & Frozen Yogurt', 'Donuts', 'Cafes', 'Candy Stores', 'Desserts'))", 'where_exists', "c2"],
			('meal',): [4, " AND EXISTS(SELECT 1 FROM categories as c2 WHERE c2.business_id=r.id AND c2.category IN ('Restaurants'))", "where_exists", None]
		}
	},
	3: {
		'return': 'question',
		'bot_statement': 'Ok then. Is a stiff drink in order?',
		'branches': {
			('yes', 'ya', 'yeah', 'sure', 'definitely'): [9, " AND EXISTS(SELECT 1 FROM categories as c3 WHERE c3.business_id=r.id AND c3.category IN ('Bars', 'Breweries', 'Dive Bars', 'Sports Bars', 'Wine Bars', 'Pubs'))", "where_exists", None],
			('no', 'nope', 'nah', 'not'): [10, " AND EXISTS(SELECT 1 FROM categories as c3 WHERE c3.business_id=r.id AND c3.category IN ('Coffee & Tea', 'Cafes', 'Tea Rooms'))", "where_exists", None]
		}
	},
	4: {
		'return': 'question',
		'bot_statement': 'Are we thinking breakfast, lunch or dinner?',
		'branches': {
			('breakfast', 'brunch'): [7],
			('lunch'): [6],
			('dinner'): [6]
		}
	},
	5: {
		'return': 'question',
		'bot_statement': 0#QUERY*****
	},
	6: {
		'return': 'question',
		'bot_statement': 'Eat in, take out, or delivery?',
		'branches': {
			('eat in', 'in'): [7],
			('take out', 'tk', 'out', 'pick up'): [7],
			('delivery', 'deliver', 'delivered'): [7]
		}
	},
	7: {
		'return': 'question',
		'bot_statement': 'What about dietary concerns? Gluten? Soy? Vegan? Etc.?',
		'branches': {
			('nope', 'no', 'nah', 'none', 'negative'): [8],
			('vegetarian',): [8],
			('vegan',): [8],
			('gf', 'gluten', 'gluten-free'): [8],
			('soy',): [8],
			('halal',): [8]
		}
	},
	8: {
		'return': 'question',
		'bot_statement': "And last but not least, what's your price range?",
		'branches': {

		}
	},
	9: {
		'return': 'question',
		'bot_statement': 'Righto, bar it is! What kind of vibe were we thinkin? Romantic? Intimate...? Chill yo?',
		'branches': {
			('intimate',): 0,####QUERY,
			('romantic',): [11],
			('chill', 'casual'): [12]
		}
	},
	10: {
		'return': 'question',
		'bot_statement': 'Do you have a preference for coffee or tea?\nTea, right? You know you like tea! (Tea.)',
		'branches': {
			('cafe', 'coffee', 'cappuccino'): 0,###########,
			('tea', 'leaf', 'leaves'): 0,#######,
			('nah', 'nope', 'no preference', "don't care", 'negative'): 0######
		}

	},
	11: {

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

	clean_answer = user_answer.split()
	for branch in d[locals()['last_state']]['branches']:
			for each in branch:
				if each in clean_answer:
					print each
					next_state = d[locals()['last_state']]['branches'][locals()['branch']][0]
					answer_branch = branch
					question_path.append((last_state, answer_branch))
					print question_path

					# cat_alias = d[locals()['last_state']]['branches'][locals()['branch']][3]
					# fxn = d[locals()['last_state']]['branches'][locals()['branch']][2]
					query_action = d[locals()['last_state']]['branches'][locals()['branch']][2]
					query_addition = d[locals()['last_state']]['branches'][locals()['branch']][1]
					if query_action == 'where_exists':
						query = query + query_addition
						# join_half = fxn(cat_alias, join_half)
					# filters = d[locals()['last_state']]['branches'][locals()['branch']][1]
					# where_half = where_half + filters
					# query = join_half + where_half
					print query
					cursor.execute(query)
					print "all: ", cursor.fetchall()


	# query = query.filter(f)
	# print "new query: ", query
	# newq = query.filter((model.Category.category=='Bakeries') | (model.Category.category=='Dessert') | (model.Category.category=='Ice Cream & Frozen Yogurt'))
	
	# run_query = model.session.query(model.Restaurant).join(model.Category).filter(model.Category.category=='Food').filter((model.Category.category=='Bakeries') OR (model.Category.category=='Dessert') OR (model.Category.category=='Ice Cream & Frozen Yogurt')).all()

	# run_query = model.session.query(model.Restaurant).filter(model.Restaurant.categories.any(model.Category.category=='Bakeries')).all()

	# run_query = model.session.query(model.Restaurant).join(model.Category).filter(or_(model.Category.category=='Bakeries', model.Category.category=='Ice Cream & Frozen Yogurt')).filter(model.Category.category=='Food').all()




	# for i in run_query[0].categories:
	# 	print i.category

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
		print "What city are you in?"
		city = raw_input()
		traverse_questions(0, None)
	else:
		print "I'm Ronnie. I have just met you and a looove you will you be my master?"


if __name__ == "__main__":
	main()