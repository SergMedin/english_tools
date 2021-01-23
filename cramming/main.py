from random import choice
import config

def get_answer(options):
    possible_answers = {}
    for i, key in enumerate(options):
        possible_answers[i+1] = key
        print('\t{}: {}'.format(i+1, key))

    while True:
	    try:
	    	answer_raw = input()
	    	if answer_raw in ['exit']:
	    		return '__{}__'.format(answer_raw)
	    	answer_id = int(answer_raw)
	    	if answer_id not in possible_answers.keys():
	    		print('Incorrect choice! Try again')
	    		continue
	    	break
	    except ValueError:
	    	print('Incorrect choice! Try again')

    answer = possible_answers[answer_id]
    
    return answer

def print_stat(right_answer_num, question_num):
	print()
	print('Share of right answers: {}%'. format(round(right_answer_num/question_num*100)))

print("""
You can type 'exit' if you want to stop cramming.
Question limit is {}.
""".format(config.QUESTION_NUM_LIMIT))
print('Choose topic:')

answer = get_answer(config.QUESTIONS.keys())
if answer == '__exit__':
    print('Bye!')
    quit()
questions = config.QUESTIONS[answer]


question_num = 0
right_answer_num = 0
questions_with_mistakes = []
for i in range(config.QUESTION_NUM_LIMIT):
    correct_answer = choice(list(questions))
    # print('length of questions:', len(questions[correct_answer]))
    question = choice(questions[correct_answer])
    
    question_num += 1
    print()
    print('{}:\t{}'.format(i+1, question.upper()))
    
    answer = get_answer(questions.keys())
    if answer == '__exit__':
    	print('Bye!')
    	break

    if answer != correct_answer:
        print('You are wrong. Correct answer: {}'.format(correct_answer))
        questions[correct_answer].append(question)
    else:
        right_answer_num += 1
        print('You are right.')
    
print_stat(right_answer_num, question_num)