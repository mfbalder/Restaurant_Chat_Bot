import time
from nltk.corpus import stopwords

stopword_list = stopwords.words("english")

question_path = []
query_filters = []



d = {
	1: {
		'return': 'question',
		'bot_statement': 'Are you hungry?',
		'branches': {
			('yes', 'ya', 'yeah', 'sure', 'definitely'): 2,
			('no', 'nope', 'nah', 'not'): 3
		}
	},
	2: {
		'return': 'question',
		'bot_statement': 'Snack or meal?',
		'branches': {
			('snack',): 4,
			('meal',): 5
		}
	},
	3: {
		'return': 'question',
		'bot_statement': 'Ok then. Is a stiff drink in order?',
		'branches': {
			('yes', 'ya', 'yeah', 'sure', 'definitely'): 6,
			('no', 'nope', 'nah', 'not'): 7
		}
	},
	6: {
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
	for item in d[locals()['last_state']]['branches']:
			for each in item:
				if each in clean_answer:
					print each
					next_state = d[locals()['last_state']]['branches'][locals()['item']]
					question_path.append(next_state)

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
		traverse_questions(0, None)
	else:
		print "I'm Ronnie. I have just met you and a looove you will you be my master?"


if __name__ == "__main__":
	main()