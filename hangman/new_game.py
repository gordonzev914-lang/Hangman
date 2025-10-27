import words
import myio
import main
secret_dict={}
secret_dict["secret"]
Letters_already_guesst=[]
secret_letters=[]
def letter_Checkir(ch):
    if ch in Letters_already_guesst:
         print("already in list")
    else:    
         Letters_already_guesst.append(ch)
         return ch
    
# print(letter_Checkir(myio.prompt_guess()))
# print(Letters_already_guesst)



def The_comparar(letter,word):
    if letter in list(word):
        print("good guess")
        return secret_letters.append(letter)
    else:
        print("You are wrong")
# print(The_comparator("s","dsa"))

def secret_word_list():
    print(secret_letters)
    return secret_letters

# print(secret_word_list())

# def compar_len(word,secret_letters):
#     if len(word)==len(secret_letters):
#         return 
        










