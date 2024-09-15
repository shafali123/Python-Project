import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from a list
    while '-' in word or ' ' in word:  # this while iterarte until we dont have - and spaces in a word
        word =  random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed


    #getting user input 

    while len(word_letters) > 0:
        #letters used
        #' '.join(['a','b','cd']) --> 'a b cd'
        print('You have these letters:', ' '.join(used_letters))

        # what  current word is (ie W-R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Cuuernt word: ', ' '.join(word_list))



        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have alraedy used that character. Please try again.')
    
        else:
            print("Not a valid charater. Try again")

    #get here when len(words_letter) ==0


user_input = input('Type something: ')
print(user_input)
hangman()
