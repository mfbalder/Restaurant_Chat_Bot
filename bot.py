import time

stored_info = {}



d = {
	1: {
		'return': 'question',
		'bot_statement': 'Are you hungry?',
		'branches': {
			'yes': 2,
			'no': 3
		}
	},
	2: {
		'return': 'question',
		'bot_statement': 'Snack or meal?',
		'branches': {
			'snack': 3,
			'meal': 4
		}
	}
}

# start with 1:
	# if 1 has an s in it, get the value of s, save those to the info dictionary
	# follow the branch
# to 2
	# if 2 has a q in it, print that question and get an answer
	# depending on which branch matches the answer, move to that value

def store_data(data_dict, data_attr, value):
	data_dict.setdefault(data, value)


def question(the_question, yes, no):
	print the_question
	answer = raw_input(">")
	if answer.lower() == "yes" or answer.lower() == "ya":
		pass
	if answer.lower() == "no":
		question_dict[no]



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
		answer = raw_input(">")

		# gets the value for that branch
		next_point = d[locals()['x']]['branches'][locals()['answer']]
		print next_point
		x = next_point

	

def main():
	start = raw_input(">")
	if "hi" in start.lower() and "ronnie" in start.lower():
		print "Well hello there friend!"
		project_logic()
	else:
		print "I'm Ronnie. I have just met you and a looove you will you be my master?"


if __name__ == "__main__":
	main()