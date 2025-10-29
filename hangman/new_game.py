





def letter_checkir(ch,old_guess):
    if ch in old_guess:
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





def compar_lenth_of_list_to_secret(secret_word,the_list):

        print("length the word")
        print(len(secret_word))
        if  len(secret_word)+1==len(the_list):
            return True
        else:
            return False
        












