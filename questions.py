"""
This module contains Questions class used to ask
questions in the Questions game.
"""
from termcolor import colored


class Questions:
	def __init__(self):
		self.answer = ""
		self.counter = 1

	def ask_question(self):
		if self.counter == 1:
			print(colored("Question 01: Are most orange cats male?", "magenta", attrs=["blink"]))
			self.answer = input(colored("Your answer: ", "white", attrs=["blink"]))
			self.counter += 1
		elif self.counter == 2:
			print(colored("Question 02: Do cats live longer indoors?", "magenta", attrs=["blink"]))
			self.answer = input(colored("Your answer: ", "white", attrs=["blink"]))
			self.counter += 1
			return self.answer
		elif self.counter == 3:
			print(colored("Question 03: Are cats very active throughout the whole day?", "magenta", attrs=["blink"]))
			self.answer = input(colored("Your answer: ", "white", attrs=["blink"]))
			self.counter += 1
			return self.answer
		elif self.counter == 4:
			print(colored("Question 04: Can cats see well in low light?", "magenta", attrs=["blink"]))
			self.answer = input(colored("Your answer: ", "white", attrs=["blink"]))
			self.counter += 1
			return self.answer
		elif self.counter == 5:
			print(colored("Question 05: Do you like cats?", "magenta", attrs=["blink"]))
			self.answer = input(colored("Your answer: ", "white", attrs=["blink"]))
			self.counter += 1
			return self.answer
		elif self.counter == 6:
			print(colored("We are done with all the questions!", "yellow", attrs=["blink"]))
			self.counter += 1

	def get_counter(self):
		return self.counter

	def get_answer(self):
		return self.answer
