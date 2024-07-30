valid_words_filename: str = 'validwords.txt'
valid_words_parsed_filename: str = 'validwords-parsed.txt'
answers_filename: str = 'answers.txt'
answers_parsed_filename: str = 'answers-parsed.txt'

# apologies for the pretty horrific code here, this only has to run once and then never again.

def read_valid_words(filename: str) -> list[str]:
    with open(filename, 'r') as vw_file:
        valid_words: list[str] = [word.upper()[:-1] for word in vw_file]
    return valid_words

def read_answers(filename: str) -> list[str]:
    with open(filename, 'r') as ans_file:
        answers: list[str] = [line[-6:-1].upper() for line in ans_file]
    return answers

valid_words: list[str] = read_valid_words(valid_words_filename)
cutoff_letters: list[str] = ['E', 'L', 'Q', 'T', 'garbage']
last_index: int = 0
valid_words_split: list[str] = []

# the following is probably the least efficient way possible, but I only have to run it once so I don't care.
for index, word in enumerate(valid_words):
    if word[0] == cutoff_letters[0]:
        cutoff_letters = cutoff_letters[1:]
        valid_words_split.append(''.join(valid_words[last_index:(index)]))
        last_index: int = index

valid_words_split.append(''.join(valid_words[last_index:]))

with open(valid_words_parsed_filename, "w") as vwp_file:
    for string in valid_words_split:
        vwp_file.write(string + '\n')

with open(answers_parsed_filename, "w") as ansp_file:
    ansp_file.write(''.join(read_answers(answers_filename)))