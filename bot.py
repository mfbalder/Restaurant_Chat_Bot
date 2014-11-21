import time
from nltk.corpus import stopwords

stopword_list = stopwords.words("english")



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
		'query': 
	}
}

# start with 1:
	# if 1 has an s in it, get the value of s, save those to the info dictionary
	# follow the branch
# to 2
	# if 2 has a q in it, print that question and get an answer
	# depending on which branch matches the answer, move to that value

def run_query(data_dict, data_attr, value):
	data_dict.setdefault(data, value)




def project_logic():
	global stored_info
	# set the current time
	stored_info.setdefault('current_time', time.strftime("%H:%M"))

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
		

	

def main():
	start = raw_input().lower()
	if "hi" in start or "hello" in start and "ronnie" in start:
		print "Well hello there friend!"
		project_logic()
	else:
		print "I'm Ronnie. I have just met you and a looove you will you be my master?"


if __name__ == "__main__":
	main()