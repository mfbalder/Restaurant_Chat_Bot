import time
from nltk.corpus import stopwords
import model

stopword_list = stopwords.words("english")

city = None
question_path = []
query_filters = []



d = {
	1: {
		'return': 'question',
		'bot_statement': 'Are you hungry?',
		'branches': {
			('yes', 'ya', 'yeah', 'sure', 'definitely'): [2, 'model.session.query(model.Restaurant).join(model.Category).filter((model.Category.category=="Food") | (model.Category.category=="Restaurant")).all()'],
			('no', 'nope', 'nah', 'not'): [3]
		}
	},
	2: {
		'return': 'question',
		'bot_statement': 'Snack or meal?',
		'branches': {
			('snack',): 5,
			('meal',): 4
		}
	},
	3: {
		'return': 'question',
		'bot_statement': 'Ok then. Is a stiff drink in order?',
		'branches': {
			('yes', 'ya', 'yeah', 'sure', 'definitely'): 9,
			('no', 'nope', 'nah', 'not'): 10
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
		'return': 'answer',
		'bot_statement': 'Righto, bar it is!',
		'query': None
	}
}


def run_query(data_dict, data_attr, value):
	data_dict.setdefault(data, value)

def traverse_questions(last_state, user_answer):
	"""last state --> the state that a question was just asked from (int)
	   user_answer --> the user's answer to that question (str)

	   Checks that state's branches to see which of them match the answer.
	   Gets the next state from that branch.
	   Adds that state to the list tracking the path of states.

	   Returns the next state"""

	global question_path



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
					# question_path.append(next_state)
					filtered_query = eval(d[locals()['last_state']]['branches'][locals()['branch']][1])
					# print r[0].name

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