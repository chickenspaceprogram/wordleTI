import makestrs

valid_words: list[str] = makestrs.read_valid_words(makestrs.valid_words_filename)

last_letter: str = valid_words[0][0]
num_of_each_letter: list[int] = [0]

for word in valid_words:
    if word[0] != last_letter:
        num_of_each_letter.append(1)
    else:
        num_of_each_letter[-1] += 1
    last_letter = word[0]

alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
max_RAM: int = 18000
word_size: int = 5
string_var_size: int = 11 # the size of a string variable with no elements
str_start: int = 0 # did not know what to name this, but this variable keeps track of which letter the current partitioned string starts on.

print("\nLetters : Size\n")
for index, value in enumerate(num_of_each_letter):
    if (sum(num_of_each_letter[str_start:(index + 1)]) * word_size + string_var_size) > max_RAM:
        print(f"{alphabet[str_start:index]} : {sum(num_of_each_letter[str_start:(index)]) * word_size + string_var_size}")
        str_start = index

print(f"{alphabet[str_start:(index + 1)]} : {sum(num_of_each_letter[str_start:(index + 1)]) * word_size + string_var_size}")