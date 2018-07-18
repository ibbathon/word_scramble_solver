#!/usr/bin/env python3
# Author: Ibb Marsh
# Created: 2018-07-17

import sys

class WSSolver:
	DICT_FILE_NAME = "dictionary.txt"

	def __init__ (self, argv):
		self.letters = sorted(argv[1])
		self.letterset = set(argv[1])

	def run (self):
		validwords = []
		with open(self.DICT_FILE_NAME,'r') as f:
			for word in f:
				word = word.strip()
				wordset = set(word)
				if wordset <= self.letterset and self.issubword(word):
					validwords.append(word)
		validwords.sort(key=len)
		print(validwords)

	def issubword (self, otherword):
		for l in self.letterset:
			if self.letters.count(l) < otherword.count(l):
				return False
		return True


if __name__ == '__main__':
	wss = WSSolver(sys.argv)
	wss.run()
