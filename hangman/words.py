import random
def choose_secret_word(words: list[str]):
    return(random.choice(words))


# def creates_a_list_of_underscores(the_word:str):
#     # for i in range(len(the_word)):
#     #     underscores+=('_')
#     # return underscores
#     return "_" * len(the_word)
# print(creates_a_list_of_underscores("wolf"))

def word_into_list(word,list_of_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],selected_letters=[]):
    for i in list_of_letters:
        if i in word:
            selected_letters.append(i)
    return selected_letters




 