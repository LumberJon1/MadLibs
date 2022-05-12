
# Define functions to prompt users for types of words

def prompt_word(word_type="noun", plural=False):
    """Takes a word_type and plural arguments, and prompts for that type
    of word.  Will generate validation based on plurality and prompt with a(n)"""
    
    # Check whether the prompt should use "a" or "an"
    if word_type == "adjective" or word_type == "adverb" or word_type == "exclamation":
        identifier = "an"
    else:
        identifier = "a"
    
    # TODO: Validate based on plurality
    
    # Output the prompt
    prompt = input("Enter "+identifier+" "+word_type)
    return prompt

   
prompt_word("place")
# Define the string
