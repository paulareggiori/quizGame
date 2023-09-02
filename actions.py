"""
This module contains Actions class contains all game
actions and messages.
"""
from termcolor import colored


class Actions:
	WELCOME_TEXT = colored("Hello and welcome to my little quiz!", "yellow", attrs=["reverse", "blink"])
	GOODBYE_TEXT = colored("Thank you and goodbye!", "yellow", attrs=["reverse", "blink"])

	def welcome(self):
		print(self.WELCOME_TEXT)

	def start_quiz(self):
		answer = input(colored("Do  quiz you want to start the quiz? ", "yellow", attrs=["blink"]))
		if answer.lower() == "yes":
			return True
		elif answer.lower() == "y":
			return True
		else:
			return False

	def final_score(self, score):
		print(colored("Your final score is, {} out of 10.", "yellow", attrs=["blink"]).format(score))

	def goodbye(self):
		print(self.GOODBYE_TEXT)
