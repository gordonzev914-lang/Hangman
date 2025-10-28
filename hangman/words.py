import random
def choose_secret_word(words: list[str]):
    return(random.choice(words))


def creates_a_list_of_underscores(the_word:str):
    # for i in range(len(the_word)):
    #     underscores+=('_')
    # return underscores
    return "_" * len(the_word)
# print(creates_a_list_of_underscores("wolf"))



 