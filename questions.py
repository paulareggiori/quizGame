"""
This module contains Questions class used to ask
questions in the Questions game.
"""


class Questions:
	def __init__(self):
		self.answer = ""
		self.counter = 1

	def ask_question(self):
		if self.counter == 1:
			print("Question 01: Are most orange cats male?")
			self.answer = input("Your answer: ")
			self.counter += 1
		elif self.counter == 2:
			print("Question 02: Do cats live longer indoors?")
			self.answer = input("Your answer: ")
			self.counter += 1
			return self.answer
		elif self.counter == 3:
			print("Question 03: Are cats very active throughout the whole day?")
			self.answer = input("Your answer: ")
			self.counter += 1
			return self.answer
		elif self.counter == 4:
			print("Question 04: Can cats see well in low light?")
			self.answer = input("Your answer: ")
			self.counter += 1
			return self.answer
		elif self.counter == 5:
			print("Question 05: Do you like cats?")
			self.answer = input("Your answer: ")
			self.counter += 1
			return self.answer
		elif self.counter == 6:
			print("We are done with all the questions!")
			self.counter += 1

	def get_counter(self):
		return self.counter

	def get_answer(self):
		return self.answer
