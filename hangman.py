# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
DEBUG = 1
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word=""
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            guessed_word = guessed_word+secret_word[i]
        else:
            guessed_word = guessed_word+'_'
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_str = 'abcdefghijklmnopqrstuvwxyz'
    ret_str = ''
    for i in range(len(all_str)):
        if all_str[i] not in letters_guessed:
            ret_str = ret_str + all_str[i]
    return ret_str
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
    
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_len = len(secret_word)
    num_guesses  = 6
    letters_guess = []
    # while we have guesses. Get the available letters and check if
    # the input given is a new letter and add to the list of letters.
    # check if the word has been guessed
    while num_guesses >= 1 and not is_word_guessed(secret_word, letters_guess):
        available_letters = get_available_letters(letters_guess)
        print('Guess',get_guessed_word(secret_word, letters_guess),' length=', word_len,' and number of guesses are',num_guesses)
        instr = input('Enter a letter among '+available_letters+'\n')
        while len(instr) != 1 or instr not in available_letters:
            print('Should enter one letter not in the list given')
            instr = input('Enter a letter among '+available_letters+'\n')    
        letters_guess.append(instr)
        if instr not in secret_word:
            num_guesses -= 1
    if is_word_guessed(secret_word, letters_guess):
        print('You Got it!')
    else:
        print("Didn't get", secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    if len(my_word)==len(other_word):
        for i in range(len(my_word)):
            if my_word[i]!='_' and my_word[i]!=other_word[i]:
                return False
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for eachword in wordlist:
        if match_with_gaps(my_word, eachword):
            print(eachword)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_len = len(secret_word)
    num_guesses  = 6
    letters_guess = []
    # while we have guesses. Get the available letters and check if
    # the input given is a new letter and add to the list of letters.
    # check if the word has been guessed
    while num_guesses >= 1 and not is_word_guessed(secret_word, letters_guess):
        available_letters = get_available_letters(letters_guess)
        my_word = get_guessed_word(secret_word, letters_guess)
        print('Guess',my_word,' length=', word_len,' and number of guesses are',num_guesses)
        instr = input('Enter a letter among '+available_letters+'\n')
        while len(instr) != 1 or instr not in available_letters and instr!='*':
            print('Should enter one letter not in the list given')
            instr = input('Enter a letter among '+available_letters+'\n')
        if instr == '*':
            print('You loose one turn, but here is your hint')
            show_possible_matches(my_word)
        else:
            letters_guess.append(instr)
            if instr not in secret_word:
                num_guesses -= 1
    if is_word_guessed(secret_word, letters_guess):
        print('You Got it!')
    else:
        print("Didn't get", secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    if DEBUG >= 2:
        print("match_with_gaps('my_word','mynword')", match_with_gaps('my_word','mynword'))
        print("match_with_gaps('my_word','myword')",match_with_gaps('my_word','myword'))
    if DEBUG>=2:
        print("is_word_guessed('thisletters',['t','h','i','s','l','e','r'])",is_word_guessed('thisletters',['t','h','i','s','l','e','r']))
        print("is_word_guessed('thisletters',['t','h','i','s','l','e'])",is_word_guessed('thisletters',['t','h','i','s','l','e']))
    if DEBUG>=2:
        print("get_guessed_word('thisletters',['t','h','i','s','l','e','r'])",get_guessed_word('thisletters',['t','h','i','s','l','e','r']))
        print("get_guessed_word('thisletters',['t','h','i','s','l','e'])",get_guessed_word('thisletters',['t','h','i','s','l','e']))
        
    # secret_word = choose_word(wordlist)
    # secret_word = 'hungry'
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
