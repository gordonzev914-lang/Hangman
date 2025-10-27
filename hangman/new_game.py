import words
import myio
import main
secret_dict={}
secret_dict["secret"]
Letters_already_guesst=[]
secret_letters=[]
def letter_Checkir(ch):
    if ch in Letters_already_guesst:
        return True
    else:    
        
        return False
    
# print(letter_Checkir(myio.prompt_guess()))
# print(Letters_already_guesst)



def The_comparar(letter,word):
    if letter in list(word):
        
        return True
    else:
        return False
# print(The_comparator("s","dsa"))

def secret_word_list():
    return secret_letters

print(secret_word_list())

def compar_len(word,secret_letters):
    if len(word)==len(secret_letters):
        return True
        

def counter_monitor(c,m):
    if c>=m:
        return main.game_allower is True










