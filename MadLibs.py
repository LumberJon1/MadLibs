
# Define the array that will hold the words to use in prompts
prompt_words = ["adjective", "noun", "verb", "noun", "place"]

# Define the array that will store user answers
user_words = []

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

# Define the string that will be formatted with user answers
mad_libs_string = "Once there was a great man who lived in an enormous castle.  With him lived\
    his favorite pet cow and several knights.  One knight, however, would betray him.\
    Unbeknownst to this king, the knight named Sir Floolean had plotted together with \
    the cow to overthrow the king and claim his castle as their own.  So in the dead of \
    night, they crept silently into the king's chambers and cut off his head with a sword.\
    The moral of the story: never trust a cow."

# For every word in the prompt_words array, run prompt_word and store the result in
# the user_words array.
for word in prompt_words:
    user_words.append(prompt_word(word))

# Print the user_words array to test output
print(user_words)
