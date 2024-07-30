valid_words_filename: str = 'validwords.txt'
answers_filename: str = 'answers.txt'

def read_valid_words(filename: str) -> list[str]:
    with open(filename, 'r') as vw_file:
        valid_words: list[str] = [word.upper() for word in vw_file]
    return valid_words

def read_answers(filename: str) -> list[str]:
    with open(filename, 'r') as ans_file:
        answers: list[str] = [line[-5:].upper() for line in ans_file]
    return answers

def concatenate(strings: list[str]) -> str:
    return ''.join(strings)