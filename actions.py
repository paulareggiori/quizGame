"""
This module contains Actions class contains all game
actions and messages.
"""


class Actions:
	WELCOME_TEXT = "Hello and welcome to my little quiz!"
	GOODBYE_TEXT = "Thank you and goodbye!"

	def welcome(self):
		print(self.WELCOME_TEXT)

	def start_quiz(self):
		answer = input("Do  quiz you want to start the quiz? ")
		if answer.lower() == "yes":
			return True
		elif answer.lower() == "y":
			return True
		else:
			return False

	def final_score(self, score):
		print("Your final score is, {} out of 10.".format(score))

	def goodbye(self):
		print(self.GOODBYE_TEXT)
