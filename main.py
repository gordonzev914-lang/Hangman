import words
import new_game
import myio

word = words.choose_secret_word(["נמר"])
display=words.creates_a_list_of_underscores(word)
# display_list=[]
# display_list=[]
# display=display.split()
display_list=display.split()
# print(display_list)
# letters_already_guesst=[]
print(f"{display_list} display works")
print(word)
round_limit=int(input("enter a limit"))


def game_init(the_word= word, the_guess = display_list , limit = round_limit , counter=0, letters_already_guesst=[]):
    mistakes_counter=0
    stopping_conditions=True
    if counter>=limit:
        stopping_conditions=False
    while stopping_conditions is True:
        stopping_conditions=True
        if counter>=limit:
            stopping_conditions=False
        print(the_guess)
        letter=myio.prompt_guess()
        counter+=1
        print(counter)
        is_str=myio.is_it_a_str(letter)
        if is_str==False:
            print("not good")
            mistakes_counter+=1
            continue
        
            # letter=myio.prompt_guess()
        elif  is_str==True:
            has_been_given=new_game.letter_checkir(letter,letters_already_guesst)    
               
            if has_been_given==True:
                    print("already in list")
                    mistakes_counter+=1
                    continue
                
            else:
                letters_already_guesst.append(letter)
                letter_within_a_word=new_game.The_comparar(letter,the_word)
                if letter_within_a_word==False:
                    print("You are wrong")
                    mistakes_counter+=1
                    continue
                elif letter_within_a_word==True:
                    print("good guess")
                    for i in range(len(the_word)):
                        if the_word[i]==letter:
                            print(i)
                            the_guess[i]=the_word[i]
                            
                    # the_guess[counter-mistakes_counter]=letter
                    # the_guess.append(letter)
                    print(the_guess)
        list_content_checker=new_game.compar_lenth_of_list_to_secret(the_word,display)
        if list_content_checker==False:
            stopping_conditions=True
            print(mistakes_counter)
            continue
        elif list_content_checker==True:
            stopping_conditions=False
            print("You won")
    # print(mistakes_counter)
    # print(the_guess)
    print("game over")
game_init()
            








