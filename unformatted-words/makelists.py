import csv

def read_valid_words(filename: str) -> list[str]:
    with open(filename, 'r') as vw_file:
        valid_words: list[str] = [word.upper()[:-1] for word in vw_file]
    return valid_words

def read_answers(filename: str) -> list[str]:
    with open(filename, 'r') as ans_file:
        answers: list[str] = [line[-6:-1].upper() for line in ans_file]
        answers[-1] = 'SHAVE' # couldn't figure out how to fix a small bug, so it's been corrected manually
    return answers

def convert_str(string: str):
    global letter_to_num
    length = len(string)
    return_val: int = 0
    for index, letter in enumerate(string, 1):
        return_val += letter_to_num[letter] * (26 ** (length - index))
    return return_val

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_to_num: dict = dict()
for index, letter in enumerate(alphabet):
    letter_to_num[letter] = index

valid_words: list = read_valid_words('validwords.txt')
answers: list = read_answers('answers.txt')
all_words: list = valid_words + answers

# the following is horrible but easy

valid_words: list = [all_words[(i * 3456):(i * 3456 + 3456)] for i in range(5)]

valid_words[4] += ['AAAAA'] * (3456 - len(valid_words[4]))

valid_words_num: list[list[int]] = []

# basically taking the first letters from every entry and stuffing them all at the end of each list
# this is done so that each entry can be stored as a base 26 number without losing precision

for list_index, words_list in enumerate(valid_words):
    vw_sublist: list = []
    vw_endlist: list = []
    for word_index in range(0, len(words_list), 2):
        vw_sublist.append(words_list[word_index] + words_list[word_index + 1])
    for index, word in enumerate(vw_sublist):
        vw_endlist.append(word[0])
        vw_sublist[index] = vw_sublist[index][1:]
    for chunk_index in range(0, len(vw_endlist), 9):
        chunk: str = ''
        for letter in vw_endlist[chunk_index:chunk_index + 9]:
            chunk += letter
        vw_sublist.append(chunk)
    valid_words_num.append([convert_str(i) for i in vw_sublist])

for index, value in enumerate(valid_words_num):
    with open(f'list{index + 1}.csv', 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(value)