from words import choose_secret_word
from new_game import letter_Checkir
from new_game import secret_word_list
from new_game import The_comparar
from new_game import compar_len
from myio import prompt_guess
word = choose_secret_word()
counter=0
game_allower=False
while game_allower is False:
    def game_init():
        letters_already_guesst=[]
        secret_letters=[]
        letter=prompt_guess()
        lc=letter_Checkir(letter,letters_already_guesst)
        if lc==True:
            print("already in list")
            counter+=1
        else:
            letters_already_guesst.append(letter)
            counter+=1
            tc=The_comparar(letter,word)
            if tc==False:
                print("You are wrong")
            elif tc==True:
                print("good guess")
                secret_letters.append(letter)
        swl=secret_word_list()
        compar_len(word,secret_letters)
                        








