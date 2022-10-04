import random
from words import words
import string

print('you get infinite chances since i put in a 24 character word ;)')

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print('you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter is word_letters:
                word_letters.remove(user_letter)
                print('')

        elif user_letter in used_letters:
            print('you just guessed that letter...?')

        else:
            print('invalid character')
            
    else:
        print('You won! :D you guessed the word:', word, '!!')


if __name__ == '__main__':
    hangman()
