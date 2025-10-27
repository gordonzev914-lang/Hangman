import words
import new_game
import myio

word = words.choose_secret_word(["נמר","גמל","פיל","קוף"])
counter=0
round_limit=int(input("enter a limit"))
game_allower=False
compare = new_game.compar_len(word,)
def game_init():
    while game_allower is False:
        letters_already_guesst=[]
        secret_letters=[]
        letter=myio.prompt_guess()
        lc=new_game.letter_Checkir(letter,letters_already_guesst)
        if lc==True:
            print("already in list")
            counter+=1
        else:
            letters_already_guesst.append(letter)
            counter+=1
            tc=new_game.The_comparar(letter,word)
            if tc==False:
                print("You are wrong")
            elif tc==True:
                print("good guess")
                secret_letters.append(letter)
        swl=new_game.secret_word_list()
        print(swl)
        cl=new_game.compar_len(word,secret_letters)
        cm=new_game.counter_monitor(counter,round_limit)
game_init()
            








