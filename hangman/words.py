import random
def choose_secret_word(words: list[str]):
    return(random.choice(words))
print(choose_secret_word(["apple", "banana", "cherry"]))