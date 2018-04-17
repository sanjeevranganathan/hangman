import unittest
from hangman import get_guessed_word

class TestMe(unittest.TestCase):
	def test_get_guessed_word(self):
		self.assertNotEqual(get_guessed_word('naveen',['n','v','e']),'n_vee')
		self.assertEqual(get_guessed_word('naveen',['n','v','e']),'n_veen')

if __name__ == '__main__':
	unittest.main()
