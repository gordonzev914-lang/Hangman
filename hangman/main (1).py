import words
import new_game
import myio

secret_word = words.choose_secret_word(["cat","fat","wolf"])
# display=words.creates_a_list_of_underscores(word)
# display_list=[]
# letters_already_guesst=[]


# check if counter ends or he won!


def game_init():
    limit = int(input("enter a limit"))
    correct_letters_guessed = []
    round_counter = 0
    letters_of_word = words.word_into_list(secret_word)
    while (len(letters_of_word) != len(correct_letters_guessed)) and round_counter < limit:
        # get letter
        letter = myio.prompt_guess()
        # check validity of said letter
        #is_str = myio.is_it_a_str(letter)
        # check if exists in letters_of_word, if yes append it to correctly_guessed
        if letter in letters_of_word and letter not in correct_letters_guessed:
            correct_letters_guessed.append(letter)
        round_counter += 1

    if len(letters_of_word) == len(correct_letters_guessed):
        print("You Won")
    else:
        print("You lose")



game_init()
            








