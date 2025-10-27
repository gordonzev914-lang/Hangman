import words
import myio

# def game_init(secret=words.choose_secret_word(), max_tries):
#       return  { 
#    "secret": secret                 
#    "display": render_display()          
# "guessed":  validate_guess          
#    "wrong_guesses": int,        
#    "max_tries": max_tries            
#  }


 
def validate_guess(ch: str, guessed: set[str]):
    if ch in guessed:
        return "no"
    else:
        print("good guess")
        return guessed.append(ch)
       

def apply_guess(state:dict,ch: str):
    if ch in state["Guessed_letters"]:
        render_display(ch) 
    else:
        print('guest wrong')

def render_display(ch):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    print(ch)

# apply_guess("cherry","h")  

    

                     