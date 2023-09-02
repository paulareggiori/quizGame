"""
This is a simple Questions game that takes in the answers
from a user and in the end of the given questions, will show
a overall score.
"""
from actions import Actions
from questions import Questions
from validation import Validation

# Stater objects
questions = Questions()
game_actions = Actions()
validation = Validation()

# Welcome user
game_actions.welcome()

# Ask if they want to start playing

if game_actions.start_quiz():
	counter = questions.get_counter()
	while counter < 6:
		# Trigger questions
		questions.ask_question()
		answer = questions.get_answer()

		# Validate answer and add to score
		validation.check_answer(answer, counter)
		counter +=1

	# When questions are done, show finished score
	final_score = validation.final_score()
	game_actions.final_score(final_score)

# Goodbye message
game_actions.goodbye()
