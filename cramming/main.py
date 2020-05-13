
from random import choice

QUESTIONS = {
    'prepositions': {
        'at': [
            'school', 'home', 'work', 'university', 'the airport', 'the station', 'a bus stop', 'a party', 'the door',
            '6 o\'clock', 'half past two', '7.45',
            'Christmas', 'Easter night', 'the weekend'
        ],

        'in': [
            'France', 'Paris',
            'the kitchen',
            'February', 'June',
            '(the) winter',
            'a shop', 'a museum',
            'a park', 'a garden', 'a car',
            '2011',
            'the morning', 'the afternoon', 'the evening'
        ],

        'on': [
            'a bike', 'a bus', 'a train', 'a plane', 'a ship',
            '1st March',
            'Tuesday', 'New Year\'s Day', 'Valentine\'s Day',
            'the floor', 'a table', 'a shelf', 'the balcony', 'the roof', 'the wall'
        ]
    },

    'ed': {
        'd': [
            'turned', 'described', 'complained', 'remained', 'played', 'lived', 'died', 'entered'
        ],

        't': [
            'asked', 'faked', 'watched', 'cooked', 'kicked', 'washed'
        ],

        'id': [
            'painted', 'coincided', 'concluded', 'exaggerated'
        ]

    },

    'tenses': {
        'Present Simple':
            ['regular actions', 'well-known facts'],
        'Present Continuous':
            ['actions in progress now', 'temporary actions'],
        'Present Perfect':
            ['actions in the past with result in the present', 'experience', 'just, already, yet'],
        'Past Simple':
            [
                'actions completed in the past', 'yesterday, last month, 2 days ago',
                'story', 'actions at a stated past time'
            ],
        'Present Perfect Continuous':
            [
                'actions which started in the past, continued to the present and are still in progress, or have just finished',
                'visible consequences'
            ]
    }    
}

QUESTION_NUM_LIMIT = 100

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
""".format(QUESTION_NUM_LIMIT))
print('Choose topic:')

answer = get_answer(QUESTIONS.keys())
if answer == '__exit__':
    print('Bye!')
    quit()
questions = QUESTIONS[answer]


question_num = 0
right_answer_num = 0
for i in range(QUESTION_NUM_LIMIT):
    correct_answer = choice(list(questions))
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
    else:
        right_answer_num += 1
        print('You are right.')
    
print_stat(right_answer_num, question_num)