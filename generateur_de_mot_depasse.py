
import random
import string

def generat_password(min_lenht, numbers=True, special_characters=True): 
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
