import pandas

# TODO 1. Create a dictionary in this format:
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {letter: code for (letter, code) in alphabet_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
