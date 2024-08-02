valid_words_input: str = 'validwords.txt'
valid_words_output: str = 'validwords-formatted.txt'
answers_input: str = 'answers.txt'
answers_output: str = 'answers-formatted.txt'

# apologies for the pretty horrific code here, this only has to run once and then never again.

def read_valid_words(filename: str) -> list[str]:
    with open(filename, 'r') as vw_file:
        valid_words: list[str] = [word.upper()[:-1] for word in vw_file]
    return valid_words

def read_answers(filename: str) -> list[str]:
    with open(filename, 'r') as ans_file:
        answers: list[str] = [line[-6:-1].upper() for line in ans_file]
        answers[-1] = 'SHAVE' # couldn't figure out how to fix a small bug, so it's been corrected manually
    return answers

valid_words: list[str] = read_valid_words(valid_words_input)
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

with open(valid_words_output, "w") as vwout_file:
    for string in valid_words_split:
        vwout_file.write(string + '\n')

answers: list = read_answers(answers_input)
answers_str6: list = answers[:1000]
answers_str7: list = answers[1000:]

with open(answers_output, "w") as ansout_file:
    ansout_file.write(''.join(answers_str6) + '\n')
    ansout_file.write(''.join(answers_str7))
