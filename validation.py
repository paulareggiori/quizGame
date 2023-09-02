"""
This module contains Validate class used to check
if the answers of the user are write and keep track
of their score.
"""


class Validation:
	def __init__(self):
		self.score = 0
		self.max_score = 10

	def check_answer(self, answer, counter):
		if counter == 1:
			if answer.lower() in "yes":
				self.add_score()
			else:
				pass
		elif counter == 2:
			if answer.lower() in "yes":
				self.add_score()
			else:
				pass
		elif counter == 3:
			if answer.lower() in "no":
				self.add_score()
			else:
				pass
		elif counter == 4:
			if answer.lower() in "yes":
				self.add_score()
			else:
				pass
		elif counter == 5:
			if answer.lower() in "yes":
				self.add_score()
			else:
				pass
		else:
			pass

	def add_score(self):
		self.score += 1

	def final_score(self):
		self.score = self.score * 20
		final_score = self.score / self.max_score
		return final_score

