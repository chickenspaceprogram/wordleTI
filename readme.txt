wordleTI
A port of Wordle to TI-BASIC

v0.1 (alpha)

wordleTI is currently still in development, and is incomplete.



Notes:

Dec 32/33 2022 were manually removed from the list of words for each day, as these are not valid days, aren't 5 characters long, and would break this program. 

How words are broken up:
a-d (1-4) : Str1
e-k (5-11) : Str2
l-p : (12-16) : Str3
q-s : (17-19) : Str4
t-z : (20-26) : Str5
answers: Str6


Included files:

wordleTI/
|- readme.txt
|- calc-files/
|  |- GETINPUT.8xp
|  |- GETWORD.8xp
|  |- Str1.8xs
|  |- Str2.8xs
|  |- Str3.8xs
|  |- Str4.8xs
|  |- Str5.8xs
|  |- Str6.8xs
|- formatted-words/
|  |- answers-formatted.txt
|  |- validwords-formatted.txt
|- unformatted-words/
|  |- answers.txt
|  |- makestrs.py
|  |- testing.py
|  |- validwords.txt



Acknowledgements:

- SourceCoder 3 (converting .txt files to TI's string format)
URL: cemetech.net/sc

- dracos (list of allowed words)
URL: gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93

- Owen Yin (list of answers)
URL: medium.com/@owenyin/here-lies-wordle-2021-2027-full-answer-list-52017ee99e86

- Josh Wardle (creator of Wordle)
URL: powerlanguage.co.uk

