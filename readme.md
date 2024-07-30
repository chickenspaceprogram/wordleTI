# wordleTI
### A port of Wordle to TI-BASIC

v0.1 (alpha)

wordleTI is currently still in development, and is incomplete.

Notes:

Dec 32/33 2022 were manually removed from the list of words for each day, as these are not valid days, aren't 5 characters long, and would break this program. 

How valid words are broken up:

a-d (1-4) : Str1

e-k (5-11) : Str2

l-p : (12-16) : Str3

q-s : (17-19) : Str4

t-z : (20-26) : Str5

answers: Str6

What things do:

readme.md    - You are here

testing.py   - A python script for testing some of the algorithms used

makestrs.py  - A python script to convert validwords.txt and answers.txt into a format usable by graphing calculators

validwords.txt - Contains every word you're allowed to enter in Wordle.

answers.txt - Contains Wordle's original solutions list. These have changed since Wordle was purchased by the New York Times.


Acknowledgements:
- [SourceCoder 3](https://www.cemetech.net/sc/), an online TI-BASIC IDE
  - Used primarily for converting to TI-BASIC's string format
- [dracos](https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93), a GitHub user who has listed all valid Wordle words
- [Owen Yin](https://medium.com/@owenyin/here-lies-wordle-2021-2027-full-answer-list-52017ee99e86), who has provided the list of Wordle's answers.
