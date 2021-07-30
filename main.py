import random

def play():
    lives = 6
    # pick a random word from a predefine list
    word = select_random_word()
    display_word = create_display_list(word)
    guess_list = []

    # if player out of lives, game over
    # else keep playing (while loop)
    while check_lives(lives):

    # display the blank spots where each spot represents the letter from the word
        display_letter_spots(display_word)

    # display a list of guesses that the player has made (if any)
        display_guesses(guess_list)

    # ask the user to guess a letter
        while True:
            entry = input("Please enter a letter: ")
            if len(entry) != 1:
                print("Invalid response")
                continue
            else:
                break

        # add the letter to a list of guesses
        guess_list.append(entry)

        # check if the letter is in the word
        match_indexes = check_guess_with_word(entry, word)


        # if letter is not in the word
        # draw next part of the hangman
        if len(match_indexes) == 0:
            lives -= 1
            draw_body(lives, word)

        # if letter is in the word add letter to the display
        display_word = replace_list_with_letter(entry,display_word, match_indexes)
        print(display_word)

        if check_win(display_word, word):
            break

# draw hangman based on the number of lives left
def draw_body(lives, word):
    if lives == 5:
        print(" 0")
    elif lives == 4:
        print(" O")
        print("|")
    elif lives == 3:
        print(" O")
        print("/|")
    elif lives == 2:
        print(" O")
        print("/|\\")
    elif lives == 1:
        print(" O")
        print("/|\\")
        print("/")
    elif lives == 0:
        print(" O")
        print("/|\\")
        print("/ \\")
        print("You lost")
        print(f"The word was {word}")

# randomly select a word from a predefined list
# return the word
def select_random_word():
    word_lst = ['mom', 'scene', 'example', 'war', 'control', 'deer', 'condition', 'territory', 'minister', 'rifle',
                'stranger', 'country', 'snake', 'health', 'mice', 'harbor', 'coat', 'ship', 'horse', 'baby']
    chosen_word = random.choice(word_lst)
    return chosen_word

# pass in a word
# display blanks based on number of letters
# update the display word as users guess correct letters
def display_letter_spots(display_word):
    converted_list = " ".join(display_word)
    print(converted_list)

# create a list of underscores (blanks) based on length of word
def create_display_list(word):
    display_list = []
    for character in word:
        display_list.append("_")
    return display_list

# print out the current list of guesses that the user have made
def display_guesses(guess_list):
    guesses = ", ".join(guess_list)
    print(f"Here are your previous guesses: {guesses}")

# take guess and determine if the guess letter is in the word
# return a list of index value where the guess matches in the word
# return -1 if no matches were found
def check_guess_with_word(entry, word):
    match_list = []
    index_found = 0
    starting_point = 0
    while index_found != -1:
        index_found = word.lower().find(entry, starting_point)
        starting_point = index_found + 1
        if index_found != -1:
            match_list.append(index_found)
    return match_list

# replaces the index of the list with a correct entry
def replace_list_with_letter(entry, display_list, match_list):
    for number in match_list:
       display_list[number] = entry
    return display_list

# check if the user has more than 0 lives
# return True if user's lives > 0
# return False if user's lives <= 0
def check_lives(lives):
    if lives > 0:
        return True

def check_win(display_word, word):
    display_word_combined = "".join(display_word)
    if display_word_combined == word.lower():
        print("You have won the game")
        return True
    else:
        return False

if __name__ == "__main__":
    play()
